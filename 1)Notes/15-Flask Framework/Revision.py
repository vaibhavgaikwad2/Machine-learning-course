from flask import Flask
from flask import render_template, request, redirect, url_for


app=Flask(__name__)


@app.route("/",methods=["GET"])
def welcome():
    return "Hello"

@app.route("/index/<score>")
def index(score):
    return "<h1>Your marks is :</h1>"+ score

@app.route("/main/<int:marks>")
def main(marks):
    if marks<35:
        return "Your failed, you required to pass" + str(35-marks)
    else:
        return "your passed the exam"


@app.route("/Success")
def Success():
    return "Passed! You Got "

@app.route("/Failed")
def fail():
    return "FAiled! You Got "


@app.route("/form",methods=["GET","POST"])
def form():
    if request.method=="GET":
        return render_template('getresult.html')
    else:
        maths=float(request.form['maths'])
        science=float(request.form['science'])
        c = float(request.form['c'])
        datascience=float(request.form['datascience'])

        avg_marks=(maths+science+c+datascience)/3

        res=""
        if avg_marks<35:
            res="fail"

        else:
            res="Success"

        return redirect(url_for(res))
        




        #return render_template('getresult.html',score=avg_marks)

if __name__=="__main__":
    app.run(debug=True)
