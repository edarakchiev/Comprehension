names = input().split(", ")
name_dict = {}

name_dict = {name: {} for name in names}

while True:
    data = input()
    if data == "End":
        break
    name, item, price = data.split("-")
    if item in name_dict[name]:
        continue
    name_dict[name][item] = price

for key, value in name_dict.items():
    print(f"{key} -> Items: {len(value)}, Cost: ", end="")
    prices = 0
    for current_item, item_price in value.items():
        prices += int(item_price)
    print(prices)



