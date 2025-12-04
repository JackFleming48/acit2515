from flask import Flask, render_template, redirect, url_for, Blueprint
from models.users import User
from db import db

users_bp = Blueprint("users", __name__)

@users_bp.route("/")
def users_display():

    stmt = db.select(User)

    users = db.session.execute(stmt).scalars().all()
    print(users)

    return render_template("users.html",
                           users=users)

@users_bp.route("/<int:id>")
def user_id(id):
    stmt = db.select(User).where(User.id == id)
    user = db.session.execute(stmt).scalars().first()

    if user is None:
        return "User not found", 404
    
    return render_template("user.html",
                           user=user)