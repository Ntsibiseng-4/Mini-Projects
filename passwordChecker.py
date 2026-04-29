#Login user system

users = {"usernames": ["Kamogelo", "Tebogo", "Nyakallo", "Hellen", "Dimakatso"],
         "password": ["kamo09", "LeshTebo", "Theka", "mahlaHell", "DimaLes"]}

passingWord = input("Enter the password: ")

if passingWord in users["password"]: #check if the password exist in the list
    idx = users["password"].index(passingWord) #find the position (index) of the password
    name = users["usernames"][idx] #use the same index to find the corresponding name
    
    print("Access granted!")
    print(f"Welcome back {name}")
    
else:
    usingName = input("Password incorrect. Enter your username: ")
    
    if usingName in users["usernames"]:
        idx = users["usernames"].index(usingName)
        newPassword = input("Enter a new password: ")
        users["password"][idx] = newPassword #Update only the password at that specific index
        print("Password Changed!")
    else:
        print("Access denied!")