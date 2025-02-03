from flask import Flask

app=Flask(__name__)

@app.route("/")
def welcome():
    return "<h1>Welcome</h1>"

@app.route('/success/<int:score>') #--> we can only pass the string value in this if we pass int then we have to typecast int into string

def success(score):
    return "the marks is" + str(score)

if __name__=="__main__":
    app.run(debug=True)
