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
        users.append(user_info())
        print("user added successfully!")
    elif choice=="2":
        clear_terminal()
        if users:
            print("displaying all users....")
            for I in users:
                I.display_users()    
        else:
            print("sorry,we didn't found anything to display for you")       
    elif choice=="3":
        print("exiting....")    
        break
    else:
        print("invalid choice, please choice between 1 and 3")        
        
           