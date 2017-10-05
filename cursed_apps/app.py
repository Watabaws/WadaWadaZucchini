from flask import Flask, session, render_template, request, redirect
import os

app = Flask(__name__)

app.secret_key = os.urandom(32)


@app.route("/")
def logd_n_QM():
    try:
        if request.args["submit"] == "Logout":
          session["loggedIn"] = False
          session["username"] = ""
    except:
        pass
    try: 
        if session["username"] != "wada":
            return render_template("loginpage.html")
        else:
            return render_template("ushallpass.html", username = "wada")
    except:
        session["loggedIn"] = False
        return render_template("loginpage.html")

@app.route("/ushallpass")
def shall_pas(): 
        if "username" in session:
            if session["username"] == "":
                return render_template("loginpage.html")
        username = request.args["user"].lower()
        password = request.args["passo"]
        if username == "wada":
            if password == "Zucchini":
                session["username"] = "wada"
                session["loggedIn"] = True
                return render_template("ushallpass.html", username = "wada")
            else:
                return render_template("errorpage.html", bad = "password")
        else:
            return render_template("errorpage.html", bad = "username")
if __name__ == "__main__":
    app.debug = True
    app.run()
