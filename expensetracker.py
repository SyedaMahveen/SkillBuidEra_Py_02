expenses = []

def add_expense():
    date = input("Enter Date (YYYY-MM-DD): ")
    category = input("Enter Category: ")
    amount = float(input("Enter Amount: "))

    expenses.append([date, category, amount])

    print("Expense added successfully!")

def view_expenses():
    print("\n--- Expense Records ---")

    if not expenses:
        print("No expenses recorded.")
        return

    for expense in expenses:
        print(f"Date: {expense[0]}, Category: {expense[1]}, Amount: ₹{expense[2]}")

def generate_report():
    if not expenses:
        print("No expenses available.")
        return

    total = sum(expense[2] for expense in expenses)

    print("\n--- Expense Report ---")
    print(f"Total Expenses: ₹{total:.2f}")

while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Generate Report")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        generate_report()

    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice.")
