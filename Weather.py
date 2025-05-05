import pandas as pd
from collections import defaultdict

# Load and clean data
df = pd.read_csv(r"C:\Users\HP\Downloads\mumbai_weather.csv")
df = df.dropna(subset=['tavg'])
df['year'] = pd.to_datetime(df['time'], dayfirst=True).dt.year

# MAP Phase: (year, tavg)
mapped = [(row['year'], row['tavg']) for _, row in df.iterrows()]

# SHUFFLE Phase: group by year
shuffled = defaultdict(list)
for year, temp in mapped:
    shuffled[year].append(temp)

# REDUCE Phase: calculate averages
reduced = {year: sum(shuffled[year]) / len(shuffled[year]) for year in shuffled}

# Find hottest and coolest
hottest = max(reduced.items(), key=lambda x: x[1])
coolest = min(reduced.items(), key=lambda x: x[1])

# Print
print("=== Yearly Avg Temps ===")
for year in sorted(reduced):
    print(f"{year}: {reduced[year]:.2f}°C")

print(f"\nHottest Year: {hottest[0]} ({hottest[1]:.2f}°C)")
print(f"Coolest Year: {coolest[0]} ({coolest[1]:.2f}°C)")
