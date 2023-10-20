from flask import *
from app.models.courses import *
from flask_wtf import *

courses_bp = Blueprint('courses', __name__)

@courses_bp.route('/courses/')  
def courses():
    courses = view_courses()
    return render_template('courses.html', courses=courses) 

@courses_bp.route('/courses/add', methods=['GET', 'POST'])
def add_courses():
    if request.method == 'POST':
        coursecode = request.form['coursecode']
        coursename = request.form['coursename']
        collegecode = request.form['collegecode']  
        add_course(coursecode, coursename, collegecode)
        return redirect('/courses/')
    colleges = get_college_codes()
    return render_template('coursesform.html', colleges=colleges)

@courses_bp.route('/courses/search', methods=['GET', 'POST'])
def search_courses():
    courses = []
    if request.method == 'POST':
        search_query = request.form.get('coursesearch')
        if search_query:
            courses = find_course(search_query)
    return render_template('courses.html', courses=courses)

@courses_bp.route('/courses/delete/<string:coursecode>', methods=['DELETE'])
def remove_course(coursecode):
    if request.method == 'DELETE':
        print(coursecode)
        delete_course(coursecode)
        return jsonify({'success': True})

@courses_bp.route('/courses/edit', methods=['GET', 'POST'])
def edit_course():
    course = None   
    
    if request.method == 'GET':
        course_code = request.args.get('coursecode')
        if course_code:
            course = get_course_by_code(course_code)

    elif request.method == 'POST':
        course_code = request.form['coursecode']  
        coursename = request.form['coursename']
        collegecode = request.form['collegecode']

        # Update the course information in the database
        update_course(course_code, coursename, collegecode)

        return redirect(url_for('courses.courses', coursecode=course_code))
    colleges = get_college_codes()
    return render_template('Updatecourse.html', course=course, colleges=colleges)

