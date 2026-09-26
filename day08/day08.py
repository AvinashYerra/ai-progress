import requests
import csv

url = "https://dummyjson.com/products"
params = {"limit": 5}

try :
    response = requests.get(url, params=params)
    data = response.json()
    products = data["products"]

    overall_products = []
    for product in products:
        each_product = []
        each_product.append(product["id"])
        each_product.append(product["title"])
        each_product.append(product["price"])
        each_product.append(product["category"])
        overall_products.append(each_product)
        print(product["title"], "-", product["price"])

    with open("products.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Title", "Price", "Category"])
        writer.writerows(overall_products)

except requests.exceptions.RequestException as e:
    print("Error occurred while fetching data:", e)