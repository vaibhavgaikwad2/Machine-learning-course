from flask import Flask

app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html><h1>Welcome</h1></html>"










if __name__=="__main__":
    app.run(debug=True)