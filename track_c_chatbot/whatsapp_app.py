# track_c_chatbot/whatsapp_app.py
import streamlit as st
import datetime
import subprocess
import sys
import os
import re

# PATH FIXER: Tells Streamlit to look at the main root folder for module imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from track_a_twins.personas import personas_database, get_system_prompt

# Page configurations to match a clean mobile viewport layout
st.set_page_config(page_title="Jio Conversational Assistant Sandbox", page_icon="💬", layout="centered")

st.title("💬 Jio Customer Care — WhatsApp Sandbox")
st.caption("Phase 2 UI: Multi-Persona Behavioral Evaluation & Interaction Sandbox")

# --- SIDEBAR CONTROL PANEL ---
st.sidebar.header("⚙️ Simulation Settings")
selected_persona = st.sidebar.selectbox(
    "Select Customer Persona Twin:",
    options=list(personas_database.keys())
)

p_info = personas_database[selected_persona]
st.sidebar.markdown(f"""
**Selected Profile Summary:**
- **Age/Location:** {p_info['demographics']['age']} | {p_info['demographics']['location']}
- **Income Tier:** {p_info['demographics']['income_tier']}
- **Language Style:** *{p_info['behavioral_constraints']['primary_language']}*
""")

# If the user switches personas, clear the chat memory automatically to prevent crossover
if "current_twin" not in st.session_state:
    st.session_state.current_twin = selected_persona

if st.session_state.current_twin != selected_persona:
    st.session_state.messages = []
    st.session_state.current_twin = selected_persona
    st.rerun()

if st.sidebar.button("Clear Chat History"):
    st.session_state.messages = []
    st.rerun()

# --- CHAT BUFFER CORE ---
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "timestamp": "12:30 PM", "content": f"Namaste! Welcome to Jio Services. You are now testing live interactions with {selected_persona}'s synthetic twin avatar."}
    ]

# Render chat history logs on screen
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
        st.caption(f"Sent at {msg['timestamp']}")

# --- LIVE INTERACTION AND OFFLINE GENERATION LOOPS ---
if user_query := st.chat_input("Type your marketing pitch or message here..."):
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    
    # 1. Display user input string immediately
    st.session_state.messages.append({"role": "user", "timestamp": current_time, "content": user_query})
    with st.chat_message("user"):
        st.write(user_query)
        st.caption(f"Sent at {current_time}")
        
    # 2. Build out the FULL conversation history string to feed Llama-3's memory context
    system_rules = get_system_prompt(selected_persona)
    conversation_history = f"System Rules:\n{system_rules}\n\nHere is the ongoing conversation history:\n"
    
    for msg in st.session_state.messages:
        role_label = "Customer" if msg["role"] == "user" else "AI Simulation Assistant"
        conversation_history += f"{role_label}: {msg['content']}\n"
    
    conversation_history += "\nGenerate the next response matching your profile constraints precisely."
    
    # 3. Stream a placeholder while calling the offline system line
    with st.chat_message("assistant"):
        with st.spinner(f"Connecting to local Llama-3 core engine ({selected_persona} is tracking context...)..."):
            try:
                process = subprocess.run(
                    ['ollama', 'run', 'llama3', conversation_history],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    encoding='utf-8'
                )
                
                if process.returncode == 0:
                    raw_response = process.stdout.strip()
                    
                    # 🧹 Clean terminal artifacts
                    clean_step1 = re.sub(r'\x1b\[\d*[ADGK]', '', raw_response)
                    ai_response = re.sub(r'\[\d*[ADGK]', '', clean_step1)
                else:
                    ai_response = f"❌ Local process execution error: {process.stderr.strip()}"
                    
            except Exception as e:
                ai_response = f"❌ System execution failure: {e}"
                
        # 4. Render and commit response to session history arrays
        st.write(ai_response)
        st.caption(f"Sent at {current_time}")
        st.session_state.messages.append({"role": "assistant", "timestamp": current_time, "content": ai_response})