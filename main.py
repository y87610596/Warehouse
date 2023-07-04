balance = 0
warehouse_store = {}
operations = []

balance_file = "balance.txt"
inventory_file = "inventory.txt"
history_file = "history.txt"

with open(balance_file, 'r') as file:
        balance = file.readline()
        if balance:
            balance = float(balance)
        if not balance:
            balance = 0

with open(inventory_file, 'r') as file:
    while True:
        response = file.readline()
        if not response:
            break
        key, value = response.strip().split(':')
        warehouse_store[key] = value

with open(history_file, 'r') as file:
    while True:
        response = file.readline()
        if not response:
            break
        operations.append(response)

while True:
    print("Available commands:")
    print("balance\nsale\npurchase\naccount\nlist\nwarehouse\nreview\nend")
    command = input("Enter a command:")


    if command == "balance":
        change_on_balance = float(input("Please enter change on balance"))
        balance += change_on_balance
        continue



    if command == "sale":
        product_name = input("Enter the name of the product: ")
        price = float(input("Enter the price of the product: "))
        quantity = int(input("Enter the quantity of the product sold: "))
        total_sale = price * quantity
        total_sale = float(total_sale)
        balance += total_sale
        if product_name in warehouse_store:
            warehouse_store[product_name] -= quantity
            operations.append(f"Sale: {product_name} - {quantity} units")
        else:
            print("Product not available in warehouse.")
        continue

    if command == "purchase":
        product_name = input("Enter the name of the product: ")
        price = float(input("Enter the price of the product: "))
        quantity = int(input("Enter the quantity of the product bought: "))
        total_purchase = price * quantity
        total_purchase = float(total_purchase)
        if total_purchase > balance :
            print("Balance not enough, cannot purchase")
            continue

        balance -= total_purchase
        if product_name in warehouse_store :
            warehouse_store[product_name] += quantity
        else:
            warehouse_store[product_name] = quantity

        operations.append(f"Purchase: {product_name} - {quantity} units")
        continue


    if command == "account":
        print(f"Your balance:${balance}")
        continue



    if command == "list":
        for product_name, quantity in warehouse_store.items():
            print(f"Product: {product_name} Quatity: {quantity}")
        continue


    if command == "warehouse":
        single_product = input()
        if single_product in warehouse_store :
            quantity = warehouse_store[single_product]
            print(f"{single_product} has {quantity} in stock")

        else:
            print("Product is not in stock")
        continue

    if command == "review":
        from_index = input("Enter the 'from' index: ")
        to_index = input("Enter the 'to' index: ")

        if not from_index:
            from_index = 0
        else:
            from_index = int(from_index)

        if not to_index:
            to_index = len(operations)
        else:
            to_index = int(to_index)

        if from_index < 0 or to_index > len(operations) or from_index > to_index:
            print("Invalid range.")
        else:
            print("Recorded operations:")
            for op in operations[from_index:to_index]:
                print(op)

    if command == "end":
        with open(balance_file, 'w') as file:
            file.write(str(balance))

        with open(inventory_file, 'w') as file:
            for product_name, quantity in warehouse_store.items():
                file.write(f"{product_name}:{quantity}\n")

        with open(history_file, 'w') as file:
            for op in operations:
                file.write(op)

        print("Program is now closed, goodnight!")
        break
