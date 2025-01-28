def add_item(cart):
    item = input("Enter the item name to be added: ")
    price = float(input("Enter the price of the item added: "))
    cart.append({"name": item, "price": price})  # Add item as a dictionary
    print("Item added successfully!")

def view_items(cart):
    if not cart:
        print("The cart is empty!")
    else:
        for index, item in enumerate(cart, start=1):
            print(f"{index}. {item['name']} - ${item['price']}")  # Display items and their prices

def price_cal(cart):
    if not cart:
        print("The cart is empty!")
    else:
        total = sum(item['price'] for item in cart)  # Sum up prices of all items
        print(f"Total price of items in the cart: ${total}")

def main():
    cart = []  # Initialize an empty shopping cart
    while True:  #loop to choose items
        print("\n1. Add item to the cart")
        print("2. View items in the cart")
        print("3. Calculate the total price of items in the cart")
        print("4. Exit")
        choice = input("Select any one option from above: ")  # Get user's choice
        
        if choice == "1":
            add_item(cart)
        elif choice == "2":
            view_items(cart)
        elif choice == "3":
            price_cal(cart)
        elif choice == "4":
            print("Thank you for shopping! Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

main()
