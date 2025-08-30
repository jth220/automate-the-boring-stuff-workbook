def display_inventory(inventory: dict[str, int]) -> None:
    # print header
    # iterate items and print "<count> <item>"
    # compute and print total
    print("Inventory")
    total = 0
    for item, count in inventory.items():
        print(f"{count} {item}")
        total += count

    print(f"Total number of items is : {total}")

def add_to_inventory(inventory: dict[str, int], added_items: list[str]) -> dict[str, int]:
    # for each name in added_items: inventory[name] = inventory.get(name, 0) + 1
    # return inventory
    for item in added_items:
        inventory.setdefault(item, 0)
        inventory[item] += 1

    return inventory