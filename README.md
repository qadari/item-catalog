# Item-Catalog 
This application provides a list of items within a variety of categories as well as provide a user registration(google) and authentication system. Registered users will have the ability to post, edit and delete their own items.It utilizes Flask, SQL Alchemy, JQUERY, CSS, Java Script, and OAUTH 2 to create an Item catalog website.

# Files Included
database_setup.py
data_setup.py
project.py
static folder
templates folder
json files

# Installation
Virtual Box
Vagrant
python 3.6.2
Flask

# setting up OAuth2.0
You will need to sign up for a google account and set up a client id and secret.
Visit: http://console.developers.google.com for google setup
You Can also signup for facebook account and set up the client id and secret.
Visit: https://developers.facebook.com/ for facebook setup

# Preparing the Enviornment.
clone this repo to '/vagrant/restaurant' folder.
Run 'python database_setup.py'
Run 'python data_setup.py'
Run 'python project.py'
Open your web browser and visit http://localhost:8000/
The applications main page will open and you will need to click on login and then use Google+ to login.