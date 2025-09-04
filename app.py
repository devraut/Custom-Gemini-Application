import os
from app import app   # Import the app instance directly

if __name__ == "__main__":
    print("Current working directory:", os.getcwd())
    print("Flask app running on http://127.0.0.1:5000/")
    app.run(host="127.0.0.1", port=5000, debug=True)
