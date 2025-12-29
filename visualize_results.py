# visualize_results.py
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def create_performance_graphs():
    """Generate all performance comparison graphs"""
    
    # Load data
    df = pd.read_csv('results/metrics_with_speedup.csv')
    
    # Set style
    plt.style.use('seaborn-v0_8-darkgrid')
    
    # Create figure with subplots
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('Parallel Image Processing Performance Analysis', 
                 fontsize=16, fontweight='bold')
    
    # Graph 1: Execution Time Comparison
    ax1 = axes[0, 0]
    mp_data = df[df['method'] == 'multiprocessing']
    cf_data = df[df['method'] == 'concurrent.futures']
    
    x = np.arange(len(mp_data))
    width = 0.35
    
    ax1.bar(x - width/2, mp_data['total_time'], width, 
            label='Multiprocessing', color='#2E86AB')
    ax1.bar(x + width/2, cf_data['total_time'], width, 
            label='Concurrent.Futures', color='#A23B72')
    
    ax1.set_xlabel('Number of Workers')
    ax1.set_ylabel('Execution Time (seconds)')
    ax1.set_title('Execution Time vs Number of Workers')
    ax1.set_xticks(x)
    ax1.set_xticklabels(mp_data['num_workers'])
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Graph 2: Speedup Comparison
    ax2 = axes[0, 1]
    ax2.plot(mp_data['num_workers'], mp_data['speedup'], 
             marker='o', linewidth=2, markersize=8, 
             label='Multiprocessing', color='#2E86AB')
    ax2.plot(cf_data['num_workers'], cf_data['speedup'], 
             marker='s', linewidth=2, markersize=8, 
             label='Concurrent.Futures', color='#A23B72')
    
    # Add ideal speedup line
    ax2.plot(mp_data['num_workers'], mp_data['num_workers'], 
             linestyle='--', color='gray', label='Ideal Speedup')
    
    ax2.set_xlabel('Number of Workers')
    ax2.set_ylabel('Speedup')
    ax2.set_title('Speedup Analysis')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    # Graph 3: Efficiency Comparison
    ax3 = axes[1, 0]
    ax3.plot(mp_data['num_workers'], mp_data['efficiency'] * 100, 
             marker='o', linewidth=2, markersize=8, 
             label='Multiprocessing', color='#2E86AB')
    ax3.plot(cf_data['num_workers'], cf_data['efficiency'] * 100, 
             marker='s', linewidth=2, markersize=8, 
             label='Concurrent.Futures', color='#A23B72')
    
    ax3.axhline(y=100, linestyle='--', color='gray', label='100% Efficiency')
    ax3.set_xlabel('Number of Workers')
    ax3.set_ylabel('Efficiency (%)')
    ax3.set_title('Parallel Efficiency')
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    
    # Graph 4: Throughput Comparison
    ax4 = axes[1, 1]
    ax4.bar(x - width/2, mp_data['throughput'], width, 
            label='Multiprocessing', color='#2E86AB')
    ax4.bar(x + width/2, cf_data['throughput'], width, 
            label='Concurrent.Futures', color='#A23B72')
    
    ax4.set_xlabel('Number of Workers')
    ax4.set_ylabel('Throughput (images/second)')
    ax4.set_title('Processing Throughput')
    ax4.set_xticks(x)
    ax4.set_xticklabels(mp_data['num_workers'])
    ax4.legend()
    ax4.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('results/graphs/performance_comparison.png', dpi=300, bbox_inches='tight')
    print("✅ Performance graphs saved to results/graphs/performance_comparison.png")
    
    plt.show()


def create_comparison_table():
    """Create formatted comparison table"""
    df = pd.read_csv('results/metrics_with_speedup.csv')
    
    # Create summary table
    summary = df[['method', 'num_workers', 'total_time', 'speedup', 'efficiency', 'throughput']]
    summary['efficiency'] = (summary['efficiency'] * 100).round(2)
    summary = summary.round(4)
    
    print("\n" + "="*100)
    print("PERFORMANCE COMPARISON TABLE")
    print("="*100)
    print(summary.to_string(index=False))
    print("="*100)
    
    # Save to text file
    with open('results/comparison_table.txt', 'w') as f:
        f.write(summary.to_string(index=False))
    
    print("\n✅ Comparison table saved to results/comparison_table.txt")


if __name__ == "__main__":
    import os
    os.makedirs('results/graphs', exist_ok=True)
    
    create_performance_graphs()
    create_comparison_table()