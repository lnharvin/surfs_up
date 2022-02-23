# import the Flask dependency
from flask import Flask

# create new Flask instance
app = Flask(__name__)

# create Flask route
@app.route('/')
def hello_world():
    return 'Hello world'