# track_b_geo/run_geo_audit.py
import subprocess
import json
import re
import os
from prompts_dataset import geo_audit_prompts

def clean_terminal_artifacts(raw_text):
    """Scribes away messy ANSI terminal codes from the output stream."""
    clean_step = re.sub(r'\x1b\[\d*[ADGK]', '', raw_text)
    return re.sub(r'\[\d*[ADGK]', '', clean_step).strip()

def execute_local_audit():
    print("🛰️ STARTING AUTOMATED GEO BRAND VISIBILITY AUDIT RUN...")
    print(f"Loaded {len(geo_audit_prompts)} target purchase-intent queries.\n")
    
    audit_results = []
    
    for item in geo_audit_prompts:
        p_id = item["prompt_id"]
        query = item["prompt_text"]
        category = item["category"]
        
        print(f"👉 Processing [{p_id}] ({category}) ...")
        
        try:
            # Feed the query directly to your background local Llama-3 processor
            process = subprocess.run(
                ['ollama', 'run', 'llama3', query],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                encoding='utf-8'
            )
            
            if process.returncode == 0:
                raw_output = process.stdout
                ai_response = clean_terminal_artifacts(raw_output)
                
                # --- VISIBILITY SCORING ENGINE ---
                # Check for brand mentions (case-insensitive)
                mention_jio = "jio" in ai_response.lower()
                mention_airtel = "airtel" in ai_response.lower()
                mention_vi = " vi " in ai_response.lower() or "vodafone" in ai_response.lower()
                
                # Log metrics dictionary
                record = {
                    "prompt_id": p_id,
                    "category": category,
                    "query": query,
                    "ai_recommendation": ai_response[:150] + "...", # Store a snapshot
                    "visibility_metrics": {
                        "jio_visible": mention_jio,
                        "airtel_visible": mention_airtel,
                        "vi_visible": mention_vi
                    }
                }
                audit_results.append(record)
            else:
                print(f"❌ Error on {p_id}: {process.stderr.strip()}")
                
        except Exception as e:
            print(f"❌ System failure on {p_id}: {e}")
            
    # Save the audit matrix cleanly into a JSON file for your final data analysis
    output_path = os.path.join(os.path.dirname(__file__), "geo_audit_report.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(audit_results, f, indent=4)
        
    print("\n✅ GEO AUDIT COMPLETE!")
    print(f"Metrics report successfully generated and saved to: {output_path}")

if __name__ == "__main__":
    execute_local_audit()
    