############## LIBRARIES #####################################################
from app import app,base_url
from flask import render_template, request, redirect, url_for, flash
from datetime import date, datetime, timedelta
import re, os, smtplib, uuid, requests, json
from concurrent.futures import ThreadPoolExecutor
import app.routes as fn


#######################################################################
##################  DIFFERENT ENDPOINTS   ##############################

# Administrative homepage for Displaying List of all Tissue Sample Collections
@app.route("/")
def homepage():
    try:
        r = requests.get(f"{base_url}/api/v1/collection")
        response = r.json()
    except Exception as e:
        flash(e, "danger") #danger is a category
        return render_template("index.html", title="Home | Tissue Sample Collection", collections= [], count="0", action="active", year=fn.footer_year())

    if response.get("status"):
        message = response["message"]
        data = response["data"]
        count = response["count"]
        # flash(message, "success") #success is a category
        return render_template("index.html", title="Home | Tissue Sample Collection", collections= data, count=count, action="active", year=fn.footer_year())

    else:
        message = response["message"]
        flash(message, "danger") #danger is a category
        return render_template("index.html", title="Home | Tissue Sample Collection", collections= [], count="0", action="active", year=fn.footer_year())


# Endpoint for displaying list of all Collections
@app.route("/collection")
def show_all_collections():
    return redirect(url_for("homepage"))
    

# Endpoint for Creating a new Collection
@app.route("/collection/create", methods=["GET","POST"])
def create_collection():
    if request.method == "POST":
        payload = {
            "disease_term" : request.form['disease_term'],
            "title" : request.form['title']
        }
        try:
            url = f"{base_url}/api/v1/collection"
            r = requests.post(url=url, json=payload)
            response = r.json()
        except Exception as e:
            flash(e, "danger") #danger is a category
            return redirect(url_for("create_collection"))

        if response.get("status"):
            message = response["message"]
            flash(message, "success") #success is a category
            return redirect(url_for("create_collection"))

        else:
            message = response["message"]
            flash(message, "danger") #danger is a category
            return redirect(url_for("create_collection"))
    
    else:
        return render_template("create_collection.html", title="Create new collection | Tissue Sample Collection", action="active", year=fn.footer_year())


# Endpoint for displaying list of Samples of all collections
@app.route("/sample")
def show_all_samples():
    try:
        r = requests.get(f"{base_url}/api/v1/sample/all")
        response = r.json()
    except Exception as e:
        flash(e, "danger") #danger is a category
        return render_template("all_samples.html", title="Home | Tissue Sample Collection", samples= [], count="0", action="active", year=fn.footer_year())

    if response.get("status"):
        message = response["message"]
        data = response["data"]
        count = response["count"]
        # flash(message, "success") #success is a category
        return render_template("all_samples.html", title="Home | Tissue Sample Collection", samples= data, count=count, action="active", year=fn.footer_year())

    else:
        message = response["message"]
        flash(message, "danger") #danger is a category
        return render_template("all_samples.html", title="Home | Tissue Sample Collection", samples= [], count="0", action="active", year=fn.footer_year())


# Endpoint for Adding a new sample to an existing collection [With Collection_id]
@app.route("/sample/add/<string:collection_id>/", methods=["GET","POST"])
def add_sample1(collection_id):
    if request.method == "POST":
        payload = {
            "donor_count" : request.form['donor_count'],
            "material_type" : request.form['material_type']
        }
        try:
            url = f"{base_url}/api/v1/sample/{collection_id}"
            r = requests.post(url=url, json=payload)
            response = r.json()
        except Exception as e:
            flash(e, "danger") #danger is a category
            return redirect(url_for("add_sample1", collection_id=collection_id))

        if response.get("status"):
            message = response["message"]
            flash(message, "success") #success is a category
            return redirect(url_for("add_sample1", collection_id=collection_id))

        else:
            message = response["message"]
            flash(message, "danger") #danger is a category
            return redirect(url_for("add_sample1", collection_id=collection_id))
    
    else:
        # Validate the collection_id
        url = f"{base_url}/api/v1/collection/{collection_id}"
        validate = fn.make_any_request("GET",url)
        if not validate["status"]:
            return redirect(url_for("add_sample2"))
        return render_template("add_sample1.html", title="Add new Sample | Tissue Sample Collection", action="active", data=validate["data"], year=fn.footer_year())


# Endpoint for Adding a new sample to an existing collection [Without Collection_id]
@app.route("/sample/add", methods=["GET","POST"])
def add_sample2():
    if request.method == "POST":
        payload = {
            "donor_count" : request.form['donor_count'],
            "material_type" : request.form['material_type']
        }
        try:
            url = f"{base_url}/api/v1/sample/{request.form['collection_id']}"
            r = requests.post(url=url, json=payload)
            response = r.json()
        except Exception as e:
            flash(e, "danger") #danger is a category
            return redirect(url_for("add_sample2"))

        if response.get("status"):
            message = response["message"]
            flash(message, "success") #success is a category
            return redirect(url_for("add_sample2"))

        else:
            message = response["message"]
            flash(message, "danger") #danger is a category
            return redirect(url_for("add_sample2"))
    
    else:
        # retrieve all collections
        url = f"{base_url}/api/v1/collection"
        all_collection = fn.make_any_request("GET",url)
        if not all_collection["status"]:
            flash(all_collection["message"], "danger") #danger is a category
            return redirect(url_for("homepage"))
        return render_template("add_sample2.html", title="Add new Sample | Tissue Sample Collection", action="active", data=all_collection["data"], year=fn.footer_year())


# Endpoint for displaying individual collection's samples
@app.route("/sample/<string:collection_id>/", methods=["GET","POST"])
def add_sample(collection_id):
    # Validate the collection_id
    url = f"{base_url}/api/v1/collection/{collection_id}"
    validate = fn.make_any_request("GET",url)
    if not validate["status"]:
        flash(validate["message"], "danger") #danger is a category
        return redirect(url_for("homepage"))
    data1 = validate["data"]

    try:
        url = f"{base_url}/api/v1/sample/{collection_id}"
        r = requests.get(url=url)
        response = r.json()
    except Exception as e:
        flash(e, "danger") #danger is a category
        return render_template("view_sample.html", title="Samples Records | Tissue Sample Collection", action="active", data1=data1, data2=[], count="0", year=fn.footer_year())

    if response.get("status"):
        data2 = response["data"]
        return render_template("view_sample.html", title="Samples Records | Tissue Sample Collection", action="active", data1=data1, data2=data2, count=len(data2), year=fn.footer_year())

    else:
        message = response["message"]
        flash(message, "danger") #danger is a category
        return render_template("view_sample.html", title="Samples Records | Tissue Sample Collection", action="active", data1=data1, data2=[], count="0", year=fn.footer_year())

