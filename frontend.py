import streamlit as st
import requests

# 1. Set up the web page title
st.title("HR AI Agent Chatbot")
st.write("Ask about office policies or search for employee details.")

# 2. Define your FastAPI backend URL and a simple session tracker key
BACKEND_URL = "http://127.0.0.1:8000/agent/chat"
SESSION_ID = "fresher_test_123"

# 3. Create a box for the user to type their question
user_question = st.text_input("Type your question here:")

# 4. Create a button to submit the question
if st.button("Ask Agent"):
    
    # Check if the user actually typed something
    if user_question:
        
        # Display what the user typed on the screen
        st.info(f"You asked: {user_question}")
        
        # Package the data into a standard Python dictionary payload
        payload = {
            "session_id": SESSION_ID,
            "message": user_question
        }
        
        try:
            # Send the request over to your running FastAPI backend server
            response = requests.post(BACKEND_URL, json=payload)
            data = response.json()
            
            # Extract the response string and show it as a success bubble
            ai_answer = data["response"]
            st.success(f"Agent Reply: {ai_answer}")
            
        except Exception as e:
            # Display a clean error message if FastAPI is not running
            st.error("Error: Cannot connect to the FastAPI backend server. Make sure uvicorn is running!")
