print("=== WELCOME TO YOUR PROFILE SYSTEM ===")
name = input("What is your name? ")
age = int(input("How old are you? " ))
home = input("Where are you from? ")
subject = input("What is your favorite subject? ")
id = input("What is your student ID? ")
code = input("Do you love coding? (Yes/No) ").lower()
hobby1 = input("What is your first hobby? ")
hobby2 = input("Enter is your second hobby? ")

user_details = {"Name": name, "Age": age, "Home": home, "Subject": subject}

ans = True if code == "yes" else False
extra_details = [hobby1, hobby2, ans]

sens_details = (id)

ageStatus = age >= 18

print("\n===== USER PROFILE =====")
print(f"Name: {name}")
print(f"Age: {age}")

if ageStatus is True:
    print("Status: Adult")
else:
    print("Status: Minor")
    
print(f"Hometown: {home}")
print(f"Favorite Subject: {subject}")
print(f"Student ID: {id}")

print("\n Hobbies: ")
for hobby in extra_details[:-1]:
    print(f"- {hobby}")
    
print(f"\nLike Coding {extra_details[2]}")