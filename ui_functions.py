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
    while True:
        print("\nwhere would you like to go?")
        print("type 'profile' to view and update your profile, type 'trades' to view the current trading board, or type logout' to logout")
        choice = input("please enter your choice: ")
        if choice == 'profile':
            return 5
        elif choice == 'trades':
            return 6
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
    print(f'last trade date: {info[6][0:11]}')
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
    dbms.update_info('users', type_data, data.capitalize(), 'username', dbms._username)
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


#trades functions
def trades_home_screen():
    print()
    while True:
        choice = input("welcome to the trade hub!"
                       "\nplease type 'past' to view past trades, "
                       "\n'post' to post a trade,"
                       "\n'view' to view the trading board,"
                       "\n'pending' to view current trades you are involved in,"
                       "\nor 'back' to go to the home screen: ")
        if choice == 'back':
            return 4
        elif choice == 'past':
            return 6.2
        elif choice == 'post':
            return 6.4
        elif choice == 'pending':
            return 6.6
        elif choice == 'view':
            return 6.8
        print()

def get_past_trade_data(data: list, position: int):
    """gets the data of the trades the user has participated in"""
    if data[position][2] == dbms._username:
        return data[position][3], data[position][0], data[position][1]
    else:
        return data[position][2], data[position][1], data[position][0]

def get_more_trades_option(position: int, len_data: int)->bool:
    """checks to see whether the user wants to view more trades"""
    while True:
        choice = input("type 'next' to view more trades or 'back' to go back: ")
        if choice == 'back':
            return False
        if choice == 'next' and position != len_data:
            return True
        elif choice == 'next' and position == len_data:
            print('these are all the trades you have completed')
            return False

def past_trades()->int:
    """displays the user's past trades in sets of five"""
    print('\nhere are your last five trades!')
    data = dbms.get_past_trades()
    for i in range(len(data)):
        traded_with, traded_petr, traded_for = get_past_trade_data(data, i)

        print(f'\ntraded with: {traded_with}'
              f'\ntraded petr: {traded_petr}'
              f'\ntraded for: {traded_for}'
              f'\ndate_traded: {data[i][4][0:11]}')

        if ((i+1)%5 == 0 and i != 0) or i == (len(data)-1):
            if get_more_trades_option(i, len(data)-1):
                pass
            else:
                break
    return 6

def post_trades()->int:
    """allows the user to post a trade"""
    trade_for = input("\nwhat petr are you looking for? (or type 'back' to go back): ")
    if trade_for == 'back':
        return 6
    trading_with = input('what petr(s) are you trading with?: ')
    description = input('add a description of the trade: ')
    dbms.insert_five('active_trades', 'petr','username','looking_for', 'description','date_posted', trading_with, dbms._username, trade_for, description, datetime.now())
    print('post was successful!')
    return 6.4

def view_trade_choice()->int | str:
    """checks to see if the user accepts the trade or wants to view the next trade"""
    while True:
        choice = input(
            "type 'accept' to choose engage in this trade, 'next' to go to the next trade, or 'back' to go back to the trading hub: ")
        if choice == 'back':
            return 6
        elif choice == 'next':
            return 'next'
        elif choice == 'accept':
            return 'accept'

def accept_trade(trade)->None:
     """sends the accepted trade to the database"""
     description = input("please explain the trade you are willing to offer: ")
     success = dbms.trade_offered(trade[1], trade[0], trade[4], trade[3], description)
     if success:
         print(
             f'great! your trade offer has been sent to {trade[1]}! this trade will now show up on your pending page')
     else:
         print('you cannot trade with yourself')

def view_active_trades()->int:
    data = dbms.get_active_trades()
    print(f'\nwelcome! there are currently {len(data)} active trades to view!')
    for trade in data:
        print(f'user: {trade[1]}'
              f'\noffered petrs: {trade[0]}'
              f'\nlooking for: {trade[4]}'
              f'\ndescription: {trade[3]}')
        choice = view_trade_choice()
        if choice == 6:
            return choice
        elif choice == 'next':
            pass
        else:
            accept_trade(trade)
        print()
    return 6

