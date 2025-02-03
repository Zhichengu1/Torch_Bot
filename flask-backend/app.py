from flask import Flask, request, jsonify
from flask_cors import CORS
from message_handler import set_message, get_message  # Import functions from message_handler
from model import response

app = Flask(__name__)
CORS(app)  # Enable CORS to allow frontend requests

# -------------------------------- api -------------------------
@app.route("/")
def home():
    return "Flask backend is running!"

@app.route("/api/message", methods=["POST"])
def chat():
    data = request.json
    set_message(data.get("message", ""))  # Set the message using the helper function
    
    # Log the incoming message
    user_message = get_message()  # Get the message from the helper function
    print(f"Received message: {user_message}")

    # You can also check the status of the request or any issues here
    if not user_message:
        print("No message received")
        return jsonify({"error": "No message received"}), 400  # Send a 400 error if no message is provided

    # Get the tokens from the response function
    tokens = response()  # Call the response function to get the tokens
    print(f"Sending tokens: {tokens}")  # Log the tokens before sending them
    
    # Rename the response variable to avoid conflict
    response_data = {"response": f"Bot says: {tokens}"}  # Pass the tokens in the response
    print(f"Sending response: {response_data}")  # Log the response before sending it

    return jsonify(response_data)  # Send the response back


if __name__ == "__main__":
    app.run(debug=True)
