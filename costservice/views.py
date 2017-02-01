
from . import costs_route

@costs.route('/api/v1/costs')
def calculate_costs():
  """
    Calculates the brokerage fee, 
    stamp duty, and clearing fee
    and sums it for the purchase/sale
    price of the stocks and include the
    additional 6% GST Tax for stocks
    purchased from Maybank Malaysia
  """
  # Accepts only json data
  request.get_json(force=True)
  # Get the request body
  body = json.loads(request.data)
  units = body['units']
  # Can be sell too
  bought_price = body['bought_price']
  current_price = body['current_price']
  