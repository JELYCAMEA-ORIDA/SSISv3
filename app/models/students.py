from flask_mysql_connector import MySQL

mysql= MySQL()

def view_students():
    cursor = mysql.connection.cursor(dictionary=True)
    query = """ SELECT students.*, CONCAT(colleges.collegename, ' (', courses.collegecode, ')') AS collegecode FROM students
    JOIN courses ON students.coursecode = courses.coursecode JOIN colleges ON courses.collegecode = colleges.collegecode"""
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
    query = """
        SELECT students.*, CONCAT(colleges.collegename, ' (', courses.collegecode, ')') AS collegecode
        FROM students
        JOIN courses ON students.coursecode = courses.coursecode
        JOIN colleges ON courses.collegecode = colleges.collegecode
        WHERE students.id LIKE %s
           OR students.firstname LIKE %s
           OR students.lastname LIKE %s
           OR students.coursecode LIKE %s
           OR students.yearlevel LIKE %s
           OR students.gender LIKE %s
           OR colleges.collegecode LIKE %s
    """
    cursor.execute(query, (search_query, search_query, search_query, search_query, search_query, search_query, search_query))
    students = cursor.fetchall()
    cursor.close()
    print("Search Results:", students)  # Add this line for debugging
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

def student_exists(student_id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT id FROM students WHERE id = %s", (student_id,))
    result = cursor.fetchone()
    cursor.close()
    return result is not None

def check_id(student_id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT id FROM students WHERE id = %s", (student_id,))
    result = cursor.fetchone()
    cursor.close()
    return result
