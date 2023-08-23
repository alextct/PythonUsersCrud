# Users Crud

## Prerequisites

Before you begin, ensure you have the following installed:

- Python (version X.X.X)
- Pip (Python package manager)
- Docker (if you plan to use MySQL with Docker)

## Installation

1. Be sure you have the following packages installed:
python-decouple
pymysql
cryptography
selenium
flask
requests

2. Start a Mysql DB:
docker run --name mysql -v $(pwd):/var/lib/mysql -e MYSQL_ROOT_PASSWORD=mysql -e MYSQL_DATABASE=mydb -e MYSQL_USER=user -e MYSQL_PASSWORD=password -p 3306:3306 -d mysql:8.0.33

3. Start the 2 servers, rest_app.py and web_app.py and run combined_testing.py

   
