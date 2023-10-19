from flask import *
from app.models.students import *
from flask_wtf import *

students_bp = Blueprint('students', __name__)

@students_bp.route('/students')  
def students():
    students = view_students()
    return render_template('students.html', students=students) 

@students_bp.route('/studentform/')
def addstudent():
    return render_template("studentsform.html")

@students_bp.route('/studentsform/', methods=['GET', 'POST'])
def addstudents():
    if request.method == 'POST':
        id = request.form['id']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        coursecode = request.form['coursecode']
        yearlevel = request.form['yearlevel']
        gender = request.form['gender']  
        add_student(id, firstname, lastname, coursecode, yearlevel, gender)
        return redirect('/studentsform/') 
    return render_template('studentsform.html')

@students_bp.route('/students/', methods=['GET', 'POST'])
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
        return jsonify({'success': True})