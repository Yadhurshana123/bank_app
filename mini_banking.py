import getpass

balance = 0

def generate_user_identy():
    user_id = 1
    count = 0
    with open("customers.txt", "r") as customer_file: 
        for line in  customer_file:
            count += 1 
            user_id += count 
        return user_id  

def create_customer():
    user_name = input("Enter customer name: ").strip()
    pass_word = getpass.getpass("Enter customer password: ").strip()
    nic = int(input("Enter customer NIC number: "))    
    address = input("Enter customer address: ").strip()
    t_no = int(input("Enter customer phone number: "))
    birth_date = input("Enter customer birth date: ")

    with open("customers.txt", "a") as customer_file:
        customer_file.write(f"{user_name}  ,  {pass_word}  ,  {nic}  ,  {address}  ,   {t_no}  ,   {birth_date} , ")

        user_ID =  generate_user_identy()
    with open("customers.txt", "a") as customer_file:
        customer_file.write(f"C0{user_ID}\n")


    print("Customer created successfully! Now",user_name,"is a customer of Unicom TIC Bank.")

    
#{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}


def generate_account_no():
    try:  
        acc_num = 1
        count = 0
        with open('accounts.txt', 'r') as details_file:
            for line in details_file:
                count += 1
                acc_num += count
        return acc_num  

    except FileNotFoundError:
        print("File not found")
        return 

def create_account():
    user_id = input("Enter customer userID:")
    with open("customers.txt", "r") as customer_file:
        for line in customer_file:
            ID = line.strip().split()
            if ID[-1] == user_id:

                holder_name = input("Enter account holder name: ")
                initial_balance = float(input("Enter Initial balance :Rs."))

                if initial_balance < 500:
                    print("Your amount must grater then Rs.500. Try again")

                else:
                    with open('accounts.txt', 'a') as details_file:
                        details_file.write(f"{holder_name} , {initial_balance} , ")
                        ac_number = generate_account_no() 
                    
                    with open('accounts.txt', 'a') as details_file:
                        details_file.write(f"ACC{ac_number}\n")

                    with open('transfer.txt', 'a') as transfer_file:
                        transfer_file.write(f"ACC{ac_number} , Balance Rs:{initial_balance}\n")

                    print("Account created successfully!")
                 #break
        else:
            print("User ID not found")


#{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}

def create_admin():
    user_name = input("Enter new admin name: ").strip()
    pass_word = input("Enter new admin password: ").strip()
    user_ID = input("Enter new admin user ID: ").strip()
    print(f"{user_name} is a new admin of UnicomTIC bank")
    with open("users.txt", "a") as user_file:
        user_file.write(f"{user_name} , {pass_word} , {user_ID}\n")
    
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
    try:
        ac_number = input("Enter your account number: ").strip()
        with open('accounts.txt', 'r') as details_file:
            for detail in details_file:
                ac_number= detail[1]
    except FileNotFoundError:
        print("Customer ID not found")
        return           
    try:
        amount = float(input("Enter your deposit amount: Rs."))
        if amount <= 0:
            print("Amount must be positive.")
            return
    except ValueError:
        print("Invalid amount.")
        return

    with open('transfer.txt', 'a') as transfer_file:
        transfer_file.write(f"ACC{ac_number} , Deposit Rs{amount}\n")

    with open('accounts.txt', 'a') as details_file:
        details_file.write(f"Deposit Rs{amount}\n")

    print(f"Rs.{amount} deposited successfully.")


#{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}


def with_draw():
    try:
        ac_number = input("Enter your account number: ").strip()
        with open('accounts.txt', 'r') as details_file:
            for detail in details_file:
                ac_number= detail[1]
    except FileNotFoundError:
        print("Customer ID not found")
        return    
    try:
        withdraw = float(input("Enter withdraw amount : Rs."))
        if balance < withdraw and withdraw < 0:
            print("Your available balance is not enough for withdraw.")
            return
    except ValueError:
        print("Invalid amount.")
        return
    
    with open('accounts.txt', 'a') as details_file:
        details_file.write(f"Withdraw Rs{withdraw}\n")  

    with open('transfer.txt', 'a') as transfer_file:
        transfer_file.write(f"Withdraw Rs{withdraw}\n")
    
    print(f"Rs.{withdraw} withdrawed successfully.")

           
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

#{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}

def account_details(account_number):
    try:
        with open('accounts.txt', 'r') as details_file:
            for line in details_file:
                data = line.strip().split()
                if data[-1] == account_number:
                    print(f"Account found!!. Name:{data[0]}\t Balance:{data[2]} \n ")

    except FileNotFoundError:
        print("File not found")

#{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}

def admin_login():
    try:
        while True:
            admin_name = "Admin"
            admin_password = "Admin123"
            admin_id = "A001"
            
            print("Enter 1 for default admin / Enter 2 for existing admin")

            option  = input("choose an option :")

            if option == "1":

                user_name = input("Enter your user name: ").strip()
                pass_word = input("Enter your password: ").strip()
                user_ID = input("Enter your user ID: ").strip()

                if user_name == admin_name and pass_word == admin_password and user_ID == admin_id :
                    print("Login Successful!")
                    print(f"Hi {user_name}, Welcome to Unicom TIC bank")
                    admin_menu() 
                    return

                else:
                    print("Admin information not correct")

            elif option == "2":
                user_name = input("Enter your user name: ").strip().lower()
                pass_word = input("Enter your password: ").strip()
                user_ID = input("Enter your user ID: ").strip()

                with open("users.txt", "r") as user_file:
                    for user in user_file:
                        user_details = user.strip().split()

                        if user_name in user_details and pass_word in user_details and user_ID in user_details:
                            print("Login Successful!")
                            print(f"Hi {user_name},Welcome to Unicom TIC bank")
                            admin_menu()
                            return
            else: 
                print("Please kindly choose 1 or 2")

    except FileNotFoundError:
        print("Admin data not found")                                               
        return
#{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}


def customer_login():
    while True:
        user_name = input("Enter your user name: ").strip()
        pass_word = input("Enter your password: ").strip()
        user_ID = input("Enter your user ID: ").strip()

        with open("customers.txt", "r") as customer_file:
            for customer in customer_file:
                customer_details = customer.strip().split()
                
                if user_name in customer_details and pass_word in customer_details and user_ID in customer_details:
                    print("Login Successful!")
                    print(f"Hi {user_name}, Welcome Customer")
                    customer_menu()  
                    return
                
                else:
                    print("Customer information is not correct. Try again.")

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
           print(f"Your available balance is,{balance}")
        elif choice == "4":
            transaction_History()
        elif choice == "5":
            acc_number = input("Enter your account number : ")
            account_details(acc_number)
        elif choice == "6":
            print("Thank you for using Unicom TIC banking system.Good bye!")
            exit()
            
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