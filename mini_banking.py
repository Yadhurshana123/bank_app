#{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}

user_ids = []
transaction_history=[]
balance=0
account_number=[]
account_details=[]

import getpass

def create_customer():
    user_name = input("Enter your new user name: ")
    pass_word = getpass.getpass("Enter your new password: ")
    nic = input("Enter your NIC number: ")
    user_ID = input("Enter your user ID: ")
    address = input("Enter your address: ")
    t_no = input("Enter your phone number: ")
    birth_date = input("Enter your birth date: ")

    user_ids.append(user_ID)

    return (user_name, pass_word, nic, user_ID, address, t_no, birth_date)

customers = create_customer()

with open("customers.txt", "a") as customer_file:
    customer_file.write(",".join(customers) + "\n")

print("Customer created successfully! Now you're a customer of Unicom TIC Bank.")
print("Hi", customers[0], "! Welcome to Unicom TIC mini banking system.")




    # customer = open('customer.txt' , 'a')
    # customer.write(f"{user_name}\t")
    # customer.write(f"{pass_word}\t" )
    # customer.write(f"{user_ID}\t" )
    # customer.write(f"{nic}\t" )
    # customer.write(f"{address}\t" )
    # customer.write(f"{t_no}\t" )
    # customer.write(f"{birth_date}\t" )
    # customer.write("\n")
    # customer.close()
    
    
#{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}

def create_account():
            entered_user_ID=input("enter your userID :")
            if entered_user_ID in range:
                ac_number = input("Enter account number :")
                holder_name = input("Enter account holder name :")
                Balance = input("Enter Initial balance :$")
                print("Account created successful!")
            else:
                print("User not found.Try again")
            account_number.append(ac_number)

#{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}

def deposit():
    try:
        amount = int(input("Enter your deposit amount : $"))
        global balance
        balance += amount
        print(f"Your available balance is : $",balance)
    except ValueError:
        print("You must enter a number only")

#{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}

def withdraw():
    try:
        global balance
        with_draw = int(input(f"Enter withdraw amount :$"))
        if balance > with_draw and with_draw > 0:
            balance -= with_draw
            print(f"Your available balance is:$",balance)
    except ValueError:
        print("You must enter a number only")

#{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}

def transaction_History():
    transaction_history.append(f"Deposit : {amount}") 
    transaction_history.append(f"Withdraw : {with_draw}") 

#{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{[{{{{}}}}]}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}

def del_account():
    delete_account = input("Enter account to delete: ")
    if delete_account in account_number:
        del account_number[delete_account]
        print(f"Admin deleted {delete_account}account.With customer permission")
    else:
        print("Account not found.")

#{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}
admin_username = "Unicomtic"
admin_password = "Uni123"
admin_userID = "A001"

while True :
    try:
        login = input("Enter your Role(Admin or Customer) :")
        if login == "Admin":
            user_name = input("Enter your user name : ")
            pass_word = input("Enter your password : ")
            user_ID = input("Enter your user ID : ")

            if user_name == admin_username and pass_word == admin_password and user_ID == admin_userID:
                print("Login Successful!")
                print(" Hi", user_name ,"! Welcome Admin")
                break
            
            else:
                print("Invalid input.Try again!")

                user= open('users.txt' , 'w')
                user.write(f"{user_name}\t")
                user.write(f"{pass_word}\t" )
                user.write(f"{user_ID}\t" )
                user.write("\n")
                user.close()
                

#{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}

        elif login == "Customer":
            while True:
                print(" ====MENU====")
                print("1. Deposit Money")
                print("2. Withdraw Money ")
                print("3. Check Balance ")
                print("4. Transaction History ")
                print("5. Account Details")

                print("6. Exit ")
            
                choice = input("Enter your choice(1-6) : ")
    
                if choice == "1":
                    deposit()

                elif choice == "2":
                    withdraw()

                elif choice == "3":
                    print("Your available balance is : $",balance)

                elif choice == "4":
                    transaction_History()

                elif choice == "5":
                    acNumber = input("Enter your account number :")
                    if acNumber in account_number:
                        account_details[account_number]={"Holoder Name":user_name,"User ID":user_ID,"Birth Date":birth_date,"NIC":nic,"Address":address,"Telephone Number":t_no,"Balance Amount":balance}
                        print(account_details)
                    else:
                        print("User Not Found....")

                elif choice == "6":
                    exit()

                else:
                    print("Invalid input. Try again")

    except TypeError:
            print("Invalid input. Try again")


#{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}

while True :
    print(" ====MENU====")
    print("1. Create customer ")
    print("2. Create Account ")
    print("3. Deposit Money")
    print("4. Withdraw Money ")
    print("5. Check Balance ")
    print("6. Transaction History ")
    print("7. Account Details")
    print("8. Delete Account")
    print("9. Exit ")

    choice = input("Enter your choice(1-9) : ")
    if choice == "1":
        create_customer()

    elif choice == "2":
        create_account()

    elif choice == "3":
        deposit()

    elif choice == "4":
        withdraw()

    elif choice == "5":
        print("Your available balance is : $",balance)

    elif choice == "6":
        transaction_History()

    elif choice == "7":
        acNumber = input("Enter your account number :")
        if acNumber in account_number:
           account_details[account_number]={"Holoder Name":user_name,"User ID":user_ID,"Birth Date":birth_date,"NIC":nic,"Address":address,"Telephone Number":t_no,"Balance Amount":balance}
           print(account_details)
        else:
            print("Account Not Found....")
            
    elif choice == "8":
        del_account()

    elif choice == "9":
        exit()

#{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}