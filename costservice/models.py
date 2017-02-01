
from __future__ import division

def Costs:
  def calculate_brokerage_fee(minimum_fee, fee_in_percent=0.42, units, price_per_unit):
    """
      Calculates the brokerage fee
    """
    purchased_price = price_per_unit * units
    calculated_fee = fee_in_percent / 100 * purchased_price
    # Take the lowest fee
    brokerage_fee = min([calculated_fee, minimum_fee])
    return None
  def calculate_clearing_fee ():
    """
      Calculate the clearing fee
    """
    return None
  def calculate_stamp_duty(stamp_duty):
    """
      Calculate the stamp duty
    """
    return None
  def calculate_tax():
    """
      Calculate the after tax price
    """
  def calculate_gross_purchase_price():
    """
      The gross purchase price does not include
      the tax or brokerage fee
    """
    return None
  def calculate_net_purchase_price():
    return None
  def calculate_gross_sell_price():
    """
      The gross purchase price does not include
      the tax or brokerage fee
    """
    return None
  def calculate_net_sell_price():
    """
      Calculate the final sell price 
    """
    return None
  def calculate_profit_or_losses(sell_price):
    """
      Calculate the profit or loss gain
      by selling the stock at the given price
    """
    return None
  def calculate_minimum_sell_value():
    """
      Calculates the minimum cost of the sell
      price per unit in order to gain a profit
    """
    return None
  def calculate_projected_values():
    """
      Calculates a list of projected values and
      the corresponding loss/gain
    """
    return None

