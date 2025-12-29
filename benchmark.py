# benchmark.py
import pandas as pd
from multiprocessing_impl import run_multiprocessing
from concurrent_futures_impl import run_concurrent_futures

def run_comprehensive_benchmark(image_dir, worker_counts=[1, 2, 4, 8]):
    """
    Run comprehensive benchmark comparing both methods
    """
    all_results = []
    
    print("\n" + "="*70)
    print("COMPREHENSIVE BENCHMARK - PARALLEL IMAGE PROCESSING")
    print("="*70)
    
    # Test multiprocessing
    print("\n### TESTING MULTIPROCESSING ###")
    for workers in worker_counts:
        output_dir = f"output/multiprocessing/{workers}_workers"
        result = run_multiprocessing(image_dir, output_dir, workers)
        all_results.append(result)
    
    # Test concurrent.futures
    print("\n### TESTING CONCURRENT.FUTURES ###")
    for workers in worker_counts:
        output_dir = f"output/concurrent_futures/{workers}_workers"
        result = run_concurrent_futures(image_dir, output_dir, workers)
        all_results.append(result)
    
    # Save results to CSV
    df = pd.DataFrame(all_results)
    df.to_csv('results/metrics.csv', index=False)
    
    print("\n" + "="*70)
    print("BENCHMARK COMPLETE - Results saved to results/metrics.csv")
    print("="*70)
    
    return df


def calculate_speedup_efficiency(df):
    """
    Calculate speedup and efficiency metrics
    """
    # Get baseline (1 worker) times for each method
    baseline_mp = df[(df['method'] == 'multiprocessing') & 
                     (df['num_workers'] == 1)]['total_time'].values[0]
    
    baseline_cf = df[(df['method'] == 'concurrent.futures') & 
                     (df['num_workers'] == 1)]['total_time'].values[0]
    
    # Calculate speedup and efficiency
    df['speedup'] = df.apply(
        lambda row: (baseline_mp if row['method'] == 'multiprocessing' 
                    else baseline_cf) / row['total_time'],
        axis=1
    )
    
    df['efficiency'] = df['speedup'] / df['num_workers']
    
    return df


if __name__ == "__main__":
    IMAGE_DIR = "pizza"
    WORKER_COUNTS = [1, 2, 4]  # Adjust based on your VM's vCPUs
    
    # Run benchmark
    results_df = run_comprehensive_benchmark(IMAGE_DIR, WORKER_COUNTS)
    
    # Calculate speedup and efficiency
    results_df = calculate_speedup_efficiency(results_df)
    
    # Save enhanced metrics
    results_df.to_csv('results/metrics_with_speedup.csv', index=False)
    
    # Display summary
    print("\n" + "="*70)
    print("PERFORMANCE SUMMARY")
    print("="*70)
    print(results_df.to_string())