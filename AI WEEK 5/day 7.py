import micropip
await micropip.install("pandas")
import pandas as pd

data = {
    "day":      ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "steps":    [9200, 10500, 8800, 11000, 7600, 9400, 10200],
    "sleep_hr": [7.5, 8.0, 6.5, 7.0, 9.0, 7.5, 8.0],
    "water":    [7, 8, 6, 9, 8, 7, 8],
}
df = pd.DataFrame(data)

print("Statistics for all numeric columns:")
print(df.describe().to_string())

print("\nManual checks:")
print(f"Mean steps:  {df['steps'].mean():.0f}")
print(f"Max steps:   {df['steps'].max()}")
print(f"Min steps:   {df['steps'].min()}")
print(f"Total steps: {df['steps'].sum()}")
# In VS Code
import pandas as pd

df = pd.read_csv("weekly_log.csv")
print(df.head())
print(df.shape)