import markdown
import os
import shelve

# Import the framework
from flask import Flask, g
from flask_restful import Resource, Api, reqparse

# Create an instance of Flask
app = Flask(__name__)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = shelve.open('devices.db')
    return db

@app.teardown_appcontext
def teardown_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/')
def index():
    """ Present some document"""
    # Open the README file
    with open(os.path.dirname(app.root_path) + '/README.md', 'r') as markdown_file:
        
        # Read the content of the file
        content = markdown_file.read()

        # Convert to HTML
        return markdown.markdown(content)

class DeviceList():
    def get(self):
        shelf = get_db()
        keys = list(shelf.keys())

        devices = []

        for key in keys:
            devices.append(shelf[key])

        return {'message' : 'Success', 'data' : devices}, 200


api.add_resource(DeviceList, '/devices')
# api.add_resource(Device, '/device/<string:identifier>')
         