import os
import zipfile

# Ensure you have Kaggle API credentials set up
kaggle_json_path = os.path.expanduser("~/.kaggle/kaggle.json")

if not os.path.exists(kaggle_json_path):
    raise FileNotFoundError("Kaggle API credentials not found. Place kaggle.json in ~/.kaggle/")

# Specify the dataset you want to download and the target directory
dataset_url = "berkanoztas/synthetic-transaction-monitoring-dataset-aml"
output_dir = "TMdata/"

# Ensure the target directory exists
os.makedirs(output_dir, exist_ok=True)

# Download the dataset using the Kaggle API
os.system(f"kaggle datasets download -d {dataset_url} -p {output_dir}")

# Unzip the downloaded dataset
zip_files = [f for f in os.listdir(output_dir) if f.endswith('.zip')]
for zip_file in zip_files:
    with zipfile.ZipFile(os.path.join(output_dir, zip_file), 'r') as zf:
        zf.extractall(output_dir)
    os.remove(os.path.join(output_dir, zip_file))

print(f"Dataset downloaded and extracted to {output_dir}")
