import csv

with open("customers.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)


with open("customers.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)




customers = [
    ["customer_id", "name", "city"],
    ["1001", "ABC Healthcare", "Pune"],
    ["1002", "XYZ Hospital", "Mumbai"],
    ["1003", "PQR Pharmacy", "Delhi"]
]

with open("output.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerows(customers)

with open("data.txt", "r") as file:
    content = file.read()

print(content)

with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())


with open("data.txt", "r") as file:
    lines = file.readlines()

print(lines)

with open("output.txt", "w") as file:
    file.write("Hello Python\n")
    file.write("Learning file handling\n")


with open("output.txt", "a") as file:
    file.write("New line\n")