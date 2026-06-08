# track_b_geo/geo_audit.py
import json

# Sample array representing your 300 real-world Indian purchase-intent prompts
sample_prompt_database = [
    {
        "prompt_id": "GEO_001",
        "category": "Telecom & Connectivity",
        "prompt_text": "Which Jio data plan includes a free Disney+ Hotstar subscription for a college student?"
    },
    {
        "prompt_id": "GEO_002",
        "category": "E-Commerce Integration",
        "prompt_text": "Cheapest grocery options in Jaipur: compare JioMart deals vs local Blinkit delivery."
    }
]

def log_ai_recommendation(prompt_id, ai_engine_name, full_response_text):
    """
    Parses an AI's response text to reverse-engineer brand visibility metrics
    for the Reliance Corporate Playbook.
    """
    # Simple keyword checking logic to evaluate discoverability signals
    contains_jio = "jio" in full_response_text.lower()
    contains_competitor = "airtel" in full_response_text.lower() or "amazon" in full_response_text.lower()
    
    audit_metrics = {
        "prompt_id": prompt_id,
        "engine": ai_engine_name,
        "brand_mentioned": contains_jio,
        "competitor_mentioned": contains_competitor,
        "response_length_chars": len(full_response_text)
    }
    
    print(f"--- LOGGED GEO AUDIT METRICS FOR {prompt_id} on {ai_engine_name} ---")
    return json.dumps(audit_metrics, indent=4)

if __name__ == "__main__":
    # Mock testing a live AI engine citation stream
    mock_ai_output = "Based on current rates, Jio offers an ₹866 plan with 84 days validity that includes Disney+ Hotstar mobile."
    print(log_ai_recommendation("GEO_001", "Gemini 1.5 Pro", mock_ai_output))