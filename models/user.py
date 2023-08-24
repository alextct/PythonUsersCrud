# models/user.py
# from ..utils.mysql_connection import establish_connection
from .mysql_connection import establish_connection

class User:
    """
    Represents a user with attributes id and user_name.
    Provides methods to interact with the users table in the database.
    """

    def __init__(self, id=None, user_name=None):
        """
        Initialize a User object.

        :param id: User ID. Default is None.
        :param user_name: User's name. Default is None.
        """
        self.id = id
        self.user_name = user_name

    def save(self):
        """
        Save a user to the database.
        If the user already exists (has an id), update the user.
        Otherwise, insert a new user.

        :return: The saved or updated User object.
        """
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
        """
        Fetch all users from the database.

        :return: A list of User objects or None if no users exist.
        """
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
        """
        Fetch a user by its ID.

        :param user_id: The ID of the user to fetch.
        :return: A User object or None if the user does not exist.
        """
        connection = establish_connection()

        try:
            with connection.cursor() as cursor:
                query = "SELECT * FROM users WHERE id = %s"
                cursor.execute(query, user_id)
                result = cursor.fetchone()
                if result:
                    return User(id=result[0], user_name=result[1])
                return None

        finally:
            connection.close()

    def delete(self):
        """
        Delete the user from the database.

        :return: The deleted User object or None if the user did not exist.
        """
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
