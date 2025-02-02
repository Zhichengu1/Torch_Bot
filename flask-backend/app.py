from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS to allow frontend requests

@app.route("/")
def home():
    return "Flask backend is running!"

@app.route("/api/message", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")
    
    # Log the incoming message
    print(f"Received message: {user_message}")

    # You can also check the status of the request or any issues here
    if not user_message:
        print("No message received")
        return jsonify({"error": "No message received"}), 400  # Send a 400 error if no message is provided

    # Return a response back to the frontend
    response = {"response": f"Bot says: {user_message}"}
    print(f"Sending response: {response}")  # Log the response before sending it

    return jsonify(response)  # Send the response back

if __name__ == "__main__":
    app.run(debug=True)
