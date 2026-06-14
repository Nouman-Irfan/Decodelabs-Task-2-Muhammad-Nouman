# Import datetime module
# Used to store current date and time of expense
from datetime import datetime


# File name used to store expenses permanently
file_name = "expenses.txt"


# =========================================
# FUNCTION: ADD EXPENSE
# This function takes expense details
# from user and saves them in file
# =========================================

def add_expense():

    print("\n========== ADD EXPENSE ==========")

    # Take category input from user
    category = input("Enter category: ")

    # Take expense amount input from user
    user_input = input("Enter expense amount: ")

    try:

        # Convert input into decimal number
        amount = float(user_input)

        # Validation check
        # Expense amount must be greater than 0
        if amount <= 0:

            print("Expense amount must be greater than 0.")

        else:

            # Get current date and time
            date_time = datetime.now().strftime("%d-%m-%Y %I:%M %p")

            # Open file in append mode
            # Append mode adds new data without deleting old data
            with open(file_name, "a") as file:

                # Save expense in file
                # Format:
                # category,amount,date_time
                file.write(category + "," +
                           str(amount) + "," +
                           date_time + "\n")

            print("Expense added successfully!")

    # Handle invalid input
    except ValueError:

        print("Invalid amount! Please enter numbers only.")


# =========================================
# FUNCTION: VIEW EXPENSES
# This function reads and displays
# all expenses from file
# =========================================

def view_expenses():

    print("\n========== EXPENSE HISTORY ==========")

    try:

        # Open file in read mode
        with open(file_name, "r") as file:

            # Read all lines from file
            lines = file.readlines()

        # Check if file is empty
        if len(lines) == 0:

            print("No expenses found.")

        else:

            # Expense counter variable
            expense_number = 1

            # Loop through each line in file
            for line in lines:

                # Remove extra spaces/newline
                line = line.strip()

                # Ignore empty lines
                if line != "":

                    # Split data using comma
                    data = line.split(",")

                    # Check if data format is correct
                    if len(data) == 3:

                        # Store separated values
                        category = data[0]
                        amount = float(data[1])
                        date_time = data[2]

                        # Display expense details
                        print("Expense", expense_number)
                        print("Category:", category)
                        print("Amount: Rs",
                              format(amount, ".2f"))
                        print("Date/Time:", date_time)

                        print("--------------------------")

                        # Increase expense number
                        expense_number = expense_number + 1

    # Handle missing file
    except FileNotFoundError:

        print("No expenses found yet.")


# =========================================
# FUNCTION: SHOW SUMMARY
# This function calculates:
# - Total Expenses
# - Number of Expenses
# - Average Expense
# - Highest Expense
# =========================================

def show_summary():

    # Variable to store total expenses
    total = 0

    # Variable to count expenses
    count = 0

    # Variable to store highest expense
    highest = 0

    # Variable to store category
    # of highest expense
    highest_category = ""

    try:

        # Open file in read mode
        with open(file_name, "r") as file:

            # Read file line by line
            for line in file:

                # Remove extra spaces/newline
                line = line.strip()

                # Ignore empty lines
                if line != "":

                    # Split data using comma
                    data = line.split(",")

                    # Check valid format
                    if len(data) == 3:

                        category = data[0]

                        amount = float(data[1])

                        # Add amount into total
                        total = total + amount

                        # Increase expense count
                        count = count + 1

                        # Find highest expense
                        if amount > highest:

                            highest = amount

                            highest_category = category

        print("\n========== EXPENSE SUMMARY ==========")

        # Display total expenses
        print("Total Expenses: Rs",
              format(total, ".2f"))

        # Display number of expenses
        print("Number of Expenses:", count)

        # Calculate average only if count > 0
        if count > 0:

            average = total / count

            print("Average Expense: Rs",
                  format(average, ".2f"))

            print("Highest Expense: Rs",
                  format(highest, ".2f"))

            print("Highest Category:",
                  highest_category)

        else:

            print("Average Expense: Rs 0.00")

            print("Highest Expense: Rs 0.00")

    # Handle missing file
    except FileNotFoundError:

        print("\nNo expenses found yet.")


# =========================================
# MAIN PROGRAM LOOP
# Displays menu repeatedly until
# user chooses Exit
# =========================================

while True:

    print("\n================================")
    print("       EXPENSE TRACKER")
    print("================================")

    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Expense Summary")
    print("4. Exit")

    # Take menu choice from user
    choice = input("\nEnter your choice: ")


    # =====================================
    # OPTION 1: ADD EXPENSE
    # =====================================

    if choice == "1":

        add_expense()


    # =====================================
    # OPTION 2: VIEW EXPENSES
    # =====================================

    elif choice == "2":

        view_expenses()


    # =====================================
    # OPTION 3: SHOW SUMMARY
    # =====================================

    elif choice == "3":

        show_summary()


    # =====================================
    # OPTION 4: EXIT PROGRAM
    # =====================================

    elif choice == "4":

        print("\nProgram Closed Successfully.")

        break


    # =====================================
    # INVALID MENU OPTION
    # =====================================

    else:

        print("Invalid Choice! Please select 1, 2, 3, or 4.")