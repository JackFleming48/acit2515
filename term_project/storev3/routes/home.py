from flask import Flask, render_template, redirect, url_for, Blueprint


home_bp = Blueprint("home", __name__)

@home_bp.route("/")
def home_display():

    return render_template("home.html")