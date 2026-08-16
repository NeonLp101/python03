import sys

NEW_ITEM = "magic_item"
NEW_QUANTITY = 1

inventory = {}

print("=== Inventory System Analysis ===")

for arg in sys.argv[1:]:
    parts = arg.split(":")

    if len(parts) != 2 or parts[0] == "" or parts[1] == "":
        print(f"Error - invalid parameter '{arg}'")
        continue

    item = parts[0]
    if item in inventory:
        print(f"Redundant item '{item}' - discarding")
        continue

    try:
        quantity = int(parts[1])
    except ValueError as error:
        print(f"Quantity error for '{item}': {error}")
        continue

    if quantity < 0:
        print(f"Quantity error for '{item}': negative quantity {quantity}")
        continue

    inventory.update({item: quantity})

print(f"Got inventory: {inventory}")
print(f"Item list: {list(inventory.keys())}")

total = sum(inventory.values())
print(f"Total quantity of the {len(inventory)} items: {total}")

for item in inventory.keys():
    if total == 0:
        percentage = 0.0
    else:
        percentage = round(inventory[item] / total * 100, 1)
    print(f"Item {item} represents {percentage}%")

if len(inventory) == 0:
    print("Inventory is empty - no most or least abundant item")
else:
    most_item = ""
    least_item = ""
    for item in inventory.keys():
        if most_item == "" or inventory[item] > inventory[most_item]:
            most_item = item
        if least_item == "" or inventory[item] < inventory[least_item]:
            least_item = item

    print(f"Item most abundant: {most_item} "
          f"with quantity {inventory[most_item]}")
    print(f"Item least abundant: {least_item} "
          f"with quantity {inventory[least_item]}")

if NEW_ITEM in inventory:
    inventory.update({NEW_ITEM: inventory[NEW_ITEM] + NEW_QUANTITY})
else:
    inventory.update({NEW_ITEM: NEW_QUANTITY})

print(f"Updated inventory: {inventory}")
