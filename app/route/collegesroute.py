from flask import *
from app.models.colleges import *
from flask_wtf import *

colleges_bp = Blueprint('colleges', __name__)

@colleges_bp.route('/colleges')  
def colleges():
    colleges = view_colleges()
    return render_template('colleges.html', colleges=colleges) 
