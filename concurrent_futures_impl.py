# concurrent_futures_impl.py
import os
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from filters import apply_all_filters
from pathlib import Path

def run_concurrent_futures(image_dir, output_dir, num_workers):
    """
    Run image processing using concurrent.futures
    
    Args:
        image_dir: Directory containing input images
        output_dir: Directory to save processed images
        num_workers: Number of processes to use
    
    Returns:
        dict with execution time and statistics
    """
    print(f"\n{'='*60}")
    print(f"CONCURRENT.FUTURES MODE - {num_workers} Workers")
    print(f"{'='*60}")
    
    # Get all image paths
    image_paths = list(Path(image_dir).glob('*.jpg')) + \
                  list(Path(image_dir).glob('*.png')) + \
                  list(Path(image_dir).glob('*.jpeg'))
    
    total_images = len(image_paths)
    print(f"Total images to process: {total_images}")
    
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    
    # Start timing
    start_time = time.time()
    results = []
    
    # Use ProcessPoolExecutor
    with ProcessPoolExecutor(max_workers=num_workers) as executor:
        # Submit all tasks
        future_to_image = {
            executor.submit(apply_all_filters, str(img_path), output_dir): img_path
            for img_path in image_paths
        }
        
        # Process completed tasks
        completed = 0
        for future in as_completed(future_to_image):
            result = future.result()
            results.append(result)
            completed += 1
            
            # Progress indicator
            if completed % 50 == 0 or completed == total_images:
                print(f"Progress: {completed}/{total_images} images processed")
    
    # Calculate total time
    total_time = time.time() - start_time
    
    # Analyze results
    successful = sum(1 for r in results if r['success'])
    failed = total_images - successful
    avg_time_per_image = sum(r['duration'] for r in results) / total_images
    
    print(f"\n{'='*60}")
    print(f"RESULTS:")
    print(f"Total Time: {total_time:.4f} seconds")
    print(f"Images Processed: {successful}/{total_images}")
    print(f"Failed: {failed}")
    print(f"Average Time per Image: {avg_time_per_image:.4f}s")
    print(f"Throughput: {total_images/total_time:.2f} images/second")
    print(f"{'='*60}\n")
    
    return {
        'method': 'concurrent.futures',
        'num_workers': num_workers,
        'total_time': total_time,
        'total_images': total_images,
        'successful': successful,
        'failed': failed,
        'avg_time_per_image': avg_time_per_image,
        'throughput': total_images / total_time
    }


if __name__ == "__main__":
    # Test with different worker counts
    IMAGE_DIR = "images"
    OUTPUT_BASE = "output/concurrent_futures"
    
    for workers in [1, 2, 4]:
        output_dir = f"{OUTPUT_BASE}/{workers}_workers"
        result = run_concurrent_futures(IMAGE_DIR, output_dir, workers)
        print(f"Result: {result}\n")