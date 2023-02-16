from stdiomask import getpass 
import hashlib
import os

clear = lambda: os.system('cls')

def main():
    clear()
    print("Main Menu")
    print("---------")
    print()
    print("Aircraft Maintenance Program")
    print()
    while True:
        print()
        userChoice = input("Choose an option: ")
        if userChoice in ['1', '2']:
            break
    if userChoice == '1':
        Register()
    else:
        Login()
    # while True:
    #     print()
    #     userChoice = input("Please press 1 to login ")
    #     if userChoice == '1':
    #         break
    # if userChoice == '1':
    #     Login()

def Register():
    clear()
    print("Register")
    print("--------")
    print()
    while True:
        userName = input("Enter Your Name: ").title()
        if userName != '':
            break
    userName = sanitizeName(userName)
    while True:
        userPassword = getpass("Enter Your Password: ")
        if userPassword != '':
            break
    while True:
        confirmPassword = getpass("Confirm your Password: ")
        if confirmPassword == userPassword:
            break
        else:
            print("Password Don't Match")
            print()
    while True:
        admin = input("Enter 1 if this is an admin. Enter 0 otherwise: ")
        if admin == "1" or admin == "0":
            break
        else:
            print("Error, please enter 1 or 0")
    p = userAlreadyExist(userName, userPassword)
    while p == True:
        print()
        error = input("You Are Already Registered. \n\nPress (T) to try again:\nPress (L) to Login: ").lower()
        if error == "t":
            Register()
            return
        elif error == "l":
            Login()
    addUserInfo([userName, hash_password(userPassword), admin])


def Login():
    clear()
    print("Login")
    print("-----")
    print()
    usersInfo = {}
    userAdminInfo = {}
    with open('userInfo.txt', 'r') as file:
        for line in file:
            line = line.split()
            usersInfo.update({line[0]: line[1]})
            userAdminInfo.update({line[0]: line[2]})

    while True:
        userName = input("Enter Your Name: ").title()
        userName = sanitizeName(userName)
        if userName not in usersInfo:
            print("You are not Registered")
            print()
        else:
            break
    while True:
        userPassword = getpass("Enter Your Password: ")
        if not check_password_hash(userPassword, usersInfo[userName]):
            print("Incorrect Password")
            print()
        else:
            break
    if isAdmin(userAdminInfo[userName]) == True:
        print()
        print("Logged In as Admin!")
    else:
        print()
        print("Logged In!")

def addUserInfo(userInfo: list):
    with open('userInfo.txt', 'a') as file:
        for info in userInfo:
            file.write(info)
            file.write(' ')
        file.write('\n')

def userAlreadyExist(userName, userPassword):
    userPassword = hash_password(userPassword)
    usersInfo = {}
    with open('userInfo.txt', 'r') as file:
        for line in file:
            line = line.split()
            if line[0] == userName and line[1]== userPassword:
                usersInfo.update({line[0]: line[1]})
    if usersInfo == {}:
        return False
    return usersInfo[userName] == userPassword
        

def sanitizeName(userName):
    userName = userName.split()
    userName = '-'.join(userName)
    return userName

def hash_password(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

def check_password_hash(password, hash):
    return hash_password(password) == hash

def isAdmin(admin):
    if admin == "1":
        return True
    else:
        return False


main()