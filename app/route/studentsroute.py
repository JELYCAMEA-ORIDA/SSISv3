from flask import *
from app.models.students import *
from flask_wtf import *

students_bp = Blueprint('students', __name__)

@students_bp.route('/students/')  
def students():
    students = view_students()
    return render_template('students.html', students=students) 

@students_bp.route('/students/add', methods=['GET', 'POST'])
def add_students():
    if request.method == 'POST':
        id = request.form['id']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        coursecode = request.form['coursecode']
        yearlevel = request.form['yearlevel']
        gender = request.form['gender']  
        
        # Check if the student already exists
        if student_exists(id):
            flash("Student with this ID already exists.", "error")
        else:
            # Student doesn't exist, add them to the database
            add_student(id, firstname, lastname, coursecode, yearlevel, gender)
            flash("Student added successfully.", "success")
        return redirect('/students/')
    courses = get_course() 
    return render_template('studentsform.html', courses=courses)
from flask import flash, redirect, url_for

@students_bp.route('/students/search', methods=['GET', 'POST'])
def search_students():
    students = []
    if request.method == 'POST':
        search_query = request.form.get('studentsearch')
        if search_query:
            students = find_student(search_query)
    return render_template('students.html', students=students)

@students_bp.route('/students/delete/<string:id>', methods=['DELETE'])
def remove_student(id):
    if request.method == 'DELETE':
        print(id)
        delete_student(id)
        flash('Student deleted successfully!', 'success')
        return jsonify({'success': True})

from flask import flash, redirect, url_for

@students_bp.route('/student/edit', methods=['GET', 'POST'])
def edit_student():
    student = None

    if request.method == 'GET':
        student_id = request.args.get('student_id')
        if student_id:
            student = get_student_by_id(student_id)

    elif request.method == 'POST':
        student_id = request.form['id']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        coursecode = request.form['coursecode']
        yearlevel = request.form['yearlevel']
        gender = request.form['gender']

        # Update the student's information in the database
        update_student(student_id, firstname, lastname, coursecode, yearlevel, gender)

        return redirect(url_for('students.students'))
    courses = get_course()
    return render_template('Updatestudent.html', student=student, courses=courses)
