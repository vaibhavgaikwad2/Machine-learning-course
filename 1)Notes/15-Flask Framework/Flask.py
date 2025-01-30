# Basic skeleton of flask app
from flask import Flask


# Initialzing the flask 
app=Flask(__name__)  #--> It creates an instance of the flask class, which will be your WSGI (web server Gateway interface) application

@app.route("/")  #--> it is a decorator

def welcome():
     return "welcome this flask app "


if __name__=="__main__":  #--> entry point fo an flask application --> from this execution will start.
     app.run() #--> used to run the flask app

