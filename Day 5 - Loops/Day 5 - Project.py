# Stock Management System
def validate_number_input(prompt):
    """Ensure user inputs a valid positive number."""
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a positive number.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")


def start_system():
    """Handle program initiation with proper user confirmation."""
    while True:
        user_decision = input("Do you want to start the program? (yes/no): ").lower()
        if user_decision == 'yes':
            print("\nWelcome to your Stock Management System!")
            print("----------------------------------------")
            return True
        elif user_decision == 'no':
            print("Exiting program...")
            exit()
        else:
            print("Invalid input. Please answer 'yes' or 'no'.")


def run_stock_operations():
    """Main stock management logic with proper validation."""
    print("\nStock Input")
    print("-----------")
    total_stock = validate_number_input("Enter total stock quantity: ")
    minimum_stock = validate_number_input("Enter minimum required stock: ")

    while True:
        print("\nStock Operations")
        print("----------------")
        stock_to_remove = validate_number_input("Enter quantity to remove (or 0 to exit): ")

        if stock_to_remove == 0:
            print("Operation canceled.")
            break

        if stock_to_remove > total_stock:
            print(f"Error: Cannot remove more than available stock ({total_stock}).")
            continue

        remaining_stock = total_stock - stock_to_remove
        total_stock = remaining_stock  # Update stock for next operation

        if remaining_stock <= minimum_stock:
            print(f"\n⚠️ Warning: Low stock alert! ⚠️")
            print(f"Remaining stock: {remaining_stock}")
            print(f"Minimum required: {minimum_stock}")
            print("Please order more inventory immediately!")
        else:
            print(f"\nStock status: OK")
            print(f"Remaining stock: {remaining_stock}")
            print(f"Minimum required: {minimum_stock}")

        # Option to continue operations
        if input("\nPerform another operation? (yes/no): ").lower() != 'yes':
            print("\nFinal Stock Report")
            print("------------------")
            print(f"Total remaining stock: {total_stock}")
            print(f"Minimum required stock: {minimum_stock}")
            if total_stock <= minimum_stock:
                print("Status: ❌ ORDER MORE INVENTORY")
            else:
                print("Status: ✅ Stock sufficient")
            break


if __name__ == "__main__":
    if start_system():
        run_stock_operations()