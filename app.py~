from flask import Flask, session, render_template, request, redirect
import os

app = Flask(__name__)

app.secret_key = os.urandom(32)


#session["loggedIn"] = False

@app.route("/")
def logd_n_QM():
    try: 
        if session["loggedIn"] == False:
            return render_template("loginpage.html")
        else:
            return render_template("ushallpass.html")
    except:
        session["loggedIn"] = False
        return render_template("loginpage.html")

@app.route("/ushallpass")
def shall_pas(): 
    if request.args["user"].lower() == "wada" and request.args["passo"] == "Zucchini":   
        session["loggedIn"] = True
        return render_template("ushallpass.html")
    else:
        return render_template("errorpage.html")
    
if __name__ == "__main__":
    app.debug = True
    app.run()
