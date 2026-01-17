# ==================================
# Persistent Python Calculator
# ==================================






PAG INPUT SA MO HERE ! HAYA COMMIT AND PUSH
ISA ISA LANG WITH NAME NNYO PARA MAKITA NKO SA CMMOMMIT HISTORY

Test-1 
# ----- Member 2 -------
# Subtract function
def subtract(a, b):
    return a - b


check kuno, sa main branch 



# ----- Member 1 -------
# Add function + persistent loop

def add(a, b):
    return a + b

# Add function * 
def multiply(a, b):
    return a * b

def calculator():
    while True:
        print("\n--- Presistent Calculator ---")
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
            pr
            int("Result:", add(num1, num2))
        elif choice == "2":
            print("Result:", subtract(num1, num2))
        elif choice == "3":
            print("Result:", multiply(num1, num2))
        elif choice == "4":
            print("Result:", divide(num1, num2))
        else:
            print("Invalid choice.")

calculator()

hello