import pymysql
from decouple import config


def establish_connection():
    # config = Config('app/.env')

    host = config('DB_HOST')
    user = config('DB_USER')
    password = config('DB_PASSWORD')
    database = config('DB_NAME')

    try:
        connection = pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=database
        )

        print("Connected to the MySQL database!")
        return connection

    except pymysql.MySQLError as e:
        print(f"Error: {e}")
        return None
