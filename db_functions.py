import sqlite3

class Petr_dbms:
    def __init__(self):
        self._connection = sqlite3.connect("user_info.db")
        self._cursor = self._connection.cursor()
        self._username = None


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