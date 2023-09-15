from ui_functions import *

def all_login():
    if sign_in_screen() == 'l':
        login()
    else:
        get_username_password()
        get_more_info()

all_login()
home_screen()


# while True:
#     login()
#     while True:
#         if login:
#             while True:
#                 login()
#                 while True:
#
#                 if back:
#                     break
#         elif signin:
#             while True:
#                 signin()
#                 if back:
#                     break
#         elif back:
#             break



