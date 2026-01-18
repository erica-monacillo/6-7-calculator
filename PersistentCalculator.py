=# ==================================
# Persistent Python Calculator
# ==================================

# -------- Member 2 START --------
# Subtract function



# -------- Member 3 START --------
# Multiply Function 
def multiply(a, b):
    return a * b


# -------- Member 4 START --------



# -------- Member 1 START --------
# Add function + persistent loop

def add(a, b):
    return a + b

def calculator():
    while True:
        print("\n--- Persistent Calculator ---")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Select (1-5): ")

        if choice == "5":
            print("Calculator closed.")
            break

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Numbers only.")
            continue

        if choice == "1":
            print("Result:", add(num1, num2))
        elif choice == "2":
            print("Result:", subtract(num1, num2))
        elif choice == "3":
            print("Result:", multiply(num1, num2))
        elif choice == "4":
            print("Result:", divide(num1, num2))
        else:
            print("Invalid choice.")

calculator()

# -------- Member 1 END --------


