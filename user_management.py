import time
import os
print("welcome to user management\n\n")
class User:
    def __init__(self,first_name,last_name,email,password,status="inactive"):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.password=password
        self.status=status
    def display_users(self):
        print("displaying all users....")
        time.sleep(2)
        print(f"first name:{self.first_name}")
        print(f"last name:{self.last_name}")
        print(f"email:{self.email}")
        print(f"password:{self.password}")
        print(f"status:{self.status}")
        print("----------------")
def user_info():
    First_name=input("enter the first name:")
    Last_name=input("enter the last name:")
    Email=input("enter your email:")
    Password=input("enter your password:")
    print("user added successfully!")
    return User(First_name,Last_name,Email,Password)
def clear_terminal():
    os.system("cls") if os.name=="nt" else os.system("clear")
while True:
    users=[]
    print("choose an Action:\n")
    print("1. Add new user")
    print("2. Display all users")
    print("3. Exit")
    choice=input("enter your choice:")
    if choice=="1":
        user_profile=user_info()
        users.append(user_profile)
    elif choice=="2":
        clear_terminal()
        user_profile.display_users()           
    elif choice=="3":
        break
    else:
        print("invalid choice, please choice between 1 and 4")        
        
           