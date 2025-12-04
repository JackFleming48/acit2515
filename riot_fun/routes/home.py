from flask import (
    redirect, url_for, Blueprint,
    render_template, flash, abort
)

blue_print = Blueprint("home", __name__)

@blue_print.route("/")
def home():
    return render_template("home.html")