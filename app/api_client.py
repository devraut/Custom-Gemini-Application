import os 
import google.generativeai as genai
from logger import CustomLogger

class GenAIClient:
    """Class to interact with gemini client"""

    def __init__(self):
        self.api_key=os.getenv('API_KEY') #Fetch the actual api from env file.
        genai.configure(api_key=self.api_key)
        self.model=genai.GenerativeModel(model_name="gemini-2.5-pro")
        self.chat = self.model.start_chat(history=[])
        self.logger=CustomLogger().get_logger()

    def get_response(self, message):
        """
        Send messages to the OpenAI API and return the response.
        
        :param messages: List of messages for the conversation.
        :return AI response as a string.
        """

        try:
            self.logger.info("Sending message to the OpenAI API...")
            response = self.chat.send_message(message)
            self.logger.info("Received response from Open AI")
            return response.text if response else "No response received."
        
        except Exception as e:
            self.logger.error(f'Error communicating with Gemini API: {e}')
            return "Sorry, I couldn't get a response at this time."
            

