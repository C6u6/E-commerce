from flask import Flask, flash, redirect, render_template, request, session, g
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import date
from time import sleep 
from functools import wraps
from altentication import validusername, validnames, validpassword, validemail
from helpers import login_required, Database, manipulatingData

import sqlite3, string

# Configure the app
app = Flask(__name__)

# Autoreload the app always that a change is found on template
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

""" I am remainding you that you need to do all the control data here in the backend """

# Stablishing a database
path = "database/database.sql"
Database(path)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")
    

@app.route("/login", methods=["GET", "POST"])
def login():
    """ Log user in """

    # Forget any user_id
    session.clear()

    error = None

    if request.method == "POST":
        user = request.form.get("username-or-email")
        password = request.form.get("password")
        # Ensure username was submitted
        if not user:
            error = "Must provide a username or an email"
            return render_template("login.html", error=error)

        # Ensure password was submitted
        elif not password:
            error = "Must provide password"
            return render_template("login.html", error=error)

        # Ensure user is registered
        if "@" in user:
            result = manipulatingData("SELECT * FROM users WHERE email = ?", [user], True)
            if result == []:
                error = "Email does not exist"
                flash("Check if the user is correct or consider registering")
                return render_template("login.html", error=error)
        
        if "@" not in user:
            result = manipulatingData("SELECT * FROM users WHERE user_name = ?", [user], True)
            if result == []:
                error = "Username does not exist"
                flash("Check if the email is correct or consider registering")
                return render_template("login.html", error=error)
            
            # Ensure password matchs the database
            if not check_password_hash(result[0][5], password):
                error = "Password does not exist"
                flash("Check if the password is correct or consider registering")
                return render_template("login.html", error=error)

        # Everything went well: remember the user
        session["user_id"] = result[0][0]
        return redirect("/")

    return render_template("login.html", error=error)


@app.route("/logout")
def logout():
    """ Log user out """
    session.clear()

    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    error = None

    if request.method == "POST":
        """Register the user """
        name = request.form.get("name").capitalize()
        surname = request.form.get("surname")
        surname = string.capwords(surname)
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        checkbutton = request.form.get("checkbox")

        # Validation
        if checkbutton != "agree":
            error = "Check button not clicked"
            return render_template("register.html", error=error)
        if not (validnames(name, surname)):
            error = ('Problems with name or the surname')
            return render_template("register.html", error=error)
        if not (validusername(username)):
            error = "Invalid username"
            return render_template("register.html", error=error)
        if not (validemail(email)):
            error = ("Invalid email")
            return render_template("register.html", error=error)
        if not (validpassword(password, confirmation)):
            error = ("Could not register this password")
            return render_template("register.html", error=error)

        # Inserting the user into the database
        try:
            result = manipulatingData("SELECT * FROM users WHERE user_name = ?", [username], True)
            # If the username provided is on the database, return an error
            if result != []:
                error = "This username is already registered"
                return render_template("register.html", error=error)
            # No errors, so register the user
            manipulatingData(
                """INSERT INTO users (name_user, surname, user_name, email, pass_hash)
                VALUES 
                (?,?,?,?,?)""", [name, surname, username, email, generate_password_hash(password)])
            flash("You were registered")
            return redirect("/login")
        except Exception as e:
            error = e

    return render_template("register.html", error=error)

        
@app.route("/policy")
def policy():
    return render_template("policy.html")

@app.route("/tecnologies", methods=["GET","POST"])
def tec():
    """ Automatically search for and display properly any product that belongs to the tec category"""

    if request.method == 'GET':

        # All products that belongs to the tecnology categogy
        with sqlite3.connect("commerce.db") as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM product WHERE category = 'tecnology'")
            res = fetchall()

            if results == []:
                flash("Some unknown error")
                return redirect("/")

            # Final result
            results = res[0]

        return render_template("tecnologies.html",results=results)

# This will dispay the user information   
@app.route("/user", methods=["GET", "POST"])
@login_required
def user():
    """Retriving the user information"""
    result = manipulatingData("SELECT * FROM users WHERE id = ?", [session['user_id']], True)

    if request.method == "POST":
        # Take the data
        name = request.form.get("name")
        surname = request.form.get("surname")
        email = request.form.get("email")
        password = request.form.get("password")
        newpassword = request.form.get("newpassword")
        check = request.form.get("check")
        if check != "change":
            flash("You need to agree to change something")
            return redirect("/user")
        # Copy of password to usse it in the validation function
        copy = password

        toChange = []

        # Append valid data the data
        if (validnames(name, surname)):
            toChange.append(name, surname)
        if (validemail(email)):
            toChange.append(email)
        if (validpassword(password, copy)):
            toChange.append(password)

        # Change data
        id = session['user_id']
        try:
                # Checking the old password
                res = manipulatingData("SELECT pass_hash FROM users WHERE id = ?", [id], True)
                if password != None:
                    if not check_password_hash(res[0][0], password):
                        flash("You didn't provide your current password correctly")
                        return redirect("/user")

                for data in toChange:
                    if data == name:
                        manipulatingData("UPDATE users SET name_user = ? WHERE id = ?",[name, id])
                    if data == surname:
                        manipulatingData("UPDATE users SET surname = ? WHERE id = ?",[surname, id])
                    if data == email:
                        manipulatingData("UPDATE users SET email = ? WHERE id = ?",[email, id])
                    if data == password:
                        manipulatingData("UPDATE users SET pass_hash = ? WHERE id = ?",[generate_password_hash(newpassword), id])

                flash("Data updateded successfully")
        except Exception as e:
            flash(e)
            
    return render_template("user.html", result=result)


@app.route("/account")
@login_required
def account():
    return render_template("warningdemo.hml")


@app.route("/services", methods=["GET","POST"])
@login_required
def service():
    """ Add the user to the sellers table """
    if request.method == "POST":
        checked = request.form.get("checkbox")

        if checked == "agree":
            # Inserting into sellers the user id
            try:
                # Check if the user is already a seller
                res = manipulatingData("SELECT * FROM sellers WHERE seller_id = ?", [session["user_id"]], True)
                if res != []:
                    flash("You are already a seller")
                    return redirect("/products")

                manipulatingData("INSERT INTO sellers (seller_id) VALUES (?)", [session["user_id"]])
                flash("You were registered")
                return redirect("/products")
            except Exception as e:
                flash(e)

    return render_template("services.html")


@app.route("/products", methods=["GET","POST"])
@login_required
def product():
    if request.method == "POST":
        # Getting data
        title = request.form.get("title")
        desc = request.form.get("description")
        img = request.form.get("img")
        # Validating data
        if not title:
            flash("Must provide a title for the product")
            return redirect("/product")
        if not request.form.get("description"):
            flash("Must provide a description for the product")
            return redirect("/product")
        if not img:
            flash("Must provide one(some) photos for the product")
            return redirect("/product")

    return render_template("product.html")


@app.route("/activity")
@login_required
def activity():
    return render_template("warningdemo.html")
@app.route("/clients")
@login_required
def clients():
    return render_template("warningdemo.html")
@app.route("/ordered")
@login_required
def ordered():
    return render_template("warningdemo.html")
@app.route("/contact")
@login_required
def contact():
    return render_template("warningdemo.html")

@app.route("/clothes")
def clothes():
    return render_template("clothes.html")
    
if __name__ == "__main__":
 app.run()