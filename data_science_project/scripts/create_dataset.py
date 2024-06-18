# scripts/create_dataset.py
import pandas as pd

# Create a sample dataset
data = {
    'age': [23, 45, 22, 34, 42, 54, 25, 23, 33, 45, 26, 27, 32, 34, 30, 31, 29, 28, 27, 26],
    'gender': ['male', 'female', 'female', 'male', 'female', 'male', 'female', 'male', 'female', 'male', 'female', 'male', 'female', 'male', 'female', 'male', 'female', 'male', 'female', 'male']
}

df = pd.DataFrame(data)

# Save to CSV
csv_path = 'D:\Sem 5\Data Science\PRASUNET_DS_01\data_science_project\data\sample_population.csv'
df.to_csv(csv_path, index=False)
print(f"Dataset saved to {csv_path}")