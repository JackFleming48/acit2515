from flask import Flask, render_template, redirect, url_for, request, flash

def create_app(config=None):
    app = Flask(__name__)

    from routes import home

    app.register_blueprint(home.blue_print)

    return app
