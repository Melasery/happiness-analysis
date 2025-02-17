import pandas as pd

# Load datasets
df_2015 = pd.read_csv('../data/2015.csv')
df_2016 = pd.read_csv('../data/2016.csv')
df_2017 = pd.read_csv('../data/2017.csv')
df_2018 = pd.read_csv('../data/2018.csv')
df_2019 = pd.read_csv('../data/2019.csv')

# Handling missing values
df_2018['Perceptions of corruption'].fillna(df_2018['Perceptions of corruption'].mean(), inplace=True)

# Save cleaned datasets
df_2018.to_csv('../data/2018_cleaned.csv', index=False)

print("Missing values handled and datasets cleaned.")
