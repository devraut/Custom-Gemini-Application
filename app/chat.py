from app.api_client import GenAIClient

class ChatManager:
    """Class to manage chat interactions."""

    def __init__(self):
        self.client=GenAIClient()
        self.conversation_history=[]

    def add_message(self,role, content):
        """Add a message to the conversation history."""
        self.conversation_history.append({'role':role, 'content':content})

    def get_response(self,user_message):
        """
        Gets a concise or detailed response based on user input.
        
        :params user_message: The message input from the user.
        :return AI response as a string.
        """

        # Add user's message to the history
        self.add_message('user',user_message)

        #Prepare messages for the API call based on user intent
        if any(keyword in user_message.lower() for keyword in ["what is","define"]):
            prompt=f"Provide a concise definition of: {user_message}"

        elif 'explain' in user_message.lower() or 'code' in user_message.lower():
            prompt=f"Explain clearly with examples: {user_message}"

        else:
            prompt=f"Respond concisely to: {user_message}"

        #Get AI's response
        ai_response = self.client.get_response(prompt)

        # Add AI's response to the history
        self.add_message('assistant',ai_response)

        return ai_response  

