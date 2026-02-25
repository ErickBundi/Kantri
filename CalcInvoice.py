def get_price():
    """Prompt user for price and validate it's a float"""
    while True:
        try:
            price = float(input("Enter price: "))
            return price
        except ValueError:
            print("Invalid decimal number. Please try again.")


def get_quantity():
    """Prompt user for quantity and validate it's an integer"""
    while True:
        try:
            quantity = int(input("Enter quantity: "))
            return quantity
        except ValueError:
            print("Invalid integer. Please try again.")


def main():
    """Main program loop for invoice line item calculator"""
    print("The Invoice Line Item Calculator")
    
    while True:
        # Get price and quantity from user
        price = get_price()
        quantity = get_quantity()
        
        # Calculate total
        total = price * quantity
        
        # Display results
        print(f"\nPRICE:        {price:.2f}")
        print(f"QUANTITY:     {quantity}")
        print(f"TOTAL:        {total:.2f}")
        
        # Ask if user wants to enter another item
        while True:
            another = input("Enter another line item? (y/n): ").lower()
            if another in ['y', 'n']:
                break
        
        if another == 'n':
            print("\nBye!")
            print("Press any key to continue . . .")
            input()
            break
        
        print()  # Add blank line between entries


if __name__ == "__main__":
    main()