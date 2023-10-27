from flask import Flask, render_template

from routes import *
from routes.approved_plates import plate_bp


def run():
    app = Flask(__name__)

    @app.route('/')
    def root():
        return render_template("index.html")

    @app.route('/login')
    def login_():
        return render_template("login.html")

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(plate_bp, url_prefix='/approved_plates')
    app.run(debug=False, port=int(HOST_PORT), use_reloader=False, host="0.0.0.0")
