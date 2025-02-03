from flask import Flask , render_template

app=Flask(__name__)

@app.route("/")
def welcome():
    return "<h1>Welcome</h1>"

@app.route('/success/<int:score>') #--> we can only pass the string value in this if we pass int then we have to typecast int into string

def success(score):
    res=''
    if score>=35:
        res='pass'
    else:
        res='fail'
    
    return render_template('result.html',result=res)


        #we are going to use this res value in html file to show on app using jinja temp
        # {{}} exressions to print output in html
        # {%...%} used for conditions statements and loops
        # {#..#} this is for comments
        

if __name__=="__main__":
    app.run(debug=True)
