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
            self.update_info('users', 'username', new_username, 'username', self._username)
            self._username = new_username
            return True
        except:
            print('the username is already taken, please try a new one')
            return False

    def update_info(self, table_name, col_name, col_info, where_col_name, where_col_info)->None:
        """updates the info of a user depending on the parameter such as first_name, year, etc"""
        self._cursor.execute(
            f'UPDATE {table_name} SET {col_name} = :col_info WHERE {where_col_name} = :where_col_info',
            {'col_info': col_info, 'where_col_info': where_col_info}
        )
        self._connection.commit()


    def update_password(self, old_password, new_password)->bool:
        """updates the password of a user"""
        try:
            self.update_info('users', 'password', new_password, 'password', old_password)
            return True
        except:
            print('your old password is incorrect, please try again')
            return False

    def get_past_trades(self)->list:
        """returns all the data for the user's past trades """
        self._cursor.execute(
            f'SELECT * FROM past_trades WHERE username1 = :user1 OR username2 = :user2 ORDER BY date_traded DESC',
            {'user1': self._username, 'user2': self._username}
        )
        return self._cursor.fetchall()

    def insert_five(self, table, col1, col2, col3, col4, col5, col1_info, col2_info, col3_info, col4_info, col5_info):
        try:
            self._cursor.execute(
                f'INSERT INTO {table} ({col1}, {col2}, {col3}, {col4}, {col5})'
                f'VALUES (:col1_info, :col2_info, :col3_info, :col4_info, :col5_info)',
                {'col1_info': col1_info, 'col2_info': col2_info, 'col3_info': col3_info, 'col4_info': col4_info, 'col5_info': col5_info}
            )
            self._connection.commit()
        except:
            print('something went wrong')


    def get_active_trades(self)->list:
        """returns all active trades"""
        try:
            self._cursor.execute(
                f'SELECT * FROM active_trades'
            )
            return self._cursor.fetchall()
        except:
            print('something went wrong')

    def trade_offered(self, posted_user, offered_petr, looking_for, description, user2_description)->bool:
        """updates the pending_trades table when a user initiates a trade"""
        if posted_user == self._username:
            return False
        try:
            self._cursor.execute(
                f'INSERT INTO pending_trades (posted_user, offered_petr, looking_for, description, user2, user2_description)'
                f'VALUES (:posted_user, :offered_petr, :looking_for, :description, :user2, :user2_description)',
                {'posted_user': posted_user, 'offered_petr': offered_petr, 'looking_for': looking_for, 'description':description, 'user2': self._username, 'user2_description': user2_description}
            )
            self._connection.commit()
            return True
        except:
            print('something went wrong')

    def delete_from_and(self, table_name, col1, col2, col1_info, col2_info):
        try:
            self._cursor.execute(
                f'DELETE FROM {table_name} WHERE {col1} = :c1_info AND {col2} = :c2_info',
                {'c1_info': col1_info, 'c2_info': col2_info}
            )
            self._connection.commit()
        except:
            print('something went wrong')
    def finalize_trade(self, trade, traded_with, traded_for):
        try:
            self.delete_from_and('pending_trades', 'posted_user', 'offered_petr', trade[0], trade[1])
            self.insert_five('past_trades', 'petr1','petr2','username1','username2','date_traded', traded_with, traded_for, trade[0],trade[4], datetime.now())
            self._cursor.execute(
                f'UPDATE users SET last_trade_date = :date WHERE username = :user1 OR username = :user2',
                {'date': datetime.now(), 'user1': trade[0], 'user2': trade[4]}
            )
            self._connection.commit()
        except:
            print('something went wrong')

    def select_star_where(self, table_name, column_name, column_data):
        try:
            self._cursor.execute(
                f'SELECT * FROM {table_name} WHERE {column_name} = :cd',
                {'cd': column_data}
            )
            return self._cursor.fetchall()
        except:
            print('something went wrong')

