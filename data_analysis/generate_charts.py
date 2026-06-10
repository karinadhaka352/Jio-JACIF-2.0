# data_analysis/generate_charts.py
import os
import pandas as pd
import matplotlib.pyplot as plt

def generate_experimental_charts():
    print("📊 Initializing JACIF 2.0 Graphics Engine...")
    
    # Locate dataset path
    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(current_dir, "experimental_log_matrix.csv")
    
    if not os.path.exists(csv_path):
        print(f"❌ Error: Cannot find {csv_path}")
        return
        
    # Read the data rows
    df = pd.read_csv(csv_path)
    
    # Group by Experimental Condition and calculate means
    metrics = ['TAM_Perceived_Usefulness', 'PRIV_Privacy_Calculus', 'EMO_Interface_Trust', 'DPDP_Awareness_Score']
    grouped = df.groupby('Experimental_Condition')[metrics].mean()
    
    # Configure the plot layout
    plt.figure(figsize=(10, 6))
    grouped.T.plot(kind='bar', figsize=(12, 7), width=0.8)
    
    plt.title('Jio Institute JACIF 2.0: Behavioral Construct Scores Across Multi-Arm Conditions', fontsize=14, fontweight='bold', pad=15)
    plt.ylabel('Observed Likert Mean Score (1-5 Scale)', fontsize=12)
    plt.xlabel('Evaluated Behavioral Constructs', fontsize=12)
    plt.xticks(rotation=15, ha='right')
    plt.ylim(0, 5.5)
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.legend(title='Experimental Configuration Arms', frameon=True, facecolor='white')
    plt.tight_layout()
    
    # Save chart to data_analysis directory
    output_image_path = os.path.join(current_dir, "empirical_metrics_chart.png")
    plt.savefig(output_image_path, dpi=300)
    print(f"✅ Success! Statistical chart saved beautifully at: {output_image_path}")

if __name__ == "__main__":
    generate_experimental_charts()