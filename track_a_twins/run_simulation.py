# track_a_twins/run_simulation.py
import subprocess
import json
from personas import get_system_prompt

def interview_twin(persona_name, marketing_pitch):
    """
    Runs a direct system process to communicate with Ollama offline,
    completely bypassing Python's network and security layers.
    """
    print(f"\n🚀 INITIALIZING LOCAL AI TWIN SIMULATION: {persona_name.upper()}...")
    
    # Grab the system rules we wrote in personas.py
    system_instruction = get_system_prompt(persona_name)
    
    # Construct a clean text prompt for the local model
    full_prompt = f"System Rules:\n{system_instruction}\n\nUser Input:\n{marketing_pitch}"
    
    try:
        # Execute ollama directly as a local system app process
        process = subprocess.run(
            ['ollama', 'run', 'llama3', full_prompt],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding='utf-8'
        )
        
        if process.returncode == 0:
            print(f"\n💬 {persona_name}'s Simulated Response:")
            print("-" * 50)
            print(process.stdout.strip())
            print("-" * 50)
        else:
            print(f"\n❌ Local process error: {process.stderr.strip()}")
            
    except Exception as e:
        print(f"\n❌ System execution error: {e}")

if __name__ == "__main__":
    sample_pitch = (
        "Hey! Upgrade to the new Jio Premium Max plan for just ₹149/month extra! "
        "Get instant, ad-free access to every single Hollywood movie premium stream, "
        "exclusive international sports matches, and multi-screen ultra-HD sharing."
    )
    
    interview_twin("Amit", sample_pitch)