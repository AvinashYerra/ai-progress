import numpy as np

sales = np.array([
    1200,
    800,
    1500,
    2300,
    900,
    3100,
    1700
])

print("Total sales:", sales.sum())
print("Average sales:", sales.mean())
print("Highest sale:", sales.max())
print("Lowest sale:", sales.min())

high_sales = sales[sales > 1500]

print("Sales above 1500:", high_sales)