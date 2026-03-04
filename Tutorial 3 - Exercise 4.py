data = [
    "Joe Desktop 500",
    "Joe Laptop 200",
    "Joe Desktop 400",
    "Mary Desktop 200",
    "Mary Laptop 800",
    "Beth Laptop 500",
    "Beth Tablet 250",
    "Joe Tablet 250"
]

computers = {}

for line in data:
    owner, comp_type, value = line.split()
    value = int(value)

    if owner not in computers:
        computers[owner] = {}

    if comp_type in computers[owner]:
        computers[owner][comp_type] += value
    else:
        computers[owner][comp_type] = value

print(computers)