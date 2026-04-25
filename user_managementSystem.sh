#!/bin/bash

users=("admin" "John" "guest")

#function to view users
view_users() {
    for user in "${users[@]}"
    do
    echo "User: " "${user[@]}"
    done
   
}

#function to add new users
add_user(){
    read -p "Add new user: " new_user
    users+=("$new_user") 
    echo "User added!"
}

#function to search for user
search_user(){
    read -p "What is the username to search? " username
    found=0

    #looping through to search for a user
    for name in "${users[@]}"
    do
      if [[ "$name" == "$username" ]] #user for matching name
      then
      found=1
      break
      fi
    done

         if [[ $found -eq 1 ]]
         then
           echo "User found!"
        else
           echo "User not found!"
         fi
}

count_users(){
    echo "There are: " "${#users[@]}" "users"
}

store_file(){
 printf "%s\n" "${users[@]}" > file.txt #print each element of the array on a new line and saves it
   echo "Users stored in a txt file!" 
}

view_file(){
   code file.txt
}

echo "===== USER MANAGEMENTSYSTEM SYSTEM ====="
echo "1. View all users"
echo "2. Add a user"
echo "3. Search for a user"
echo "4. Count users"
echo "5. Store to text file"
echo "6. View text file"
echo "7. Exit"

while true 
do
read -p "Make a choice: " choice

case "$choice" in
   1) 
   view_users ;;
   2)
   add_user ;;
   3) 
   search_user ;;
   4)
   count_users ;;
   5)
   store_file ;;
   6)
   view_file ;;
   7)
   echo "Thank you for using the system."
   break ;;
   *)
   echo "Invalid option" ;;
esac
done