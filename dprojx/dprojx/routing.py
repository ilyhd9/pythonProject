from channels import route

# Display all messages received
def message_handler(message):
    print(message['text'])


channel_routing = [
    route("websocket.receive", message_handler) 
]
