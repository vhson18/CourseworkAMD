import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("C:\\Users\\my pc\\Downloads\\World_Population_CountryWise_RAW.csv")

# Select the first 250 countries
df = df.iloc[:250, :]

# Convert population columns to numeric, handling errors
population_cols = df.columns[2:]
df[population_cols] = df[population_cols].apply(pd.to_numeric, errors='coerce')

# Fill missing values with column means
df[population_cols].fillna(df[population_cols].mean(), inplace=True)

# Calculate statistical measures
stats = df[population_cols].describe().T
stats['median'] = df[population_cols].median()
stats['mode'] = df[population_cols].mode().iloc[0]
stats['std'] = df[population_cols].std()

# Function to plot statistics with rotated x-axis labels
def plot_statistics(stat, label, title, color='blue'):
    plt.figure(figsize=(12, 6))
    plt.plot(stats.index, stats[stat], label=label, color=color)
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.title(title)
    plt.xticks(rotation=90)  # Rotate x-axis labels
    plt.legend()
    plt.grid(True)
    plt.show()

# Visualizations
plot_statistics('mean', 'Mean', 'Mean Population Over Years')
plot_statistics('median', 'Median', 'Median Population Over Years', color='orange')
plot_statistics('std', 'Standard Deviation', 'Standard Deviation of Population Over Years', color='green')
