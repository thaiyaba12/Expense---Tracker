expenses = []

def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    expenses.append((category, amount))
    print("Expense added.\n")

def view_expenses():
    if not expenses:
        print("No expenses yet.\n")
        return
    for category, amount in expenses:
        print(f"{category} - ₹{amount}")
    print()

def view_total():
    total = sum(amount for _, amount in expenses)
    print(f"Total spent: ₹{total}\n")

while True:
      print("1. Add Expense")
      print("2. View Expenses")
      print("3. View Total")
      print("4. Exit")

      choice = input("Enter your choice (1–4): ")

      if choice == "1":
          add_expense()
      elif choice == "2":
          view_expenses()
      elif choice == "3":
          view_total()
      elif choice == "4":
         print("Goodbye!")
         break
      else:
        print("Invalid choice. Try again.\n")