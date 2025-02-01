# Basic skeleton of flask app
from flask import Flask


# Initialzing the flask 
app=Flask(__name__)  #--> It creates an instance of the flask class, which will be your WSGI (web server Gateway interface) application

@app.route("/")  #--> it is a decorator

def welcome():
     return "welcome to this flask app, hello i am vaibhav gaikwad"



@app.route("/index")

def index():
     return "welcome to index page"


if __name__=="__main__":  #--> entry point fo an flask application --> from this execution will start.
     app.run(debug=True) #--> used to run the flask app
     
     # debug is used to update changes on real time in flask app u dont need to restart the app
      
