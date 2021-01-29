categories = input().split(", ")
n = int(input())
items = [input().split(" - ") for _ in range(n)]

items_data = {}
#items_data = {items_data[c]: {} for c in categories}

for c in categories:
    items_data[c] = {}

sum_quantity = 0
for el in items:
    cat, item, q_data = el
    quantity, quality = q_data.split(";")
    quality_data = quality.split(":")
    quality_num = int(quality_data[1])
    quantity_data = quantity.split(":")
    quantity_num = int(quantity_data[1])
    items_data[cat][item] = {"Quality": quality_num, "Quantity": quantity_num}


it = []
quantity_sum = 0
quality_sum = 0
for key, value in items_data.items():
    for k, v in value.items():
        quantity_sum += v["Quantity"]
        quality_sum += (v["Quality"])
print(f"Count of items: {quantity_sum}")
print(f"Average quality: {quality_sum/len(categories):.2f}")


for key, value in items_data.items():
    print(f"{key} -> ", end="")
    for k, v in value.items():
        it.append(k)
    print(", ".join(it))
    it = []
