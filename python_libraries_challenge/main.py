import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests

# 1. NumPy Array & Mean
numbers = np.arange(1, 11)  # Array of numbers 1–10
mean_value = np.mean(numbers)
print("NumPy Array:", numbers)
print("Mean of array:", mean_value)

# 2. Pandas DataFrame & Summary Stats
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Age": [24, 30, 22, 35, 28],
    "Score": [85, 90, 78, 92, 88],
}
df = pd.DataFrame(data)
print("\nPandas DataFrame:")
print(df)

print("\nSummary Statistics:")
print(df.describe())

# 3. Requests: Fetch API Data
url = "https://api.coindesk.com/v1/bpi/currentprice.json"  # Public API
try:
    response = requests.get(url)
    response.raise_for_status()  # Raise error for bad response
    data = response.json()
    bitcoin_price = data["bpi"]["USD"]["rate"]
    print("\nCurrent Bitcoin Price (USD):", bitcoin_price)
except requests.exceptions.RequestException as e:
    print("\nError fetching API data:", e)

# 4. Matplotlib: Line Graph
y_values = [2, 4, 6, 8, 10]
x_values = range(1, len(y_values) + 1)

plt.plot(x_values, y_values, marker="o", linestyle="-", color="b")
plt.title("Simple Line Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()
