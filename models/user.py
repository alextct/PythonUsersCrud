# models/user.py
import pymysql
from app.utils.mysql_connection import establish_connection


class User:
    def __init__(self, id=None, user_name=None, email=None):
        self.id = id
        self.user_name = user_name

    def save(self):
        connection = establish_connection()

        try:
            with connection.cursor() as cursor:
                if self.id is None:
                    # Insert a new user
                    sql = "INSERT INTO users (user_name, email) VALUES (%s, %s)"
                    cursor.execute(sql, self.user_name)
                    connection.commit()
                    self.id = cursor.lastrowid
                else:
                    # Update an existing user
                    sql = "UPDATE users SET user_name = %s WHERE id = %s"
                    cursor.execute(sql, (self.user_name, self.id))
                    connection.commit()

        finally:
            connection.close()

    @staticmethod
    def get_all():
        connection = establish_connection()

        try:
            with connection.cursor() as cursor:
                sql = "SELECT id, user_name, email FROM users"
                cursor.execute(sql)
                result = cursor.fetchall()
                users = [User(id=row['id'], user_name=row['user_name'], email=row['email']) for row in result]
                return users

        finally:
            connection.close()

    @staticmethod
    def get_by_id(user_id):
        connection = establish_connection()

        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM users WHERE id = %s"
                cursor.execute(sql, user_id)
                result = cursor.fetchone()
                if result:
                    return User(id=result['id'], user_name=result['user_name'], email=result['email'])
                return None

        finally:
            connection.close()

    def delete(self):
        if self.id is not None:
            connection = establish_connection()

            try:
                with connection.cursor() as cursor:
                    sql = "DELETE FROM users WHERE id = %s"
                    cursor.execute(sql, (self.id,))
                    connection.commit()

            finally:
                connection.close()
