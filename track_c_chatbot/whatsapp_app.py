# track_c_chatbot/whatsapp_app.py
import streamlit as st
import datetime

# Page configuration to match a clean mobile viewport layout
st.set_page_config(page_title="Jio Conversational Assistant Mockup", page_icon="💬", layout="centered")

st.title("💬 Jio Customer Care — WhatsApp Sandbox")
st.caption("Testing Framework for Conversational Commerce and DPDP Compliance Sign-offs")

# Initialize mock session state variables for chat history log loops
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "timestamp": "12:30 PM", "content": "Namaste! Welcome to Jio Customer Care. How can I assist you with your Jio Services today?"}
    ]

# Display current chat history logs natively
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
        st.caption(f"Sent at {msg['timestamp']}")

# Accept live user interface input strings
if user_query := st.chat_input("Type your message here..."):
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    
    # Append user chat input to current screen instance state tracker
    st.session_state.messages.append({"role": "user", "timestamp": current_time, "content": user_query})
    with st.chat_message("user"):
        st.write(user_query)
        st.caption(f"Sent at {current_time}")
        
    # Standard echo response for Phase 2 UI behavioral evaluation
    mock_reply = f"System Echo: Received your message: '{user_query}'. Hooking into Track A Digital Twin configurations for persona response alignment testing..."
    st.session_state.messages.append({"role": "assistant", "timestamp": current_time, "content": mock_reply})
    with st.chat_message("assistant"):
        st.write(mock_reply)
        st.caption(f"Sent at {current_time}")
        