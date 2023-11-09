from flask_mysql_connector import MySQL

mysql= MySQL()

def view_colleges():
    cursor = mysql.connection.cursor (dictionary=True)
    query= "SELECT * FROM colleges"
    cursor.execute(query)
    colleges = cursor.fetchall()
    cursor.close()
    return colleges

def add_college(collegecode, collegename):
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO colleges (collegecode, collegename) VALUES (%s, %s)", (collegecode, collegename))
    mysql.connection.commit()
    cursor.close()

def find_college(college_search):
    cursor = mysql.connection.cursor(dictionary=True)
    search_query = "%" + college_search + "%"
    cursor.execute("SELECT * FROM colleges WHERE collegecode LIKE %s OR collegename LIKE %s", (search_query, search_query))
    colleges = cursor.fetchall()
    cursor.close()
    return colleges

def delete_college(college_code):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM colleges WHERE collegecode = %s", (college_code,))
    mysql.connection.commit()
    cursor.close()

def update_college(collegecode, collegename):
    cursor = mysql.connection.cursor()
    update_query = "UPDATE colleges SET collegename = %s WHERE collegecode = %s"
    cursor.execute(update_query, (collegename, collegecode))
    mysql.connection.commit()
    cursor.close()

def get_college_by_code(college_code):
    cursor = mysql.connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM colleges WHERE collegecode = %s", (college_code,))
    college = cursor.fetchone()
    cursor.close()
    return college

def college_exists(collegecode):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT collegecode FROM colleges WHERE collegecode = %s", (collegecode,))
    result = cursor.fetchone()
    cursor.close()
    return result is not None
