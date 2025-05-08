import getpass

user_ids = []
transaction_history=[]
balance=0
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


def create_account():
    entered_user_ID=input("enter your userID :")
    if entered_user_ID in user_ids:
        ac_number = input("Enter account number :")
        holder_name = input("Enter account holder name :")
        initial_balance = float(input("Enter Initial balance: $"))
        print("Account created successfully!")
        global account_details
        account_details.append({
            "account_number": ac_number,
            "Holder name": holder_name,
            "Balance": initial_balance
        })
    
    else:
        print("User not found.Try again")

#{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}


def view_all_customers():
    try:
        with open("customers.txt", "r") as customer_file:
            for line in customer_file:
                print(line.strip())
    except FileNotFoundError:
        print("Customer Data Not found")           

#{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}


amount = 0
def deposit():
    global amount
    try:
        amount = int(input("Enter your deposit amount : $"))
        global balance
        balance += amount
        print(f"Your available balance is : $",balance)
    except ValueError:
        print("You must enter a number only")

#{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}


withdraw = 0
def with_draw():
    global withdraw
    try:
        global balance
        withdraw = int(input("Enter withdraw amount :$"))
        if balance > withdraw and withdraw > 0:
            balance -= withdraw
            print(f"Your available balance is:$",balance)
        else:
            print("Insufficient Funds. Check balance")
    except ValueError:
        print("You must enter a number only")

#{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}


def transaction_History():
    global amount
    global withdraw

    transaction_history.append(f"Deposit : {amount}") 
    transaction_history.append(f"Withdraw : {withdraw}") 

    with open('transfer.txt', 'r') as transfer_file:
        transfer_file.write(f"{account_number}\t Deposit Rs{deposit}\t Withdraw Rs{withdraw}\n")

#{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}


def del_account():
    user_id = input("Enter ypur user ID : ")
    delete_account = input("Enter account to delete: ")
    if user_id in user_ids:
        if delete_account in account_details:
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
    acNumber = input("Enter your account number :")
    if acNumber in account_details:
        account_details[account_number]={"Holoder Name":user_name,"User ID":user_ID,"Balance Amount":balance,"Deposit Rs":amount,"Withdraw Rs":withdraw}
        #print(account_details)

        with open('account_details.txt', 'a') as details_file:
            details_file.write(f"{user_name}\t{user_ID}\t{balance}\n Deposit RS{amount}\t Withdraw Rs{withdraw}\n")

    else:
        print("Account Not Found....")

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
        print("3. View All Customers")
        print("4. Check Balance")
        print("5. Delete Account")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            create_customer()
        elif choice == "2":
            create_account()
        elif choice == "3":
            view_all_customers()
        elif choice == "4":
           print("Your available balance is: $", 0)  
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