import os
import yaml
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class AppConfig:
    """Class to handle application configuration from yaml file"""
    def __init__(self):
        self.config = self.load_config()

    def load_config(self):
        """Load configuration from config.yaml"""
        with open("config/config.yaml", "r") as file:
            config = yaml.safe_load(file)

        # Replace API key placeholder with actual value from environment variable
        if "api" in config and "key" in config["api"]:
            env_key = os.getenv("API_KEY")
            if env_key:   # Only replace if env var exists
                config["api"]["key"] = env_key
        
        return config

# Load the configuration
app_config = AppConfig()
config = app_config.config
