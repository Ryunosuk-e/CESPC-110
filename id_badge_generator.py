print("Please enter the following information: ") 

first_name = input("First name: ")
last_name = input("Last name: ")
email_address = input("Email address: ")
phone_number = input("Phone number: ")
job_title = input("Job Title: ")
id_number = input("ID Number: ")
print()


print("The ID Card is:")
print("------------------------------------------------------------")
print(f"{last_name.upper()} , {first_name}")
print(f"{job_title.title()}")
print(f"ID: {id_number}")
print()
print(email_address.lower())
print(phone_number)
print("------------------------------------------------------------")

