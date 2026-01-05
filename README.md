# CST435 – Assignment 2: Parallel Image Processing Benchmark

## Project Description
This project implements a parallel image processing pipeline using Python. It applies five filters (Grayscale, Gaussian Blur, Sobel Edge Detection, Sharpening, Brightness) to the Food-101 dataset. The system compares the performance of two parallel paradigms:
- **Multiprocessing** (Process-based parallelism)
- **Concurrent Futures** (High-level interface)

The benchmark evaluates performance scaling across **1, 2, 4, and 8 workers** on the Google Cloud Platform (GCP).

---

## 1. System Setup
Update system packages and install the required tools (Git, Python, Zip).

```bash
sudo apt update
sudo apt install -y python3-pip python3-venv git zip
```

## 2. Environment Configuration
Create a virtual environment to manage dependencies and install required Python libraries (`pillow`, `numpy`, etc.).

```bash
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install pillow numpy pandas matplotlib scipy
```

## 3. Installation
Clone the repository and enter the project directory.

```bash
git clone [https://github.com/faizaladullah/Assignment2CST435.git](https://github.com/faizaladullah/Assignment2CST435.git)
cd Assignment2CST435
```

## 4. Execution
Create the results directory and run the benchmark script. This script will execute the processing pipeline using both paradigms.

```bash
mkdir -p results
python3 benchmark.py
```

## 5. Output Retrieval
Use the following commands to zip and download the results from GCP.

### Option A: Download ALL Results
Compress the entire output folder:
```bash
zip -r output.zip output/
```
> **Download Path:** `/home/<username>/Assignment2CST435/output.zip`

### Option B: Download Sample Outputs (Worker Count: 2)
If the full dataset is too large, use these commands to grab a sample of 50 images from the 2-worker test case.

**Multiprocessing Sample:**
```bash
mkdir -p mp_sample_output
cp $(ls output/multiprocessing/2_workers/*.jpg | head -n 50) mp_sample_output/
zip -r mp_sample.zip mp_sample_output/
```
> **Download Path:** `/home/<username>/Assignment2CST435/mp_sample.zip`

**Concurrent Futures Sample:**
```bash
mkdir -p cf_sample_output
cp $(ls output/concurrent_futures/2_workers/*.jpg | head -n 50) cf_sample_output/
zip -r cf_sample.zip cf_sample_output/
```
> **Download Path:** `/home/<username>/Assignment2CST435/cf_sample.zip`

---

## Appendix: Output Directory Structure
After running the benchmark, the `output/` directory will be organized as follows:

```text
output/
├── multiprocessing/
│   ├── 1_workers/
│   ├── 2_workers/
│   ├── 4_workers/
│   └── 8_workers/
└── concurrent_futures/
    ├── 1_workers/
    ├── 2_workers/
    ├── 4_workers/
    └── 8_workers/
```