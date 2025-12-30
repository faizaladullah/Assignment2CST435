- Installation & Setup
1. System Update and Prerequisites
Update the local package index and install Python 3 and Pip:

sudo apt update

sudo apt install -y python3-pip python3-venv git

2. Virtual Environment Setup
Create and activate a virtual environment to manage dependencies:

python3 -m venv venv

source venv/bin/activate

3. Install Dependencies
Install the required libraries for image processing, numerical calculations, and visualization:

pip install pillow numpy pandas matplotlib  

pip3 install scipy

- Execution Guide
1. Clone the Repository
   
sudo apt-get install git -y

git clone https://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@github.com/faizaladullah/Assignment2CST435.git

cd Assignment2CST435

2. Create results directory

mkdir -p results

3. Run Benchmark
Execute the comprehensive benchmark for both multiprocessing and concurrent.futures across 1, 2, 4 and 8 workers:

python3 benchmark.py


- To download all processed images from GCP to your local machine:

sudo apt-get install zip -y
zip -r output.zip output/

Download Path: /home/"username"/Assignment2CST435/output.zip

- to download sample Worker 2 outputs for both methods

sudo apt-get install zip -y

1. Sample from Multiprocessing Results
Bash

-Create a temporary directory for samples
mkdir -p mp_sample_output

-Copy the first 50 processed images (approx. 10 original sets)
cp $(ls output/multiprocessing/2_workers/*.jpg | head -n 50) mp_sample_output/

- Compress the sample folder
zip -r mp_sample.zip mp_sample_output/
Download Path: /home/mohamadfaizal1656/Assignment2CST435/mp_sample.zip

2. Sample from Concurrent.Futures Results
Bash

-Create a temporary directory for samples
mkdir -p cf_sample_output

-Copy the first 50 processed images
cp $(ls output/concurrent_futures/2_workers/*.jpg | head -n 50) cf_sample_output/

-Compress the sample folder
zip -r cf_sample.zip cf_sample_output/
Download Path: /home/mohamadfaizal1656/Assignment2CST435/cf_sample.zip