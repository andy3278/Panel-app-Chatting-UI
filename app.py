import panel as pn
from panel.chat import ChatInterface

pn.extension()

def echo(contents, user, instance):
    return contents

chat_interface = ChatInterface(
    callback=echo, 
    user="EchoBot",
    avatar="?",
    callback_user="Counter",)

chat_interface.servable()
