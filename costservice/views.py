import json
from flask import request, jsonify
from . import costs
from models import Calculator

@costs.route('/api/v1/costs/profit', methods=['POST'])
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
  buy_price = body['buy_price']
  sell_price = body['sell_price']
  
  calculator = Calculator()

  return jsonify({
    'data': calculator.profit_or_losses(units, buy_price, sell_price)
  })

@costs.route('/api/v1/costs/minimum-sell-price', methods=['POST'])
def calculate_minimum_sell_price():
  """
  """
  # Accepts only json data
  request.get_json(force=True)
  # Get the request body
  body = json.loads(request.data)
  units = body['units']
  buy_price = body['buy_price']
  
  calculator = Calculator()
  return jsonify({
    'data': calculator.minimum_sell_price(units, buy_price)
  })

@costs.route('/api/v1/costs/target-profit', methods=['POST'])
def calculate_target_profit():
  """
  """
  # Accepts only json data
  request.get_json(force=True)
  # Get the request body
  body = json.loads(request.data)
  units = body['units']
  buy_price = body['buy_price']
  target_profit = body['target_profit']
  
  calculator = Calculator()
  return jsonify({
    'data': calculator.target_sell_price_for_profit(units, buy_price, target_profit)
  })

@costs.route('/api/v1/costs/lists', methods=['POST'])
def calculate_projected_values():
  """
  """
  # Accepts only json data
  request.get_json(force=True)
  # Get the request body
  body = json.loads(request.data)
  units = body['units']
  buy_price = body['buy_price']
  sell_price = body['sell_price']
  
  calculator = Calculator()
  return jsonify({
    'data': calculator.projected_values(units, buy_price, sell_price)
  })