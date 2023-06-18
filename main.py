balance = 0
warehouse_store = {}

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
        else:
            warehouse_store[product_name] = -quantity
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
            print("Product not in stock")
        continue

    if command == "end":
        print("Program is closed, goodnight!")
        break
