from app.utils.mysql_connection import establish_connection

connection = establish_connection()
if connection:
    try:
        with connection.cursor() as cursor:
            query = "SELECT * FROM xmloutuser"
            cursor.execute(query)
            results = cursor.fetchall()

            for row in results:
                print(row)

    finally:
        connection.close()

