# INTRODUCTION

**Developer Assessment 1 – Tissue Sample Collection** involve working on an administrative interface for a system that will allow a Tissue Sample directory to keep track of the number of samples with certain characteristics contained within a larger collection of samples. This assessment is a part of the recruitment requirements for the job: Trainee Software Engineer (Fixed term) (IS236722) - Digital Research Service.

**This Project - Tissue Sample Collection** has been carefully coded in Python programming language and Flask microframework, with clear comments in all of its PY, JS, SCSS and HTML files.
MongoDB has been used to store the data.



##  APPLICATION DIRECTORY TREE STRUCTURE

        |-- LICENSE
        |-- Procfile
        |-- README.md
        |-- app
        |   |-- __init__.py
        |   |-- backend.py
        |   |-- error.py
        |   |-- routes.py
        |   |-- static
        |   |   |-- admin_dist
        |   |   |   |-- css
        |   |   |   |-- img
        |   |   |   `-- js
        |   |   `-- admin_plugins
        |   |       |-- bootstrap
        |   |       |   `-- js
        |   |       |-- chart.js
        |   |       |-- fontawesome-free
        |   |       |   |-- css
        |   |       |   `-- webfonts
        |   |       `-- jquery
        |   |-- templates
        |   |   |-- add_sample1.html
        |   |   |-- add_sample2.html
        |   |   |-- all_samples.html
        |   |   |-- create_collection.html
        |   |   |-- error_page.html
        |   |   |-- includes
        |   |   |   `-- _message.html
        |   |   |-- index.html
        |   |   `-- view_sample.html
        |   `-- view.py
        |-- config.py
        |-- requirements.txt
        |-- run.py


## INSTALLATION AND GUIDE ON HOW TO EXECUTE THE PROJECT ON UBUNTU 20.04LTS

### MongoDB
1. Set up your database account
 
You could setup MongoDB on your machine (https://www.digitalocean.com/community/tutorials/how-to-install-mongodb-on-ubuntu-20-04) or on the cloud (https://www.makeuseof.com/mongodb-cluster-cloud-free-setup/)

**For this Project:** 

- I setup MongoDB Cluster in the Cloud for Free and Get a Connection String From the Cluster (https://www.makeuseof.com/mongodb-cluster-cloud-free-setup/)

- MongoDB Connection String typically looks this:

        mongodb+srv://{username}:{password}@cluster0.1z0kr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority
        
MongoDB cluster will append your username to the string automatically. You'll need to replace {password} with the permission password you set earlier. Also, myFirstDatabase is your database name. Change this to whatever name you like.

### Github
2. clone/download the project from github to your machine

        $ git clone https://github.com/nnorukaemeka/TissueSampleCollection.git


#### Using virtual environment

3. Create a virtual environment

        $ python3 -m venv venv
        $ . venv/bin/activate

4. Install the project's dependancies

        $ pip install requirements.txt           

5. In config.py file, 
- replace {ENTER YOUR SECRET KEY} with a value.
- replace {YOUR MONGODB CONNECTION STRING} with the MongoDB Connection String gotten earlier. Remember to replace {password} in the MongoDB Connection String with the permission password you set while creating MongoDB Cluster.

6. Configure your flask path

        $ export FLASK_APP=run.py


7. Launch application

        $ flask run            

8. Head to http://127.0.0.1:5000

- This project has been developed on an Ubuntu 20.04LTS using Flask server (http://127.0.0.1:5000) and hosted on Heroku cloud at https://tissue-sample-collection.herokuapp.com for remote access.

- Finally, this application works with a connection to a MongoDB database to allow a Tissue Sample directory to keep track of the number of samples with certain characteristics contained within a larger collection of samples.
