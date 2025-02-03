# model.py
from message_handler import get_message  # Import from message_handler.py
from torchtext.data.utils import get_tokenizer

# Set up the string normalizer and ready to split by space
tokenizer = get_tokenizer("basic_english")

def response():
    message = get_message()  # Get the message
    print(f"Message: {message}")  # Ensure the message is what you expect
    tokens = tokenizer(message)  # Tokenize the message
    print(tokens)  # Process the tokens
    return tokens

