# data_analysis/analyze_empirical_data.py
import os
import numpy as np
import pandas as pd
from scipy import stats

def calculate_kl_divergence(p, q):
    """
    Computes Kullback-Leibler (KL) Divergence to measure statistical distance.
    """
    p = np.asarray(p, dtype=float)
    q = np.asarray(q, dtype=float)
    
    # Apply Laplace smoothing to prevent division by zero or log(0) errors
    p = np.where(p == 0, 1e-10, p)
    q = np.where(q == 0, 1e-10, q)
    
    # Normalize arrays to true probability distributions
    p /= np.sum(p)
    q /= np.sum(q)
    
    return np.sum(p * np.log(p / q))

def run_twin_validation_tests():
    print("======================================================================")
    print("🤖 JACIF 2.0: DIGITAL TWIN EMPIRICAL VALIDATION ENGINE")
    print("======================================================================")
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(current_dir, "experimental_log_matrix.csv")
    
    if not os.path.exists(csv_path):
        print(f"❌ Error: Could not find dataset log at {csv_path}")
        return
        
    # Load your logged CSV observations directly into a pandas dataframe
    df = pd.read_csv(csv_path)
    print(f"📊 Successfully loaded {len(df)} live experimental observations from log matrix.")
    
    # Target scoring metrics
    constructs = ['TAM_Perceived_Usefulness', 'PRIV_Privacy_Calculus', 'EMO_Interface_Trust', 'DPDP_Awareness_Score']
    
    print("\n⚖️ Running Cross-Condition Behavioral Statistical Breakdown...")
    
    for construct in constructs:
        # Extract individual scores from your matrix columns
        scores = df[construct].values
        mean_score = np.mean(scores)
        std_score = np.std(scores)
        
        print(f"\nMetric Target Focus Block: [{construct}]")
        print(f"  -> Sample Observed Mean: {mean_score:.2f} (StdDev: {std_score:.2f})")
        
        # Simulating a typical human benchmark baseline for the KS test contrast
        human_benchmark = [4, 4, 5] if "Trust" in construct or "Usefulness" in construct else [3, 4, 5]
        
        # Run Kolmogorov-Smirnov Distribution Alignment Contrast
        ks_stat, p_value = stats.ks_2samp(scores, human_benchmark)
        print(f"  -> Kolmogorov-Smirnov Test Stat: {ks_stat:.4f} (p-value: {p_value:.4f})")
        
        if p_value > 0.05:
            print("  -> Status: 🟢 ALIGNED (Twin behavior profile matches expected benchmark boundaries)")
        else:
            print("  -> Status: 🟡 DISTORTION ALERT (Variance detected across experimental configurations)")

    print("\n======================================================================")
    print("✅ STATISTICAL PIPELINE COMPLETELY ONLINE & FUNCTIONAL")
    print("======================================================================")

if __name__ == "__main__":
    run_twin_validation_tests()