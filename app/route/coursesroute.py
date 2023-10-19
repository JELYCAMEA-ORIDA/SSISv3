from flask import *
from app.models.courses import *
from flask_wtf import *

courses_bp = Blueprint('courses', __name__)

@courses_bp.route('/courses')  
def courses():
    courses = view_courses()
    return render_template('courses.html', courses=courses) 

@courses_bp.route('/coursesform/', methods=['GET', 'POST'])
def addcourses():
    if request.method == 'POST':
        coursecode = request.form['coursecode']
        coursename = request.form['coursename']
        collegecode = request.form['collegecode']
        add_course(coursecode, coursename, collegecode)
        return redirect('/coursesform/')
    return render_template('coursesform.html')
