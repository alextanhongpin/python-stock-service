from flask import Blueprint
# from .models import Stock
costs = Blueprint('costs',
                   __name__,
                   template_folder='templates')

import views