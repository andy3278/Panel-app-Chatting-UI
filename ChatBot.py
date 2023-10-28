import panel as pn
from panel.chat import ChatInterface
import requests
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
HF_API_KEY = os.environ.get("HF_API_KEY")

API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
headers = {"Authorization": f"Bearer {HF_API_KEY}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload, stream=True)
	return response.json()


async def callback(contents: str, user: str, instance: pn.chat.ChatInterface):
    output = query({
        "inputs": contents,
    })
    message = ""
    for chunk in output['generated_text']:
        message += chunk
        yield message


chat_interface = pn.chat.ChatInterface(callback=callback, callback_user="bot", avatar="👦")
chat_interface.send(
    "This is a blenderbot-400M-distill powered ChatBot with Panel 1.3 ChatInterface!", user="System", respond=False
)
chat_interface.servable()



# def query(payload):
# 	response = requests.post(API_URL, headers=headers, json=payload)
# 	return response.json()
	
# output = query({
# 	"inputs": {
# 		"text": "what is your name?"
# 	},
# })
# print(output)