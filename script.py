import openai
import os
import json
from utils import *
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())



openai.api_key = os.getenv('OPENAI_API_KEY')
moderation_endpoint = os.getenv('moderation_endpoint')
content_directory = os.getenv('content_path')
SYSTEM_MESSAGE = os.getenv('SYSTEM_MESSAGE')




def main():
    """
    Main function to interact with the chatbot, manage conversation, and save/load conversations.

    Returns:
        None
    """

    print("Chatbot: Welcome to your Chatbot. Do you want to load a conversation? Answer with a \'yes' or \'no'") # Check if the user wants to load a conversation
    while True :

        user_input = input("You: ")

        if user_input.lower() == 'yes':
            context = recover_conversation(content_directory)
            break
        
        elif user_input.lower() == 'no' :
            context = json.loads(SYSTEM_MESSAGE)
            print('Chatbot: Ok! How can I assist you today?')
            break
        
        else :
            print('Chatbot: You shloud answer with a \'yes\' or \'no\'')

    conversation_loop(context, content_directory)

    return

main()


    





