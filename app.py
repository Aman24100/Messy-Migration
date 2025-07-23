# app.py
from flask import Flask
from config import Config
from routes.users import bp as users_bp
from routes.auth import bp as auth_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(users_bp)
    app.register_blueprint(auth_bp)

    @app.route("/")
    def home():
        return "User Management System", 200

    return app

if __name__ == "__main__":
    create_app().run(host="0.0.0.0", port=5009, debug=True)
