from flask_mysql_connector import MySQL

mysql= MySQL()

def view_students():
    cursor = mysql.connection.cursor(dictionary=True)
    query = "SELECT * FROM students"
    cursor.execute(query)
    students = cursor.fetchall()
    cursor.close()
    return students

def add_student(id, firstname, lastname, coursecode, yearlevel, gender):
    print(id, firstname, lastname, coursecode, yearlevel, gender)
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO students (id, firstname, lastname, coursecode, yearlevel, gender) VALUES (%s, %s, %s, %s, %s, %s)", (id, firstname, lastname, coursecode, yearlevel, gender))
    mysql.connection.commit()
    cursor.close()
    
def find_student(student_search):
    cursor = mysql.connection.cursor(dictionary=True)
    search_query = "%" + student_search + "%"
    cursor.execute("SELECT * FROM students WHERE id LIKE %s OR firstname LIKE %s OR lastname LIKE %s OR coursecode LIKE %s OR yearlevel LIKE %s OR gender LIKE %s", (search_query, search_query, search_query, search_query, search_query, search_query))
    students = cursor.fetchall()
    cursor.close()
    return students

def delete_student(id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM students WHERE id = %s", (id,))
    mysql.connection.commit()
    cursor.close()

def update_student(id, firstname, lastname, coursecode, yearlevel, gender):
    cursor = mysql.connection.cursor()
    update_query = "UPDATE students SET firstname = %s, lastname = %s, coursecode = %s, yearlevel = %s, gender = %s WHERE id = %s"
    cursor.execute(update_query, (firstname, lastname, coursecode, yearlevel, gender, id))
    mysql.connection.commit()
    cursor.close()

def get_student_by_id(student_id):
    cursor = mysql.connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM students WHERE id = %s", (student_id,))
    student = cursor.fetchone()
    cursor.close()
    return student

def get_course():
    cursor = mysql.connection.cursor(dictionary=True)
    cursor.execute("SELECT coursecode FROM courses")
    result = cursor.fetchall()
    print(result)
    cursor.close()
    return result
