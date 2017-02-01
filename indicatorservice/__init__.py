from flask import Blueprint
# from .models import Stock
indicators = Blueprint('indicators',
                         __name__,
                         template_folder='templates')

# import views