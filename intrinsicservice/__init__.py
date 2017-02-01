from flask import Blueprint
# from .models import Stock
fundamentals = Blueprint('fundamentals',
                         __name__,
                         template_folder='templates')

import views