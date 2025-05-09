import getpass

balance = 0

def create_customer():
    user_name = input("Enter customer user name: ")
    pass_word = getpass.getpass("Enter customer new password: ")
    nic = int(input("Enter customer NIC number: "))
    user_ID = input("Enter customer user ID: ")
    address = input("Enter customer address: ")
    t_no = int(input("Enter customer phone number: "))
    birth_date = input("Enter customer birth date: ")


    with open("customers.txt", "a") as customer_file:
        customer_file.write(f"{user_ID} \t {user_name}\t{pass_word}\t{nic}\t{address}\t{t_no}\t{birth_date}\n")


    print("Customer created successfully! Now you're a customer of Unicom TIC Bank.")
    print("Hi", user_name, "! Welcome to Unicom TIC mini banking system.")


#{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}


def generat_account_number(account_details):
    if account_details:
        max_acc_number = max(int(acc[3:])for acc in account_details)
        return f"ACC{max_acc_number + 1}" 
        return 

def create_account():
    entered_user_ID = input("Enter your userID: ")
    if entered_user_ID in user_ids: 
        ac_number = generat_account_number(account_details) 
        holder_name = input("Enter account holder name: ")
        initial_balance = float(input("Enter Initial balance :Rs."))
        print("Account created successfully!")

        with open('account_details.txt', 'a') as details_file:
            details_file.write(f"{holder_name}\t{ac_number}\t{initial_balance}\n")

        with open('transfer.txt', 'a') as transfer_file:
            transfer_file.write(f"{ac_number}\t {initial_balance}\n")

    else:
        print("User not found. Try again.")

    
    
#{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}

def create_admin():
    user_name = input("Enter new admin name: ").strip()
    pass_word = input("Enter new admin password: ").strip()
    user_ID = input("Enter new admin user ID: ").strip()
    print(f"{user_name} is a new admin of UnicomTIC bank")
    with open("users.txt", "a") as user_file:
        user_file.write(f"{user_name}\t{pass_word}\t{user_ID}\n")
    
#{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}


def view_all_customers():
    try:
        with open("customers.txt", "r") as customer_file:
            for line in customer_file:
                print(line)
    except FileNotFoundError:
        print("Customer Data Not found")           

#{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}



def deposit():
    ac_number = input("Enter your account number: ").strip()

    try:
        amount = float(input("Enter your deposit amount: Rs."))
        if amount <= 0:
            print("Amount must be positive.")
            return
    except ValueError:
        print("Invalid amount.")
        return

    account_details[ac_number]["balance"] += amount
    transaction_History.setdefault(ac_number, []).append(f"Deposited: Rs.{amount}")

    with open('transfer.txt', 'a') as transfer_file:
        transfer_file.write(f"{ac_number}\t {amount}\n")

    with open('account_details.txt', 'a') as details_file:
        details_file.write(f"Deposit Rs{amount}\n")

    print(f"Rs.{amount} deposited successfully into account {ac_number}.")


#{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}


def with_draw():
    try:
        global balance
        withdraw = float(input("Enter withdraw amount : Rs."))
        if balance > withdraw and withdraw > 0:
            global initial_balance 
            balance += initial_balance 
            balance -= withdraw
            print("Your available balance is: Rs.",balance)

            with open('transfer.txt', 'a') as transfer_file:
                transfer_file.write(f"{ac_number}\t {amount}\n")

            with open('account_details.txt', 'a') as details_file:
                details_file.write(f"Withdraw Rs{withdraw}\n")  

        else:
            print("Insufficient Funds. Check balance")
    except ValueError:
        print("You must enter a number only")

#{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}

def transaction_History():
    acNumber = input("Enter your account number: ")
    
    found = False
    with open('transfer.txt', 'r') as transfer_file:
        for line in transfer_file:
            if line.startswith(acNumber):  
                print(f"Transaction details for account {acNumber}: {line.strip()}")
                found = True
    
    if not found:
        print(f"No transactions found for account number: {acNumber}")


#{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}

def admin_login():
    while True:
        admin_name = "Admin"
        admin_password = "Admin123"
        admin_id = "A001"
        
        print("enter 1for crerate admin or enter 2 for existing admin")

        option  = input("choose an option")

        if option == "1":
            user_name = input("Enter your user name: ").strip()
            pass_word = input("Enter your password: ").strip()
            user_ID = input("Enter your user ID: ").strip()

            if user_name == admin_name and pass_word == admin_password and user_ID == admin_id :
                print("Login Successful!")
                print(f"Hi {user_name}, Welcome Admin")
                admin_menu() 
                return

        elif option == "2":
            with open("users.txt", "r") as user_file:
                for user in user_file:
                    user_details = user.strip().split() 
                    if user_name == user_details[0] and pass_word == user_details[1] and user_ID == user_details[2]:
                        admin_menu()
        else: 
            print("Admin information is not correct.")
            break

#{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}


def customer_login():
    while True:
        user_name = input("Enter your user name: ").strip()
        pass_word = input("Enter your password: ").strip()
        user_ID = input("Enter your user ID: ").strip()

        with open("customers.txt", "r") as customer_file:
            for customer in customer_file: 
                customer_details = customer.strip().split() 
                if user_name == customer_details[0] and pass_word == customer_details[1] and user_ID == customer_details[3]:
                    print("Login Successful!")
                    print(f"Hi {user_name}, Welcome Customer")
                    customer_menu()
                    return
            print("Customer information is not correct. Try again.")
            break

#{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}


def admin_menu():
    while True:
        print("==== ADMIN MENU ====")
        print("1. Create Customer")
        print("2. Create Account")  
        print("3. Create New Admin")
        print("4. View All Customers")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            create_customer()
        elif choice == "2":
            create_account()
        elif choice == "3":
            create_admin()
        elif choice == "4":
            view_all_customers()
        elif choice == "5":
            print("Thank you for using Unicom TIC banking system.Good bye!")
            exit()
            break
        else:
            print("Invalid choice. Try again.")   

#{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}


def customer_menu():
    while True:
        print("==== CUSTOMER MENU ====")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Account Details")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            deposit()
        elif choice == "2":
            with_draw()
        elif choice == "3":
            print("Your available balance is: Rs.", balance)
        elif choice == "4":
            transaction_History()
        elif choice == "5":
            account_Details()
        elif choice == "6":
            print("Thank you for using Unicom TIC banking system.Good bye!")
            exit()
            break
        else:
            print("Invalid input. Try again.")       

#{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}


def login():
    while True:
        print("1. Admin")
        print("2. Customer")
        role = input("Enter your role (1 or 2): ")
        if role == "1":
            admin_login()
            return
        elif role == "2":
            customer_login()
            return
        else:
            print("Invalid input. Please choose 1 or 2")
            break
login()

#{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}