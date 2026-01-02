# ============================================================
# CST435 - Assignment 2
# Parallel Image Processing Benchmark
# ============================================================
# This script performs:
# 1. System setup
# 2. Virtual environment creation
# 3. Dependency installation
# 4. Benchmark execution
# 5. Output compression
# 6. Sample extraction for Worker 2
# ============================================================


# -------------------------------
# STEP 1: Update system packages
# -------------------------------
# Ensures package lists are up to date
sudo apt update

# Install required system tools:=
sudo apt install -y python3-pip python3-venv git zip


# -------------------------------
# STEP 2: Clone assignment repo
# -------------------------------
# Downloads the project source code
git clone https://github.com/faizaladullah/Assignment2CST435.git

# Enter project directory
cd Assignment2CST435 


# -----------------------------------
# STEP 3: Python virtual environment
# -----------------------------------
# Create isolated Python environment
python3 -m venv venv

# Activate virtual environment
3source venv/bin/activate


# -----------------------------------
# STEP 4: Install Python dependencies
# -----------------------------------
pip install pillow numpy pandas matplotlib scipy


# -----------------------------------
# STEP 5: Prepare results directory
# -----------------------------------
# Stores benchmark timing results
mkdir -p results

# -----------------------------------
# STEP 6: Run benchmark experiment
# -----------------------------------
# Executes multiprocessing and concurrent.futures
# using 1, 2, 4, and 8 workers
python3 benchmark.py


# -----------------------------------
# STEP 7: Compress ALL processed images
# -----------------------------------
# output/ contains all processed images
# Zipped to allow easy download from GCP
sudo apt-get install zip -y
zip -r output.zip output/


# -----------------------------------
# STEP 8: Sample Worker 2 outputs
# -----------------------------------
# Only 50 images are sampled to:
# - reduce file size
# - demonstrate correctness
# - comply with submission limits


# --- Multiprocessing sample ---
mkdir -p mp_sample_output

# Copy first 50 processed images from 2 workers
cp $(ls output/multiprocessing/2_workers/*.jpg | head -n 50) mp_sample_output/

# Compress sample folder
zip -r mp_sample.zip mp_sample_output

# --- Concurrent Futures sample ---
mkdir -p cf_sample_output

# Copy first 50 processed images from 2 workers
cp $(ls output/concurrent_futures/2_workers/*.jpg | head -n 50) cf_sample_output/

# Compress sample folder
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
