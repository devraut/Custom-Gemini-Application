from flask import Flask
import os
import yaml
from dotenv import load_dotenv
from logger import CustomLogger
from config import AppConfig
from .routes import main as main_blueprint

# Load environment variables
load_dotenv()

def create_app():
    """Create and configure the flask application"""
    app = Flask(__name__, template_folder="templates", static_folder="static")

    # Load configuration
    custom_app_config = AppConfig()
    app.config.update(custom_app_config.config)

    # Set up logging
    logger = CustomLogger().get_logger()
    logger.info("Flask application starting...")

    # Register routes
    app.register_blueprint(main_blueprint)

    return app

# ✅ Expose the app instance so gunicorn can find `app:app`
app = create_app()
