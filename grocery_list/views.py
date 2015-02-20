""" Application Views """

from flask import render_template, redirect, url_for, request
from flask.ext.login import current_user, login_user, flash
from werkzeug.security import check_password_hash

from . import app
from .database import session
from .models import *

@app.route("/")
def index():
    """ App entry routing
    Login or go to page with data
    """

    # If no user, redirect to login
    if current_user.is_anonymous() == True:
        return redirect(url_for("login"))
    
    user_id = current_user.get_id()
    # Redirect to Lists if exist
    if session.query(List).filter("user_id" == user_id).first() is not None:
        return redirect(url_for("/lists"))
    # Redirect to Routes if exist
    elif session.query(Route).filter("user_id" == user_id).first() is not None:
        return redirect(url_for("/routes"))
    # Else redirect to Stores
    else:
        return redirect(url_for("/stores"))


@app.route("/login", methods=["GET", "POST"])
def login():
    """ Returns: Login page """

    if request.method == "POST":
        #HTML form entry
        email = request.form["email"]
        password = request.form["password"]
        # Return user
        user = session.query(User).filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            # Successful login
            login_user(user)
            flash("Logged in successfully.")
            return redirect(request.args.get("next") or url_for("index"))
        else:
            # Unsuccessful login
            flash("Incorrect username or password", "danger")
            return redirect(url_for("login"))

    # GET request
    return render_template("login.html")
