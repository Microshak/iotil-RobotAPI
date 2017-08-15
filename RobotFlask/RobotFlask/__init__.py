"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)
app.config["mongouri"] = "mongodb://sawyer-mongo:xJENhr8tU9SnRzvn5DVXutJWDsaXBAm6urVHUT6zNirq2ycKx0BQwDbCz6lUqsyYrXc1ENnDIFb3YMTtlE6m5g==@sawyer-mongo.documents.azure.com:10255/?ssl=true"
import RobotFlask.views
import RobotFlask.mongo
