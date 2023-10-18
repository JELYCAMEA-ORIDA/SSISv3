from flask_mysql_connector import MySQL

mysql= MySQL()

def view_students():
    cursor = mysql.connection.cursor(dictionary=True)
    query = "SELECT * FROM students"
    cursor.execute(query)
    students = cursor.fetchall()
    cursor.close()
    return students