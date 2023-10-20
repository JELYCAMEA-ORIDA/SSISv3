from flask import *
from app.models.colleges import *
from flask_wtf import *

colleges_bp = Blueprint('colleges', __name__)

@colleges_bp.route('/colleges')  
def colleges():
    colleges = view_colleges()
    return render_template('colleges.html', colleges=colleges) 

@colleges_bp.route('/collegesform/', methods=['GET', 'POST'])
def addcolleges():
    if request.method == 'POST':
        collegecode = request.form['collegecode']
        collegename = request.form['collegename']
        add_college(collegecode, collegename) 
        return redirect('/collegesform/')
    return render_template('collegesform.html')

@colleges_bp.route('/colleges/', methods=['GET', 'POST'])
def search_colleges():
    colleges = []
    if request.method == 'POST':
        search_query = request.form.get('collegesearch')
        if search_query:
            colleges = find_college(search_query)
    return render_template('colleges.html', colleges=colleges)

@colleges_bp.route('/colleges/delete/<string:collegecode>', methods=['DELETE'])
def remove_college(collegecode):
    if request.method == 'DELETE':
        print(collegecode)
        delete_college(collegecode)
        return jsonify({'success': True})

@colleges_bp.route('/updatecollege', methods=['GET', 'POST'])
def edit_college():
    college = None
    message = None  # Initialize the message variable

    if request.method == 'GET':
        college_code = request.args.get('collegecode')
        if college_code:
            college = get_college_by_code(college_code)

    elif request.method == 'POST':
        college_code = request.form['collegecode']
        collegename = request.form['collegename']

        # Update the college information in the database
        update_college(college_code, collegename)
        flash('College updated successfully!', 'success')  # Flash the success message

        # Redirect to the colleges list with the success message
        return redirect(url_for('colleges.colleges', collegecode=college_code))

    return render_template('Updatecollege.html', college=college)
