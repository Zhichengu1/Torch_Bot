# message_handler.py

user_message = ""

def set_message(message):
    global user_message
    user_message = message

def get_message():
    return user_message
