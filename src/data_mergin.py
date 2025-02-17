import pandas as pd

# Load cleaned datasets
df_2015 = pd.read_csv('../data/2015.csv')
df_2016 = pd.read_csv('../data/2016.csv')
df_2017 = pd.read_csv('../data/2017.csv')
df_2018 = pd.read_csv('../data/2018_cleaned.csv')  # Using cleaned version
df_2019 = pd.read_csv('../data/2019.csv')

# Standardize column names
df_2015.columns = ['Country', 'Happiness Rank', 'Happiness Score', 'Economy (GDP per Capita)', 'Family', 'Health (Life Expectancy)', 'Freedom', 'Trust (Government Corruption)', 'Generosity', 'Dystopia Residual']
df_2016.columns = df_2015.columns
df_2017.columns = df_2015.columns
df_2018.columns = df_2015.columns[:-1]  # 2018 doesn't have 'Dystopia Residual'
df_2019.columns = df_2015.columns[:-1]

# Add 'Year' column
df_2015['Year'], df_2016['Year'], df_2017['Year'], df_2018['Year'], df_2019['Year'] = 2015, 2016, 2017, 2018, 2019

# Merge datasets
df_combined = pd.concat([df_2015, df_2016, df_2017, df_2018, df_2019], ignore_index=True)

# Save merged dataset
df_combined.to_csv('../data/happiness_combined.csv', index=False)

print("Datasets merged successfully.")
