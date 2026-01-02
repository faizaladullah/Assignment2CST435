# CST435 – Assignment 2
## Parallel Image Processing Benchmark

This repository benchmarks **parallel image processing** using:

- **Multiprocessing**
- **concurrent.futures**

It evaluates performance across **1, 2, 4, and 8 workers**, stores processed images, and generates timing results.

---

```bash
# ============================================================
# CST435 - Assignment 2
# Parallel Image Processing Benchmark
# ============================================================

# -------------------------------
# STEP 1: Update system packages
# -------------------------------
sudo apt update
sudo apt install -y python3-pip python3-venv git zip

# -------------------------------
# STEP 2: Clone repository
# -------------------------------
git clone https://github.com/faizaladullah/Assignment2CST435.git
cd Assignment2CST435

# -----------------------------------
# STEP 3: Create Python virtual environment
# -----------------------------------
python3 -m venv venv
source venv/bin/activate

# -----------------------------------
# STEP 4: Install Python dependencies
# -----------------------------------
pip install pillow numpy pandas matplotlib scipy

# -----------------------------------
# STEP 5: Prepare results directory
# -----------------------------------
mkdir -p results

# -----------------------------------
# STEP 6: Run benchmark
# -----------------------------------
python3 benchmark.py

# -----------------------------------
# STEP 7: Compress all processed images
# -----------------------------------
zip -r output.zip output/

# -----------------------------------
# STEP 8: Sample Worker 2 outputs
# -----------------------------------

# --- Multiprocessing sample ---
mkdir -p mp_sample_output
cp $(ls output/multiprocessing/2_workers/*.jpg | head -n 50) mp_sample_output/
zip -r mp_sample.zip mp_sample_output/

# --- Concurrent Futures sample ---
mkdir -p cf_sample_output
cp $(ls output/concurrent_futures/2_workers/*.jpg | head -n 50) cf_sample_output/
zip -r cf_sample.zip cf_sample_output/

# -----------------------------------
# STEP 9: Final confirmation
# -----------------------------------
echo "============================================"
echo "Benchmark completed successfully."
echo "Generated files:"
echo " - output.zip      (all processed images)"
echo " - mp_sample.zip   (multiprocessing samples)"
echo " - cf_sample.zip   (concurrent futures samples)"
echo "============================================"

# -----------------------------------
# Output directory structure
# -----------------------------------
# output/
# ├── multiprocessing/
# │   ├── 1_workers/
# │   ├── 2_workers/
# │   ├── 4_workers/
# │   └── 8_workers/
# └── concurrent_futures/
#     ├── 1_workers/
#     ├── 2_workers/
#     ├── 4_workers/
#     └── 8_workers/
