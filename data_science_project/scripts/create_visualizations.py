# scripts/create_visualizations.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
csv_path = 'D:\Sem 5\Data Science\PRASUNET_DS_01\data_science_project\data\sample_population.csv'
df = pd.read_csv(csv_path)

# Bar Chart for Gender Distribution
gender_counts = df['gender'].value_counts()

fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.barplot(x=gender_counts.index, y=gender_counts.values, palette='viridis', ax=ax1)
ax1.set_xlabel('Gender')
ax1.set_ylabel('Count')
ax1.set_title('Distribution of Genders in the Population')
gender_chart_path = 'D:\Sem 5\Data Science\PRASUNET_DS_01\data_science_project\output\gender_distribution.png'
fig1.savefig(gender_chart_path)
print(f"Gender distribution chart saved to {gender_chart_path}")

# Histogram for Age Distribution
fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.histplot(df['age'], bins=10, kde=True, color='blue', ax=ax2)
ax2.set_xlabel('Age')
ax2.set_ylabel('Frequency')
ax2.set_title('Distribution of Ages in the Population')
age_chart_path = 'D:\Sem 5\Data Science\PRASUNET_DS_01\data_science_project\output/age_distribution.png'
fig2.savefig(age_chart_path)
print(f"Age distribution chart saved to {age_chart_path}")
