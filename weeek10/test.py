import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
df = pd.read_csv("C:\\Users\\my pc\\Downloads\\World_Population_CountryWise_RAW.csv")

# Keep only the first 250 rows for analysis
df = df.iloc[:250, :]

# Extract columns with population data (1960-2023) and convert them to numeric
population_cols = df.columns[2:]  # Assuming the first two columns are 'Country Name' and 'Country Code'
df[population_cols] = df[population_cols].apply(pd.to_numeric, errors='coerce')

# Handle any missing values by filling them with the mean of the respective columns
df[population_cols].fillna(df[population_cols].mean(), inplace=True)

# Calculate statistical measures
stats = df[population_cols].describe().T
stats['median'] = df[population_cols].median()
stats['mode'] = df[population_cols].mode().iloc[0]
stats['std'] = df[population_cols].std()

# Display the calculated statistics
print(stats)

# Plot the mean population over the years
plt.figure(figsize=(12, 6))
plt.plot(stats.index, stats['mean'], label='Mean')
plt.xlabel('Year')
plt.ylabel('Population')
plt.title('Mean Population Over Years')
plt.legend()
plt.grid(True)
plt.show()

# Plot the median population over the years
plt.figure(figsize=(12, 6))
plt.plot(stats.index, stats['median'], label='Median', color='orange')
plt.xlabel('Year')
plt.ylabel('Population')
plt.title('Median Population Over Years')
plt.legend()
plt.grid(True)
plt.show()

# Plot the standard deviation of the population over the years
plt.figure(figsize=(12, 6))
plt.plot(stats.index, stats['std'], label='Standard Deviation', color='green')
plt.xlabel('Year')
plt.ylabel('Population')
plt.title('Standard Deviation of Population Over Years')
plt.legend()
plt.grid(True)
plt.show()
