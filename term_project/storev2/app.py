from flask import Flask, render_template
from pathlib import Path
from db import db

def create_app():
    app = Flask(__name__)
    app.instance_path = Path(".").resolve()

    ROOT_DIR = Path(__file__).resolve().parent
    DB_PATH = ROOT_DIR / "data" / "database.db"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_PATH}"
    db.init_app(app)

    from routes import register_blueprints
    register_blueprints(app)

    @app.route("/")
    def home():
        return render_template("home.html")
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=8888)