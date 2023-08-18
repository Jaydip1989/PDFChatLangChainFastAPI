import openai
from config import apikey

openai.api_key = apikey

def generate_description(input):
    messages = [
        {
            'role':'user',
            'content':""" As a Product Decscription Generator, Generate multi paragraph rich text description with emojis from the information provided to you' \n"""
        }
    ]
    messages.append({'role':'user', 'content': f"{input}"})
    completion = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages = messages
    )
    reply = completion.choices[0].message.content
    return reply
