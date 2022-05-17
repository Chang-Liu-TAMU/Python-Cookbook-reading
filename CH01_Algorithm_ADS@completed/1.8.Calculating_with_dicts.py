prices = {
    "ryu": 45.23,
    "ken": 612.78,
    "sukura": 90.12,
    "luke": 839.0,
    "drug": 89.23
}

mini = min(zip(prices.values(), prices.keys()))
maxi = max(zip(prices.values(), prices.keys()))
print(f"mini: {mini}")
print(f"maxi: {maxi}")

prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)

mini_key = min(prices, key=lambda x: prices[x])
max_key = max(prices, key=lambda x: prices[x])
print(mini_key)
print(max_key)