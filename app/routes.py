############## LIBRARIES #####################################################
from app import mongo
from datetime import date, datetime, timedelta
import requests, json

#Different collections in the Database
collectiondb = mongo.db.CollectionsDB
samplesdb = mongo.db.SamplesDB

#Function that returns year.
def footer_year():
    today = date.today()
    year = today.strftime("%Y")
    return (year)

#Function that returns current date in format 2022-08-04 10:11:31.881429
def to_day():
    return str(datetime.utcnow() + timedelta(hours=1))


#Function that returns an integer value of the last collection_id in database
def get_last_collectionId():
    records = collectiondb.find().sort("$natural", -1).limit(1)
    if records:
        for record in records:
            return int(record["collection_id"])
        else:
            return 0
    return 0

# Function for making requests
def make_any_request(method, url, payload=None, headers=None, auth=None, proxies=None, timeout=None):
    s = requests.session()
    r = s.request(method=method, url=url, json=payload, headers=headers, auth=auth, proxies=proxies, timeout=timeout)
    resp = json.loads(r.content)
    s.close()
    return resp