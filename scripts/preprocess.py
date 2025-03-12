import pandas as pd

def preprocess_data(input_path, output_path):
    df = pd.read_csv(input_path)
    df.dropna(inplace=True)
    df.to_csv(output_path, index=False)

input_file = "data/raw/sample_health_data.csv"
output_file = "data/processed/cleaned_data.csv"

preprocess_data(input_file, output_file)
print(f"Data saved to {output_file}")
