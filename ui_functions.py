from db_functions import *

#creates a database object that interacts with the tables
dbms = Petr_dbms()

#sign in/login function
def sign_in_screen() -> int:
    """checks to see if the user wants to login or sign up"""
    log = None
    while log is None:
        check = input("Welcome to the Petr Trading App! Please type 'login' to login to your account or 'sign up' to create an account! ").strip()
        if check == 'login':
            return 2
        elif check == 'sign up':
            return 3


#login function
def login() -> int:
    """tries to log the user in with the given username and password"""
    logged_in = False
    while not logged_in:
        print('\nWelcome back! Please enter your username and password')
        user_name = input("username (or enter 'back' to go back): ")
        if user_name == 'back':
            return 1
        password = input("password: ")
        logged_in = dbms.check_login_credentials(user_name, password)
    return 4


#sign up functions
def sign_up()->int | float:
    """checks to make sure the username given is not already being used, returns the given username"""
    check = False
    while not check:
        print("\nWe're glad you want to sign up! PLease create a username and password")
        username = input("Create your username (or enter 'back' to go back): ").strip()
        if username == 'back':
            return 1
        password = input("Create your password: ").strip()
        check = dbms.check_valid_username(username,password)
    return 3.5

def get_more_info() -> int:
    """gets more information about the user after creating their account"""
    print("\nThank you for creating your account! Lets get to know each other better")
    f_name = input("What is your first name? ").strip().capitalize()
    l_name = input("What is your last name? ").strip().capitalize()
    grade = input("What is your graduation year (ie: 2024, 2025, alumni)? ").strip()
    dbms.update_new_info(f_name, l_name, grade)
    return 4


#homescreen functions
def home_screen()->int:
    """simulates the home screen for the user"""
    print("\nwhere would you like to go?")
    print("type 'profile' to view and update your profile, type 'trades' to view the current trading board, or type logout' to logout")
    choice = input("please enter your choice: ")
    if choice == 'profile':
        return 5
    elif choice == 'logout':
        print(f'goodbye {dbms._username}, see you again soon!')
        print()
        return 1


#view profile functions
def view_profile()->int | float:
    """prints the information of the user"""
    info = dbms.get_profile_info()
    print('\nwelcome to your profile! Here is your information: ')
    print(f'username: {info[0]}')
    print('password: ' + '*'*len(info[1]))
    print(f'first name: {info[2]}')
    print(f'last name: {info[3]}')
    print(f'graduation year: {info[4]}')
    print(f'petr? {info[5]}')
    print(f'last trade date: {info[6]}')
    print(f'favorite petr: {info[7]}')

    while True:
        choice = input("type 'update' to update your profile, or 'back' to go back to the home screen: " )
        if choice == 'update':
            return 5.5
        elif choice == 'back':
            return 4


#update profile functions
def update_profile()->int:
    """allows the user to update their information"""
    while True:
        choice = input("\ntype 'username' to change your username,"
                       "\n'first_name' or 'last_name' to change your name,"
                       "\n'password' to change your password,"
                       "\n'year' to change your graduation year,"
                       "\n'favorite_petr' to change your favorite petr,"
                       "\nor 'back' to go back: ")
                       # "\nor 'save' to save your changes: ")

        if choice == 'first_name' or choice == 'last_name' or choice == 'year' or choice == 'favorite_petr':
            profile_update_choice(choice)

        elif choice == 'username':
            profile_update_username()

        elif choice == 'password':
            profile_update_password()

        elif choice == 'back':
            return 5

def profile_update_choice(type_data)->None:
    """updates different information for the user"""
    data = input(f'Please enter your new {type_data}: ')
    dbms.update_info(type_data, data.capitalize())
    print(f'your {type_data} has been updated to {data}!')

def profile_update_username()->None:
    """updates the user's username"""
    check = False
    while not check:
        print()
        new_username = input('Please enter your new username: ')
        check = dbms.update_username(new_username)

    print(f'your username has been updated to {new_username}')

def profile_update_password()->None:
    """updates the user's password"""
    check = False
    while not check:
        print()
        old_password = input('Please enter your old password: ')
        new_password = input('Please enter your new password: ')
        new_password1 = input('Please enter your new password again: ')
        if new_password != new_password1:
            print('the new passwords do not match')
        else:
            check = dbms.update_password(old_password, new_password)
    print('your password has been updated to '+'*'*len(new_password)+'!')