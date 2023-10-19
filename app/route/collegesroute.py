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