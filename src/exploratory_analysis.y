import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load merged dataset
df = pd.read_csv('../data/happiness_combined.csv')

# Summary statistics
print(df.describe())

# Boxplot of happiness scores over the years
plt.figure(figsize=(12, 6))
sns.boxplot(x='Year', y='Happiness Score', data=df)
plt.title('Distribution of Happiness Scores Over the Years')
plt.savefig('../docs/happiness_distribution.png')
plt.show()
