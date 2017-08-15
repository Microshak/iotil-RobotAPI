"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from flask import Flask
from RobotFlask import app

from bson.json_util import dumps
import pymongo

from pymongo import MongoClient

from RobotFlask.mongo import db

app.register_blueprint(db)

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        ti='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/api')
def api():
    uri = "mongodb://sawyer-mongo:xJENhr8tU9SnRzvn5DVXutJWDsaXBAm6urVHUT6zNirq2ycKx0BQwDbCz6lUqsyYrXc1ENnDIFb3YMTtlE6m5g==@sawyer-mongo.documents.azure.com:10255/?ssl=true"

    mongoclient = MongoClient(uri)
    
    dba = mongoclient.SawyerDB

    collection = dba.Command
    data = collection.find_one({"Name": "Demo"})
    return dumps(data)
