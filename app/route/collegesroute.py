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