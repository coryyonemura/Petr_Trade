from db_functions import *

dbms = Petr_dbms()

def sign_in_screen() -> str:
    """checks to see if the user wants to log in or sign up"""
    log = None
    while log is None:
        check = input("Welcome to the Petr Trading App! Please type 'log in' to log in to your account or 'sign up' to create an account! ").strip()
        if check == 'log in':
            return 'l'
        elif check == 'sign up':
            return 's'

def login() -> str:
    """tries to log the user in with the given username and password"""
    logged_in = False
    while not logged_in:
        print('\nWelcome back! Please enter your username and password')
        user_name = input("username: ")
        password = input("password: ")
        logged_in = dbms.check_login_credentials(user_name, password)



def get_username_password()->str:
    """checks to make sure the username given is not already being used, returns the given username"""
    check = False
    while not check:
        print("\nWe're glad you want to sign up! PLease create a username and password")
        username = input("Create your username: ").strip()
        password = input("Create your password: ").strip()
        check = dbms.check_valid_username(username,password)


def get_more_info() -> None:
    """gets more information about the user after creating their account"""
    print("\nThank you for creating your account! Lets get to know each other better")
    f_name = input("What is your first name? ").strip().capitalize()
    l_name = input("What is your last name? ").strip().capitalize()
    grade = input("What is your graduation year (ie: 2024, 2025, alumni)? ").strip()
    dbms.update_new_info(f_name, l_name, grade)

def home_screen():
    print("\nwhere would you like to go?")
    print("type 'profile' to view and update your profile, type 'trades' to view the current trading board")
    choice = input("please enter your choice: ")
    if choice == 'profile':
        profile()

def profile():
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

    select_profile()

def profile_update_choice(type_data):
    data = input(f'Please enter your new {type_data}: ')
    dbms.update_info(type_data, data.capitalize())
    print(f'your {type_data} has been updated to {data}!')

def profile_update_username():
    check = False
    while not check:
        print()
        new_username = input('Please enter your new username: ')
        check = dbms.update_username(new_username)

    print(f'your username has been updated to {new_username}')

def profile_update_password():
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
def select_profile():
    choice = input("\ntype 'username' to change your username,"
                   "\n'first_name' or 'last_name' to change your name,"
                   "\n'password' to change your password,"
                   "\n'year' to change your graduation year,"
                   "\nor 'favorite_petr' to change your favorite petr: ")
                   # "\nor 'save' to save your changes: ")

    if choice == 'first' or choice == 'last' or choice == 'year' or choice == 'favorite_petr':
        profile_update_choice(choice)

    elif choice == 'username':
        profile_update_username()

    elif choice == 'password':
        profile_update_password()


