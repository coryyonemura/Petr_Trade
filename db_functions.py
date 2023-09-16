import sqlite3
from datetime import *

class Petr_dbms:
    def __init__(self):
        self._connection = sqlite3.connect("users.db")
        self._cursor = self._connection.cursor()
        self._username = None

    #sign up functions
    def check_valid_username(self, username: str, password: str) -> bool:
        """checks the database to make sure that the username
        the user has chosen is not being used by anyone else, returns a bool accordingly"""
        try:
            self._cursor.execute(
                'INSERT INTO users (username, password, first_name, last_name) VALUES (:username, :password, :first_name, :last_name)',
                {'username': username, 'password': password, 'first_name': '', 'last_name': ''}
            )
            self._connection.commit()
            self._username = username
            return True
        except:
            print('the username is already taken, please choose a different username')
            return False

    def update_new_info(self, f_name: str, l_name: str, grade: str) -> None:
        """updates the database with the new information about the user after they create their account"""
        try:
            self._cursor.execute(
                'UPDATE users SET first_name = :f_name, last_name = :l_name, year = :grade WHERE username = :user_name',
                {'f_name': f_name, 'l_name': l_name, 'grade': grade, 'user_name': self._username}
            )
            self._connection.commit()
        except:
            print('something went wrong')

    # login functions
    def check_login_credentials(self, user_name: str, password: str) -> bool:
        """checks to see if the username and password is correct"""
        try:
            self._cursor.execute(
                'SELECT username FROM users WHERE username = :user_name AND password = :password',
                {'user_name': user_name, 'password': password}
            )
            user_name = self._cursor.fetchone()
            if user_name is None:
                print('the username or password was incorrect, please try again')
                return False
            else:
                print(f'welcome back {user_name[0]}!')
                self._username = user_name[0]
                return True
        except:
            print('something went wrong')

    #view/update profile functions
    def get_profile_info(self) ->list:
        """retrieves all the profile information about a user"""
        try:
            self._cursor.execute(
                'SELECT * FROM users WHERE username = :user_name',
                {'user_name': self._username}
            )
            return self._cursor.fetchone()
        except:
            print("something went wrong")

    def update_username(self, new_username)->bool:
        """updates the username of a user"""
        try:
            self._cursor.execute(
                f'UPDATE users SET username = :new_username WHERE username = :old_username',
                {'new_username': new_username, 'old_username': self._username}
            )
            self._connection.commit()
            self._username = new_username
            return True
        except:
            print('the username is already taken, please try a new one')
            return False

    def update_info(self, type_info, info)->None:
        """updates the info of a user depending on the parameter such as first_name, year, etc"""
        self._cursor.execute(
            f'UPDATE users SET {type_info} = :info WHERE username = :username',
            {'info': info, 'username': self._username}
        )
        self._connection.commit()

    def update_password(self, old_password, new_password)->bool:
        """updates the password of a user"""
        try:
            self._cursor.execute(
                f'UPDATE users SET password = :new_password WHERE password = :old_password',
                {'new_password': new_password, 'old_password': old_password}
            )
            self._connection.commit()
            return True
        except:
            print('your old password is incorrect, please try again')
            return False

    def practice(self):
        self._cursor.execute(
            f'INSERT INTO past_trades (petr1, petr2, username1, username2, date_traded) VALUES (:petr1, :petr2, :username1, :username2, :date)',
            {'petr1': 'spongebob', 'petr2': 'patrick', 'username1': 'cory', 'username2': 'coryy', 'date': datetime.now()}
        )
        self._connection.commit()

    def get_past_trades(self):
        self._cursor.execute(
            f'SELECT * FROM past_trades WHERE username1 = :user1 OR username2 = :user2 ORDER BY date_traded DESC',
            {'user1': self._username, 'user2': self._username}
        )
        return self._cursor.fetchall()