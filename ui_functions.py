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
        check = dbms.check_valid_username(username, password)


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

def profile():
    print('welcome to your profile! Here is your information: ')
