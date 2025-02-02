import React, { useState } from "react";
import axios from "axios";
import './App.css';
import miniRobot from './png/Mini-Robot.png';
import humanoid from './png/humanoid.png';

function App() {
  const [message, setMessage] = useState("");  // To hold the current message being typed
  const [messages, setMessages] = useState([]); // To store the chat history as an array

  const handleKeyPress = (event) => {
    if (event.key === "Enter" && !event.shiftKey) {
      event.preventDefault(); // Prevents new line in textarea
      sendMessage();
      setMessage(""); // Clear the input field after sending
    }
  };

  const sendMessage = async () => {
    if (message.trim() !== "") {
      setMessages((prevMessages) => {
        const updatedMessages = [...prevMessages, { text: message, type: "user" }];
        if (updatedMessages.length > 6) updatedMessages.shift();
        return updatedMessages;
      });
  
      try {
        const response = await axios.post('http://localhost:5000/api/message', {
          message: message
        });
  
        if (response.status === 200) {
          console.log('Message sent successfully:', response.data);
  
          setMessages((prevMessages) => {
            const updatedMessages = [
              ...prevMessages, 
              { text: response.data.response, type: "bot" }
            ];
            if (updatedMessages.length > 6) updatedMessages.shift();
            return updatedMessages;
          });
        } else {
          console.error('Failed to send message:', response.data);
        }
      } catch (error) {
        console.error('Error sending message:', error);
      }
    }
  };
  
  
  

  return (
    <div className="app-container">
      <img src={humanoid} alt="Human figure" />
      {/* Chat Message Container that holds chat messages and input field */}
      <div className="chat-message-container">
        <div className="chat-container">
          {/* Display all sent messages from the messages array */}
          {messages.map((msg, index) => (
            <div key={index} className={msg.type === "user" ? "user-message" : "bot-message"}>
              {msg.text}
            </div>
          ))}
        </div>

        <div className="message-container">
          <textarea
            className="chat-input"
            placeholder="Type a message..."
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            onKeyDown={handleKeyPress} // Handles Enter key
          ></textarea>
          <button onClick={sendMessage} className="send-button">
            Send
          </button>
        </div>
      </div>
      <img src={miniRobot} alt="Mini Robot" />
    </div>
  );
}

export default App;
