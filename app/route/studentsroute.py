from flask import *
from app.models.students import *
from flask_wtf import *

students_bp = Blueprint('students', __name__)

@students_bp.route('/students')  
def students():
    return render_template('students.html') 