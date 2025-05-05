with open("customers.txt", "a") as customer_file:
    customer_file.write(",".join(customers) + "\n")
with open("users.txt","a") as users_file:
    