import React, { useState } from "react";
import "./chat.css";

export const Chat = () => {
    const [messages, setMessages] = useState([]);
    const [input, setInput] = useState("");

    const handleSend = () => {
        if (!input.trim()) return;

        const userMessage = {
            role: "user",
            text: input,
        };

        const botMessage = {
            role: "bot",
            text: "This is a sample chatbot reply.",
        };

        setMessages([...messages, userMessage, botMessage]);
        setInput("");
    };
    const handleKeyDown = (e) => {
        if (e.key === "Enter") {
            handleSend();
        }
    };

    return (
        <div className="chat-page-container">
            {/* Nav-bar */}
            <div className="navbar">
                <div className="nav-text">Nep-Learn</div>
            </div>

            {/* chat-body */}
            <div className="chat-wrapper">
                <div className="chat-messages">
                    {messages.length === 0 && (
                        <div className="chat-placeholder">
                            Start a conversation with Nep-Learn
                        </div>
                    )}

                    {messages.map((msg, index) => (
                        <div
                            key={index}
                            className={`chat-message ${msg.role}`}
                        >
                            {msg.text}
                        </div>
                    ))}
                </div>

                {/* input-area */}
                <div className="chat-input-area">
                    <input
                        type="text"
                        placeholder="Type your message..."
                        value={input}
                        onChange={(e) => setInput(e.target.value)}
                        onKeyDown={handleKeyDown}
                    />
                    <button onClick={handleSend}>Send</button>
                </div>
            </div>
        </div>
    );
};
