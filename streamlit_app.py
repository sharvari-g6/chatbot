import streamlit as st
import requests

st.title("Flask + Streamlit Chatbot")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    st.write(f"{msg['role']}: {msg['content']}")

# User input
user_input = st.text_input("You:", "")

if st.button("Send"):
    if user_input:
        # Send request to Flask backend
        response = requests.post("http://127.0.0.1:5000/chat", json={"message": user_input})

        if response.status_code == 200:
            bot_response = response.json().get("response")

            # Update chat history
            st.session_state.messages.append({"role": "You", "content": user_input})
            st.session_state.messages.append({"role": "Bot", "content": bot_response})
            
            st.rerun()  # Refresh the UI
        else:
            st.error("Error: Could not connect to chatbot.")