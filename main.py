from ui_functions import *

state = 1

#main states loop
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
    elif state == 6.4:
        state = post_trades()
    elif state == 6.6:
        state = view_pending_trades()
    elif state == 6.61:
        state = view_my_active_trades()
    elif state == 6.62:
        state = view_need_confirm_trades()
    elif state == 6.63:
        state = view_my_active_trades_accepted()
    elif state == 6.8:
        state = view_active_trades()

