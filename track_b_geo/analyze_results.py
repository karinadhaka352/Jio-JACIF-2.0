# track_b_geo/analyze_results.py
import json
import os

def calculate_share_of_voice():
    # Dynamic path mapping to find your report file
    report_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "geo_audit_report.json")
    
    if not os.path.exists(report_path):
        print(f"❌ Error: Could not find report file at {report_path}")
        return

    with open(report_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    total_queries = len(data)
    jio_count = 0
    airtel_count = 0
    vi_count = 0
    
    # Loop through the metrics to count brand wins
    for record in data:
        metrics = record["visibility_metrics"]
        if metrics["jio_visible"]: jio_count += 1
        if metrics["airtel_visible"]: airtel_count += 1
        if metrics["vi_visible"]: vi_count += 1

    # Calculate percentages
    jio_share = (jio_count / total_queries) * 100
    airtel_share = (airtel_count / total_queries) * 100
    vi_share = (vi_count / total_queries) * 100

    # Print out a beautifully formatted terminal results table
    print("\n" + "="*50)
    print("📊 GEO AUDIT: BRAND SHARE OF VOICE SUMMARY REPORT")
    print("="*50)
    print(f"Total Audit Queries Run: {total_queries}")
    print("-"*50)
    print(f" BRAND      | MENTIONS | RECOMENDATION SHARE (%)")
    print("-"*50)
    print(f" Reliance Jio| {jio_count:<8} | {jio_share:.1f}%")
    print(f" Airtel      | {airtel_count:<8} | {airtel_share:.1f}%")
    print(f" Vodafone Vi | {vi_count:<8} | {vi_share:.1f}%")
    print("="*50)
    print("💡 Project Insight: Use these baseline percentages to target")
    print("   content gap optimizations where Airtel out-ranks Jio.")
    print("="*50 + "\n")

if __name__ == "__main__":
    calculate_share_of_voice()