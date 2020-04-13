# Import the framework
from flask import Flask

# Create an instance of Flask
app = Flask(__name__)

@app.route('/')
def hello():
    