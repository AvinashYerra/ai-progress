import csv

validlist = []

with open("customer.csv", "r") as file:
    reader = csv.reader(file)

    header = next(reader)
    validlist.append(header)

    for row in reader:
        try:
            if int(row[2]) >= 1000:
                    validlist.append(row)
        except (ValueError, IndexError):
            print(f"Invalid row: {row}")

with open("high_value_customers.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(validlist)