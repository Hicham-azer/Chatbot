import openai
import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())




openai.api_key = os.getenv('OPENAI_API_KEY')






def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
#     print(str(response.choices[0].message))
    return response.choices[0].message["content"]

def collect_messages(user_input):
    prompt = user_input
    context.append({'role':'user', 'content':f"{prompt}"})
    response = get_completion_from_messages(context) 
    context.append({'role':'assistant', 'content':f"{response}"})
    print(context)
    return response




context = []
while True:    
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    response = collect_messages(user_input)
    print("Chatbot:", response)
