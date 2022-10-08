import mysql.connector

try:

    cnx = mysql.connector.connect(host="127.0.0.1", user="root", password="1234", database="CratData")
    cursor = cnx.cursor(dictionary=True)

    print("200")
      
except Exception as err:

    print(err)
