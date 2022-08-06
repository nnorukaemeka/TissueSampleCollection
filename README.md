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

### Directory Tree Walkthrough
1. **LICENSE:** A document that provides legally binding guidelines for the use and distribution of software.
2. **Procfile:** It specifies the commands that are executed by the app on Heroku startup. It declares a variety of process types, such as the app’s web server.
3. **README.md:** It is an essential guide that gives other developers a detailed description of the GitHub project.
4. **config.py:** A python configuration file for the application.
5. **requirements.txt:** a file listing all the dependencies for this project.
6. **run.py:** A python file to run the code.
7. **app:** It is an application folder that contains other folders and files for easy launch.
8. **__init__.py:** This python file makes Python treat 'app' folder containing it as a module. Furthermore, this is the first file to be loaded in a module.
9. **backend.py:** This python file contains the APIs which the client-side calls. The POSTMAN documentation for the APIs is found <a href="https://documenter.getpostman.com/view/9697202/VUjMnRGe">here</a>
10. **error.py:** This python file contains the codes that returns error pages.
11. **routes.py:** This python file contains reuseable codes (functions and classes) used in building APIs.
12. **view.py:** This python file contains the client-side code used in making http request to the APIs and rendering HTML files.
13. **static:** In folder structure for a Flask app, the static folder contains assets used by the templates, including CSS files, JavaScript files, and images.
14. **templates:** In folder structure for a Flask app, the templates folder houses html files that contain static data as well as placeholders for dynamic data. Flask uses the Jinja template library to render templates


## INSTALLATION AND GUIDE ON HOW TO EXECUTE THE PROJECT ON UBUNTU 20.04LTS

### MongoDB
1. Set up your database account
 
You could setup MongoDB on your <a href="https://www.digitalocean.com/community/tutorials/how-to-install-mongodb-on-ubuntu-20-04">machine</a> or in the <a href="https://www.makeuseof.com/mongodb-cluster-cloud-free-setup/">cloud</a>

**For this Project:** 

- I setup MongoDB Cluster in the Cloud for Free and Get a Connection String From the Cluster. Step-by-step procedure <a href="https://www.makeuseof.com/mongodb-cluster-cloud-free-setup/">here</a>

- MongoDB Connection String typically looks this:

        mongodb+srv://{username}:{password}@cluster0.1z0kr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority
        
MongoDB cluster will append your username to the string automatically. You'll need to replace {password} with the permission password you set earlier. Also, myFirstDatabase is your database name. Change this to whatever name you like.

### Github
2. clone/download the project from github to your machine

        $ git clone https://github.com/nnorukaemeka/TissueSampleCollection.git


#### Using virtual environment
3. Setup virtual environment

        $ pip install virtualenv

4. Create a virtual environment

        $ virtualenv venv

5. Activate virtual environment
For Windows:

        $ venv\Scripts\activate

For Mac OS / Linux

        $ source venv/bin/activate

6. Install the project's dependancies

        $ pip install requirements.txt           

7. In config.py file, 
- replace {ENTER YOUR SECRET KEY} with a value.
- replace {YOUR MONGODB CONNECTION STRING} with the MongoDB Connection String gotten earlier. Remember to replace {password} in the MongoDB Connection String with the permission password you set while creating MongoDB Cluster.

8. Configure your flask path

        $ export FLASK_APP=run.py


9. Launch application

        $ flask run            

10. Head to http://127.0.0.1:5000

- This project has been developed on an Ubuntu 20.04LTS using Flask server (http://127.0.0.1:5000) and hosted on Heroku cloud (<a href="https://tissue-sample-collection.herokuapp.com">open app</a>) for remote access.

- Finally, this application works with a connection to a MongoDB database to allow a Tissue Sample directory to keep track of the number of samples with certain characteristics contained within a larger collection of samples.
