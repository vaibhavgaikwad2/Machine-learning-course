# GET --> sending a url and getting a content this is GET method
from flask import Flask, render_template, request

app=Flask(__name__)

@app.route("/",methods=['GET'])
def welcome():
    return "Welcome to the flask app"

app.route("/form",methods=['GET','POST'])
def form():
    if request.method=='POST':
        name=request.form['name']
        return f"hello {name}"
    return render_template('form.html')


if __name__=="__main__":
    app.run(debug=True)

