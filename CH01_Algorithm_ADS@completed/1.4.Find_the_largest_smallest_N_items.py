import heapq
import random

nums = [33, -32, 90, 2, 3, -94, 100, 3]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))

################
portfolio = []
for _ in range(6):
    tem = {"name": "xx", "price": random.random() * 100}
    portfolio.append(tem)

print("portfolio:")
print("           ")
print(portfolio)
cheap = heapq.nlargest(3, portfolio, key=lambda x: x["price"])
expensive = heapq.nsmallest(3, portfolio, key=lambda x: x["price"])
print(cheap)
print(expensive)

#some usage
heapq.heapify([])
heapq.heappop([])
heapq.heappush([], 1)