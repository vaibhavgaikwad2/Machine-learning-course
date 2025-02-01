from flask import Flask, render_template # --> it is used to redirect to html page



app=Flask(__name__)

@app.route("/")

def welcome():
    return "<html><h1>Hello, Everyone</h1></html>"


@app.route("/index")
def index():
    return render_template('index.html') # --> create a html file in templates folder

@ app.route("/about")

def about():
    return render_template('about.html')


if __name__=="__main__":
    app.run(debug=True)