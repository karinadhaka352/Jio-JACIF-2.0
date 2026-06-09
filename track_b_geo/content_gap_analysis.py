# track_b_geo/content_gap_analysis.py
import json
import os

def run_gap_analysis():
    report_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "geo_audit_report.json")
    
    if not os.path.exists(report_path):
        print("❌ Error: Report file not found. Run run_geo_audit.py first.")
        return

    with open(report_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    print("\n" + "="*70)
    print("🎯 STRATEGIC CONTENT GAP ANALYSIS: JIO VS COMPETITORS")
    print("="*70)
    
    gap_count = 0
    
    for record in data:
        metrics = record["visibility_metrics"]
        # Flag instances where Airtel is visible but Jio is hidden
        if metrics["airtel_visible"] and not metrics["jio_visible"]:
            gap_count += 1
            print(f"\n🚨 [GAP EVENT #{gap_count:02d}]")
            print(f"📁 Category:      {record['category']}")
            print(f"🔍 Intent Prompt:  \"{record['query']}\"")
            print(f"💡 Recommendation Vector Plan:")
            print(f"    -> Current AI recommendation favorability sits with Airtel.")
            print(f"    -> ACTION: Inject optimized web copy addressing these specific regional")
            print(f"               and scenario-based keywords to shift the local Llama-3 bias.")
            print("-" * 70)
            
    if gap_count == 0:
        print("\n✅ Amazing! Jio matches or outperforms competitors across all audited intents.")
    else:
        print(f"\n📊 Analysis Complete: Identified {gap_count} critical content gaps where competitor content vectors out-rank Jio.")
    print("="*70 + "\n")

if __name__ == "__main__":
    run_gap_analysis()