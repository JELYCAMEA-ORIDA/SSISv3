from flask_mysql_connector import MySQL

mysql= MySQL()

def view_courses():
    cursor = mysql.connection.cursor(dictionary=True)
    query = "SELECT * FROM courses"
    cursor.execute(query)
    courses = cursor.fetchall()
    cursor.close()
    return courses

def add_course(coursecode, coursename, collegecode):
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO courses (coursecode, coursename, collegecode) VALUES (%s, %s, %s)", (coursecode, coursename, collegecode))
    mysql.connection.commit()
    cursor.close()
    
def find_course(course_search):
    cursor = mysql.connection.cursor(dictionary=True)
    search_query = "%" + course_search + "%"
    cursor.execute("SELECT * FROM courses WHERE coursecode LIKE %s OR coursename LIKE %s OR collegecode LIKE %s", (search_query, search_query, search_query))
    courses = cursor.fetchall()
    cursor.close()
    return courses

def delete_course(course_code):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM courses WHERE coursecode = %s", (course_code,))
    mysql.connection.commit()
    cursor.close()

def update_course(coursecode, coursename, collegecode):
    cursor = mysql.connection.cursor()
    update_query = "UPDATE courses SET coursename = %s, collegecode = %s WHERE coursecode = %s"
    cursor.execute(update_query, (coursename, collegecode, coursecode))
    mysql.connection.commit()
    cursor.close()
    
def get_course_by_code(course_code):
    cursor = mysql.connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM courses WHERE coursecode = %s", (course_code,))
    course = cursor.fetchone()
    cursor.close()
    return course

def get_college_codes():
    cursor = mysql.connection.cursor(dictionary=True)
    query = "SELECT collegecode FROM colleges"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result

def course_exists(coursecode):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT coursecode FROM courses WHERE coursecode = %s", (coursecode,))
    result = cursor.fetchone()
    cursor.close()
    return result is not None
    

