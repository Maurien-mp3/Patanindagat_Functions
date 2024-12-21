# shows the menu
def show_menu():
    items = {
        1: ("Burger", 5.99),
        2: ("Pizza", 8.99),
        3: ("Salad", 4.99),
        4: ("Fries", 2.99),
        5: ("Soda", 1.99)
    }
    print("Available Options:")
    for shop, (name, cost) in items.items():
        print(f"{shop}. {name} - ${cost:.2f}")
    return items


# choose items
def choose_item(items):
    while True:
        try:
            selection = int(input("Select an item by its number: "))
            if selection in items:
                return items[selection]
            else:
                print("Selection not valid. Try again.")
        except ValueError:
            print("Please input a valid number.")

# payment 
def handle_payment(amount_due):
    while True:
        try:
            payment = float(input(f"Amount due is ${amount_due:.2f}. Enter payment: $"))
            if payment >= amount_due:
                refund = payment - amount_due
                print(f"Transaction successful. Change: ${refund:.2f}.")
                break
            else:
                print(f"Insufficient funds. Remaining balance: ${amount_due - payment:.2f}.")
        except ValueError:
            print("Enter a valid monetary value.")

# shows the overall order 
def execute_order():
    items = show_menu()
    selected_item, price = choose_item(items)
    print(f"You chose: {selected_item} - ${price:.2f}")
    handle_payment(price)
    print("Order completed. Have a great day!")

# execute the order process
if __name__ == "__main__":
    execute_order()
