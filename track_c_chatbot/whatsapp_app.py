# track_c_chatbot/whatsapp_app.py
import streamlit as st
import datetime
import subprocess
import sys
import os
import re
import json

# PATH FIXER: Tells Streamlit to look at the main root folder for module imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from track_a_twins.personas import personas_database, get_system_prompt
from track_c_chatbot.experiment_conditions import get_experimental_modifier

# Page configurations
st.set_page_config(page_title="Jio Conversational & Analytics Sandbox", page_icon="📊", layout="wide")

st.title("🚀 Jio Customer Experience & GEO Audit Intelligence Hub")
st.caption("Integrated Portal — Phase 2 Sandbox System")

# --- MULTI-TAB NAVIGATION ENGINE ---
tab1, tab2 = st.tabs(["💬 Consumer Twin WhatsApp Sandbox", "📊 GEO Brand Share Analytics"])

# ==========================================
# TAB 1: WHATSAPP SIMULATION SANDBOX
# ==========================================
with tab1:
    st.subheader("Interactive Persona Simulator")
    
    col1, col2 = st.columns([1, 3])
    
    with col1:
        st.markdown("### ⚙️ Simulation Settings")
        selected_persona = st.selectbox(
            "Select Customer Persona Twin:",
            options=list(personas_database.keys()),
            key="persona_select"
        )

        # NEW: 3-Arm Empirical Experiment Stimulus Selector Block
        st.markdown("### 🧪 Research Variables")
        selected_condition = st.selectbox(
            "Active Experimental Arm:",
            options=[
                "Condition A: Transactional AI",
                "Condition B: Emotional Mirroring Only",
                "Condition C: Emotional AI + DPDP Disclosure"
            ],
            key="condition_select"
        )

        p_info = personas_database[selected_persona]
        st.info(f"""
        **Profile Summary:**
        - **Age/Location:** {p_info['demographics']['age']} | {p_info['demographics']['location']}
        - **Income Tier:** {p_info['demographics']['income_tier']}
        - **Language Style:** *{p_info['behavioral_constraints']['primary_language']}*
        """)
        
        # Display helper notification tracking current active experimental stimulus
        if "Condition A" in selected_condition:
            st.warning("🤖 Robotic Control Mode Active")
        elif "Condition B" in selected_condition:
            st.error("🎭 Hidden Emotion Mode Active")
        elif "Condition C" in selected_condition:
            st.success("⚖️ DPDP Compliant Mode Active")

        if st.button("Clear Chat History"):
            st.session_state.messages = []
            st.rerun()

    # Handle automatic session resets on parameter updates
    if "current_twin" not in st.session_state:
        st.session_state.current_twin = selected_persona
    if "current_condition" not in st.session_state:
        st.session_state.current_condition = selected_condition

    if st.session_state.current_twin != selected_persona or st.session_state.current_condition != selected_condition:
        st.session_state.messages = []
        st.session_state.current_twin = selected_persona
        st.session_state.current_condition = selected_condition
        st.rerun()

    with col2:
        if "messages" not in st.session_state:
            st.session_state.messages = [
                {"role": "assistant", "timestamp": "12:30 PM", "content": f"Namaste! Welcome to Jio Services. You are now testing live interactions with {selected_persona}'s synthetic twin avatar under {selected_condition} constraints."}
            ]

        # Display history arrays
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.write(msg["content"])
                st.caption(f"Sent at {msg['timestamp']}")

        # Execution Loops
        if user_query := st.chat_input("Type your marketing pitch or message here...", key="chat_input_unique"):
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            st.session_state.messages.append({"role": "user", "timestamp": current_time, "content": user_query})
            st.rerun()

# Processing incoming dynamic conversational frames with injected stimuli modifiers
if len(st.session_state.get("messages", [])) > 0 and st.session_state.messages[-1]["role"] == "user":
    last_msg = st.session_state.messages[-1]["content"]
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    
    # 1. Gather original base persona rules
    base_system_rules = get_system_prompt(st.session_state.current_twin)
    
    # 2. Gather active 3-arm experimental condition modifier constraints
    condition_modifier = get_experimental_modifier(st.session_state.current_condition, st.session_state.current_twin)
    
    # 3. Combine both layers cleanly into the model execution context
    complete_system_rules = f"{base_system_rules}\n{condition_modifier}"
    
    conversation_history = f"System Rules:\n{complete_system_rules}\n\nHere is the ongoing conversation history:\n"
    for msg in st.session_state.messages[:-1]:
        role_label = "Customer" if msg["role"] == "user" else "AI Assistant"
        conversation_history += f"{role_label}: {msg['content']}\n"
    conversation_history += f"Customer: {last_msg}\n\nGenerate the next response matching constraints precisely."
    
    with tab1:
        with col2:
            with st.chat_message("assistant"):
                with st.spinner(f"{st.session_state.current_twin} is responding..."):
                    try:
                        process = subprocess.run(
                            ['ollama', 'run', 'llama3', conversation_history],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding='utf-8'
                        )
                        if process.returncode == 0:
                            clean_step1 = re.sub(r'\x1b\[\d*[ADGK]', '', process.stdout.strip())
                            ai_response = re.sub(r'\[\d*[ADGK]', '', clean_step1)
                        else:
                            ai_response = f"❌ Process error: {process.stderr.strip()}"
                    except Exception as e:
                        ai_response = f"❌ Execution failure: {e}"
                        
                st.write(ai_response)
                st.caption(f"Sent at {current_time}")
                st.session_state.messages.append({"role": "assistant", "timestamp": current_time, "content": ai_response})
                st.rerun()

# ==========================================
# TAB 2: GEO BRAND SHARE ANALYTICS
# ==========================================
with tab2:
    st.subheader("📈 Search Optimization Visibility Matrix")
    
    report_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "track_b_geo", "geo_audit_report.json")
    
    if not os.path.exists(report_path):
        st.warning("⚠️ No GEO Audit report matrix file found. Please execute your run_geo_audit.py background script first.")
    else:
        with open(report_path, "r", encoding="utf-8") as f:
            audit_data = json.load(f)
            
        total_runs = len(audit_data)
        jio_wins = sum(1 for r in audit_data if r["visibility_metrics"]["jio_visible"])
        airtel_wins = sum(1 for r in audit_data if r["visibility_metrics"]["airtel_visible"])
        vi_wins = sum(1 for r in audit_data if r["visibility_metrics"]["vi_visible"])
        
        m_col1, m_col2, m_col3, m_col4 = st.columns(4)
        m_col1.metric("Total Intents Audited", f"{total_runs} Queries")
        m_col2.metric("Jio Recommendation Share