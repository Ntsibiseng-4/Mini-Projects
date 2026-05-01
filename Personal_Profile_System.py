print("=== WELCOME TO YOUR PROFILE SYSTEM ===")
name = input("What is your name? ")
full_name = input("What is your full names? ")
age = int(input("How old are you? " ))
home = input("Where are you from? ")
subject = input("What is your favorite subject? ")
id = input("What is your student ID? ")
code = input("Do you love coding? (Yes/No) ").lower()
hobby1 = input("What is your first hobby? ")
hobby2 = input("Enter is your second hobby? ")

user_details = {"Name": name, "Age": age, "Home": home, "Subject": subject}
extra_details = [hobby1, hobby2, code]
sens_details = (full_name, id)

if age >= 18:
    print("User is an adult")
else:
    print("User is a minor")
    
answer = (code == "yes")
extra_details.append(answer[2])
