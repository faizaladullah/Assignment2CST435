# multiprocessing_impl.py
import os
import time
import multiprocessing as mp
from filters import apply_all_filters
from pathlib import Path

def process_image_worker(args):
    """Worker function for multiprocessing"""
    image_path, output_dir = args
    return apply_all_filters(image_path, output_dir)


def run_multiprocessing(image_dir, output_dir, num_workers):
    """
    Run image processing using multiprocessing.Pool
    
    Args:
        image_dir: Directory containing input images
        output_dir: Directory to save processed images
        num_workers: Number of processes to use
    
    Returns:
        dict with execution time and statistics
    """
    print(f"\n{'='*60}")
    print(f"MULTIPROCESSING MODE - {num_workers} Workers")
    print(f"{'='*60}")
    
    # Get all image paths
    image_paths = list(Path(image_dir).glob('*.jpg')) + \
                  list(Path(image_dir).glob('*.png')) + \
                  list(Path(image_dir).glob('*.jpeg'))
    
    total_images = len(image_paths)
    print(f"Total images to process: {total_images}")
    
    # Create output directory if doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Prepare arguments for workers
    worker_args = [(str(img_path), output_dir) for img_path in image_paths]
    
    # Start timing
    start_time = time.time()
    
    # Create process pool and execute
    results = []
    completed = 0
    with mp.Pool(processes=num_workers) as pool:
        for result in pool.imap_unordered(process_image_worker, worker_args):
            results.append(result)
            completed += 1
            
            if completed % 1000 == 0 or completed == total_images:
                print(f"Progress: {completed}/{total_images} images processed")
    
    # Calculate total time
    total_time = time.time() - start_time
    
    # Analyze results
    successful = sum(1 for r in results if r['success'])
    failed = total_images - successful
    
    
    avg_time_per_image = total_time / total_images 
    
    # Optional: Calculate total CPU time for analysis
    total_cpu_time = sum(r['duration'] for r in results)
    cpu_utilization = (total_cpu_time / (total_time * num_workers)) * 100
    
    print(f"\n{'='*60}")
    print(f"RESULTS:")
    print(f"Total Wall Clock Time: {total_time:.4f} seconds")
    print(f"Total CPU Time (all workers): {total_cpu_time:.4f} seconds")
    print(f"Images Processed: {successful}/{total_images}")
    print(f"Failed: {failed}")
    print(f"Average Time per Image: {avg_time_per_image:.4f}s") 
    print(f"Throughput: {total_images/total_time:.2f} images/second")
    print(f"CPU Utilization: {cpu_utilization:.2f}%")
    print(f"{'='*60}\n")
    
    return {
        'method': 'multiprocessing',
        'num_workers': num_workers,
        'total_time': total_time,
        'total_cpu_time': total_cpu_time, 
        'total_images': total_images,
        'successful': successful,
        'failed': failed,
        'avg_time_per_image': avg_time_per_image, 
        'throughput': total_images / total_time,
        'cpu_utilization': cpu_utilization  
    }


if __name__ == "__main__":
    # Test with different worker counts
    IMAGE_DIR = "images"
    OUTPUT_BASE = "output/multiprocessing"
    
    for workers in [1, 2, 4, 8]:
        output_dir = f"{OUTPUT_BASE}/{workers}_workers"
        result = run_multiprocessing(IMAGE_DIR, output_dir, workers)
        print(f"Result: {result}\n")


