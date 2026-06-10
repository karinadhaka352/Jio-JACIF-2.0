# track_b_geo/run_geo_audit.py
import json
import os
import subprocess
import sys

# Ensure python can locate files within the same directory level
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Corrected variable name import matching prompts_dataset.py
from prompts_dataset import prompts_dataset

def execute_local_audit():
    print("🚀 Starting Local GEO Share of Voice Audit Engine...")
    print(f"📋 Loaded {len(prompts_dataset)} purchase-intent queries from dataset.")
    
    audit_results = []
    
    for item in prompts_dataset:
        p_id = item["prompt_id"]
        category = item["category"]
        query = item["query"]
        
        print(f"👉 Processing [{p_id}] ({category}) ...")
        
        # Structure the target execution message for our local Llama-3 model
        execution_prompt = (
            f"You are evaluating commercial recommendations in India. "
            f"Answer the following user query directly and recommend the best brand choice: {query}"
        )
        
        try:
            # Execute local shell process calls to interact with Llama-3
            process = subprocess.run(
                ['ollama', 'run', 'llama3', execution_prompt],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding='utf-8'
            )
            
            if process.returncode == 0:
                ai_response = process.stdout.strip()
                
                # --- VISIBILITY SCORING ENGINE ---
                # Check for brand mentions case-insensitively
                mention_jio = "jio" in ai_response.lower()
                mention_airtel = "airtel" in ai_response.lower()
                mention_vi = " vi " in ai_response.lower() or "vodafone" in ai_response.lower()
                
                # Log metrics dictionary structure
                record = {
                    "prompt_id": p_id,
                    "category": category,
                    "query": query,
                    "ai_recommendation": ai_response[:150] + "...", # Store an answer snapshot
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
    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "geo_audit_report.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(audit_results, f, indent=4)
        
    print("\n✅ GEO AUDIT COMPLETE!")
    print(f"Metrics report successfully generated and saved to: {output_path}")

if __name__ == "__main__":
    execute_local_audit()