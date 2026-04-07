from flask import Flask , request, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("post.html")

@app.route("/result" , methods = ["POST"])
def result():

    username = request.form.get("username")
    password = request.form.get("password")

    if username == "admin" and password == "1234":
        return "<h2> Successfuly Login </h2>"
 
    else:
        return f"<h2>{username} and {password} are not matching</h2>"
        return "<h2> Invalid Credentials </h2>"

app.run(debug=True)
        

    

    


