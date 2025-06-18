from flask import Flask, redirect, url_for
from .config import Config, ConfigTesting
from .routes import main_routes as routes_bp
from dotenv import load_dotenv

def create_app(testing=False):
    load_dotenv()
    app = Flask(__name__)
    app.config.from_object(ConfigTesting if testing else Config)
    app.register_blueprint(routes_bp)

    @app.errorhandler(404)
    def manejar_404(error):
        return redirect(url_for('main_routes.indexLogin_get'))
    return app