def view_pending_trades():
    #types of trades: pending waiting to accept, waiting to be accepted, simply active
    while True:
        choice = input("\ntype 'active' to view your active trades, "
                       "\ntype 'confirm' to view offers on your active trades, "
                       "\ntype 'accepted' to view trades you are waiting to be accepted for, "
                       "\nor type 'back' to go back: ")
        if choice == 'back':
            return 6
        elif choice == 'active':
            return 6.61
        elif choice == 'confirm':
            return 6.62
        elif choice == 'accepted':
            return 6.63

def view_my_active_trades():
    data = dbms.select_star_where('active_trades', 'username', dbms._username)
    if len(data) == 0:
        print('you have no active trades')
        return 6.6
    print(f'\nyou currently have {len(data)} active trades')
    for trade in data:
        print(f'user: {trade[1]}'
              f'\noffered petrs: {trade[0]}'
              f'\nlooking for: {trade[4]}'
              f'\ndescription: {trade[3]}')
        while True:
            choice = input("type 'next' to view the next active trade, type 'delete' to delete the active trade, or type 'back' to go back: ")
            if choice == 'next':
                break
            elif choice == 'back':
                return 6.6
            elif choice == 'delete':
                dbms.delete_from_and('active_trades', 'petr', 'username', trade[0], dbms._username)
                print('active trade successfully deleted!')
                break
        print()
    print('these are all of your active trades')
    return 6.6
def view_need_confirm_trades():
    data = dbms.select_star_where('pending_trades', 'posted_user', dbms._username)
    if len(data) == 0:
        print('you have no active trades')
        return 6.6
    print(f'\nyou currently have {len(data)} trades waiting to be confirmed')
    for trade in data:
        print(f'your offer: {trade[1]}'
              f'\nyour looking for: {trade[2]}'
              f'\ntrade partner: {trade[4]}'
              f'\ntheir offer: {trade[5]}')
        while True:
            choice = input("type 'next' to view the next trade, type 'accept' to accept the offer, type 'deny' to reject a trade, or type 'back' to go back to the pending home page: ")
            if choice == 'back':
                return 6.6
            elif choice == 'next':
                break
            elif choice == 'deny':
                dbms.delete_from_and('pending_trades', 'posted_user', 'offered_petr', trade[0], trade[1])
            elif choice == 'accept':
                traded_with = input('please enter the final petr you traded: ')
                traded_for = input('please enter the final petr you traded for: ')
                dbms.finalize_trade(trade, traded_with, traded_for)
                print('trade is a success! make sure to meet up and finalize the trade!')
                break
        print()
    print('there are no more confirm trades')
    return 6.6
def view_my_active_trades_accepted():
    data = dbms.select_star_where('pending_trades', 'user2', dbms._username)
    if len(data) == 0:
        print('you have no trades waiting to be accepted')
        return 6.6
    print(f'\nyou currently have {len(data)} trades waiting to be accepted')
    for trade in data:
        print(f'posted user: {trade[0]}'
              f'\noffered petr: {trade[1]}'
              f'\nlooking for: {trade[2]}'
              f'\ndescription: {trade[3]}'
              f'\nyour offer: {trade[5]}')
        while True:
            choice = input("type 'next' to view the next trade, type 'delete' to take back your offer, or type 'back' to go back to the pending home page: ")
            if choice == 'back':
                return 6.6
            elif choice == 'next':
                break
            elif choice == 'delete':
                dbms.delete_from_and('pending_trades', 'posted_user', 'offered_petr', trade[0], trade[1])
                print('trade successfully deleted!')
                break
        print()
    print('these are all of your trades waiting to be accepted')
    return 6.6
