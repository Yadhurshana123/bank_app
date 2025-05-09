import getpass

user_ids = []
balance = 0
account_details=[]

def create_customer():
    user_name = input("Enter customer user name: ")
    pass_word = getpass.getpass("Enter customer new password: ")
    nic = int(input("Enter customer NIC number: "))
    user_ID = input("Enter customer user ID: ")
    address = input("Enter customer address: ")
    t_no = int(input("Enter customer phone number: "))
    birth_date = input("Enter customer birth date: ")

    user_ids.append(user_ID)

    with open("customers.txt", "a") as customer_file:
        customer_file.write(f"{user_name}\t{pass_word}\t{nic}\t{user_ID}\t{address}\t{t_no}\t{birth_date}\n")


    print("Customer created successfully! Now you're a customer of Unicom TIC Bank.")
    print("Hi", user_name, "! Welcome to Unicom TIC mini banking system.")


#{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}
def generat_account_number(account_details):
    if account_details:
        # Assuming accounts are formatted as 'ACC<Number>' and you want the next available number
        max_acc_number = max(int(acc[3:]) for acc in account_details)
        return f"ACC{max_acc_number + 1}"
    return "ACC1001"

def create_account():
    entered_user_ID = input("Enter your userID: ")
    if entered_user_ID in user_ids: 
        ac_number = generat_account_number(account_details)  # Generates a new account number
        holder_name = input("Enter account holder name: ")
        initial_balance = float(input("Enter Initial balance: $"))
        print("Account created successfully!")

        with open('account_details.txt', 'a') as details_file:
            details_file.write(f"{holder_name}\t{ac_number}\t{initial_balance}\n")

        with open('transfer.txt', 'a') as transfer_file:
            transfer_file.write(f"{ac_number}\t")

    else:
        print("User not found. Try again.")

    
    
#{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}

def create_admin():
    print("1. yes")
    print("2. no")
    confirm =input("You want to create another admin :").lower()

    if confirm == "yes":
        user_name = input("Enter new admin name: ").strip()
        pass_word = input("Enter new admin password: ").strip()
        user_ID = input("Enter new admin user ID: ").strip()
        print(f"{user_name} is a new admin of UnicomTIC bank")
        with open("users.txt", "a") as user_file:
            user_file.write(f"{user_name}\t{pass_word}\t{user_ID}\n")
    elif confirm == "no":
        return
    else:
        print("Please kindly type yes or no")

#{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}


def view_all_customers():
    try:
        with open("customers.txt", "r") as customer_file:
            for line in customer_file:
                print(line)
    except FileNotFoundError:
        print("Customer Data Not found")           

#{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}


deposit=0
balance=0
def deposit():
    ac_number = float(input("Enter your account number : "))
    if ac_number not in account_details:
        print("Account not found")
        return
    try:
        amount = float(input("Enter your deposit amount : Rs."))
        if amount <=0 :
            print("Must be positive")
            return
    except ValueError:
        print("Invalid amount")
        return

    account_details[ac_number]["balance"] += amount
    transaction_History.setdefault(ac_number,[]).append(f"deposited:{amount}")

    with open('transfer.txt', 'a') as transfer_file:
        transfer_file.write(f"Deposit Rs{amount}\t Withdraw Rs{withdraw}\n") 
    with open('account_details.txt', 'a') as details_file:
        details_file.write(f" Deposit Rs{amount}\t")
               
  

#{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}


withdraw = 0
def with_draw():
    global withdraw
    try:
        global balance
        withdraw = float(input("Enter withdraw amount : Rs."))
        if balance > withdraw and withdraw > 0:
            global initial_balance 
            balance += initial_balance 
            balance -= withdraw
            print("Your available balance is:$",balance)

            with open('transfer.txt', 'a') as transfer_file:
                transfer_file.write(f"Withdraw Rs{withdraw}\t Balance{balance}") 

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
            # Assuming each line in transfer.txt starts with the account number
            if line.startswith(acNumber):  # Check if the account number matches
                print(f"Transaction details for account {acNumber}: {line.strip()}")
                found = True
    
    if not found:
        print(f"No transactions found for account number: {acNumber}")


#{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}


def del_account():
    user_id = input("Enter your user ID : ")
    delete_account = input("Enter account to delete: ")
    if user_id in user_ids:
        if delete_account in account_details.txt:
            confirm = input("Are you sure you want to delete this account?(yes or no) : ")
            if confirm.lower() == "yes":
                account_details.remove(user_id)
                print(f"Admin deleted {delete_account}account.With customer permission")
            else:
                print("Delete option cancelled")
        else:
            print("Account Not Found")
    else:
        print("User ID Not Found")

#{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}

def account_Details():
    try:
        ac_number = input("Enter your account number :")

        with open('account_details.txt', 'r') as details_file:
            #found = False
            for details in details_file:
                info = details.strip().split()
                if ac_number == info[1]:
                    print(details)
                    #found = True
                    break
                else:
                    print("Account Not Found....")
    except FileNotFoundError:
        print("Customer Data Not Found")

    
#{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}


def admin_login():
    while True:
        user_name = input("Enter your user name: ").strip()
        pass_word = input("Enter your password: ").strip()
        user_ID = input("Enter your user ID: ").strip()

        with open("users.txt", "r") as user_file:
            for user in user_file:
                user_details = user.strip().split() 
                if user_name == user_details[0] and pass_word == user_details[1] and user_ID == user_details[2]:
                    print("Login Successful!")
                    print(f"Hi {user_name}, Welcome Admin")
                    admin_menu()
                    return
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
        print("5. Delete Account")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            create_customer()
        elif choice == "2":
            create_account()
        elif choice == "3":
            create_admin()
        elif choice == "4":
            view_all_customers()
        elif choice == "5":
            del_account()
        elif choice == "6":
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
            print("Your available balance is: $", balance)
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
            confirmation = input("Are you sure(yes or no):").lower()
            if confirmation == "yes":
                admin_login()
            else:
                continue
        elif role == "2":
            confirmation = input("Are you sure(yes or no):").lower()
            if confirmation == "yes":
                customer_login()
            else:
                break  
        else:
            print("Invalid input. Please choose 1 or 2")
            break
login()

#{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}