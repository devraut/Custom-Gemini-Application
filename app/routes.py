from flask import Blueprint, render_template, request, jsonify
from app.utils import format_response
from app.chat import ChatManager

# Create a blueprint for the main application
main = Blueprint('main', __name__)

# Initialize the ChatManager
chat_manager = ChatManager()

@main.route('/')
def index():
    """Render the chat interface"""
    return render_template('chat.html')  # Renders chat.html

@main.route('/test')
def test():
    """Render a test page (assuming base.html exists)"""
    return render_template('base.html')

@main.route('/api/chat', methods=['POST'])
def chat():
    """Handles chat messages from user."""
    data = request.get_json(silent=True) or {}
    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    try:
        # Get Gemini response via ChatManager
        ai_response = chat_manager.get_response(user_message)

        # Format Gemini response (Markdown → HTML)
        formatted_response = format_response(ai_response)

        return jsonify({"response": formatted_response})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
