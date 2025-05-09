
first_account_number = 1000

def generate_account_number():
    global first_account_number
    first_account_number += 1
    return f"ACC{first_account_number}"

def create_account():
    entered_user_ID = input("Enter your userID: ")
    if entered_user_ID in []
    ac_number = generate_account_number(account_details[1])  
    holder_name = input("Enter account holder name: ")
    initial_balance = float(input("Enter Initial balance: $"))
    print("Account created successfully!")

    with open('account_details.txt', 'a') as details_file:
        details_file.write(f"{holder_name}\t{ac_number}\t{initial_balance}\n")

    with open('transfer.txt', 'a') as transfer_file:
        transfer_file.write(f"{ac_number}\t")
create_account()