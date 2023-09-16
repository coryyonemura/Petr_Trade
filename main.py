from ui_functions import *
# from datetime import *
#
# print(datetime.now())
# p()
state = 1
while True:
    if state == 1:
        state = sign_in_screen()
    elif state == 2:
        state = login()
    elif state == 3:
       state = sign_up()
    elif state == 3.5:
        state = get_more_info()
    elif state == 4:
        state = home_screen()
    elif state == 5:
        state = view_profile()
    elif state == 5.5:
        state = update_profile()
    elif state == 6:
        state = trades_home_screen()
    elif state == 6.2:
        state = past_trades()
