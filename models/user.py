# models/user.py
import pymysql
from app.utils.mysql_connection import establish_connection


class User:
    def __init__(self, id=None, user_name=None):
        self.id = id
        self.user_name = user_name

    def save(self):
        connection = establish_connection()

        try:
            with connection.cursor() as cursor:
                if self.id is None:
                    # we do not have the user and we have to add it now
                    query = "INSERT INTO users (user_name) VALUES (%s)"
                    cursor.execute(query, self.user_name)
                    connection.commit()
                    self.id = cursor.lastrowid

                else:
                    # we have to update an existing user
                    query = "UPDATE users SET user_name = %s WHERE id = %s"
                    cursor.execute(query, (self.user_name, self.id))
                    connection.commit()

        finally:
            connection.close()

            user = User.get_by_id(self.id)
            return user

    @staticmethod
    def get_all():
        connection = establish_connection()

        try:
            with connection.cursor() as cursor:
                query = "SELECT id, user_name FROM users"
                cursor.execute(query)
                result = cursor.fetchall()
                if result:
                    users = [User(id=row['id'], user_name=row['user_name']) for row in result]
                    return users
                else:
                    return None

        finally:
            connection.close()

    @staticmethod
    def get_by_id(user_id):
        connection = establish_connection()

        try:
            with connection.cursor() as cursor:
                query = "SELECT * FROM users WHERE id = %s"
                cursor.execute(query, user_id)
                result = cursor.fetchone()
                if result:
                    return User(id=result['id'], user_name=result['user_name'])
                return None

        finally:
            connection.close()

    def delete(self):
        if self.id is not None:
            connection = establish_connection()

            try:
                user = User.get_by_id(self.id)
                if user:
                    with connection.cursor() as cursor:
                        query = "DELETE FROM users WHERE id = %s"
                        cursor.execute(query, user.id)
                        connection.commit()
                        return user
                else:
                    return None

            finally:
                connection.close()
