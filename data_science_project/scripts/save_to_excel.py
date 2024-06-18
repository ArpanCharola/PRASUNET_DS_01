# scripts/save_to_excel.py
import pandas as pd

# Load the dataset
csv_path = 'D:\Sem 5\Data Science\PRASUNET_DS_01\data_science_project\data\sample_population.csv'
df = pd.read_csv(csv_path)
gender_counts = df['gender'].value_counts()

# Save data and visualizations to Excel
excel_path = 'D:\Sem 5\Data Science\PRASUNET_DS_01\data_science_project\output/population_data.xlsx'
with pd.ExcelWriter(excel_path) as writer:
    df.to_excel(writer, sheet_name='Population Data')
    gender_counts.to_excel(writer, sheet_name='Gender Distribution')
print(f"Data saved to Excel at {excel_path}")
