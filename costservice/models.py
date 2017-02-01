
from __future__ import division
import math

class Calculator:
  def __init__(self, brokerage_fee=0.42, minimum_brokerage_fee=12, clearing_fee=0.03, stamp_duty=0.001, tax_rate=0.06, provider='maybank'):
    self.BROKERAGE_FEE = brokerage_fee
    self.MINIMUM_BROKERAGE_FEE = minimum_brokerage_fee
    self.CLEARING_FEE = clearing_fee
    self.STAMP_DUTY = stamp_duty
    self.TAX_RATE = tax_rate
  def brokerage_fee(self, units, price_per_unit):
    """
      Calculates the brokerage fee
    """
    purchased_price = price_per_unit * units
    calculated_fee = self.BROKERAGE_FEE / 100 * purchased_price
    # Take the lowest fee
    brokerage_fee = max([calculated_fee, self.MINIMUM_BROKERAGE_FEE])
    return brokerage_fee
  def has_exceeded_minimum_brokerage_fee(self, units, price_per_unit):
    sell_price = self.minimum_sell_price(units, price_per_unit)
    return self.brokerage_fee(units, sell_price) != 12
  def clearing_fee (self, units, price_per_unit):
    """
      Calculate the clearing fee
    """
    output = self.CLEARING_FEE / 100 * units * price_per_unit
    return math.ceil(output*100) / 100
  def stamp_duty(self, units, price_per_unit):
    """
      Calculate the stamp duty
    """
    return math.ceil(self.STAMP_DUTY * units * price_per_unit)
  def total_brokerage_fee(self, units, price_per_unit):
    return self.brokerage_fee(units, price_per_unit) + self.clearing_fee(units, price_per_unit)
  def gst_tax(self, units, price_per_unit):
    """
      Calculate the after tax price
    """
    return math.ceil(self.TAX_RATE * self.total_brokerage_fee(units, price_per_unit)*100) / 100
  def total_fee(self, units, price_per_unit):
    """
      Calculates the broke
    """
    brokerage_fee = self.brokerage_fee(units, price_per_unit)
    clearing_fee = self.clearing_fee(units, price_per_unit)
    stamp_duty = self.stamp_duty(units, price_per_unit)
    gst_tax = self.gst_tax(units, price_per_unit)
    return brokerage_fee + clearing_fee + stamp_duty + gst_tax
  def gross_amount(self, units, price_per_unit):
    """
      The gross purchase price does not include
      the tax or brokerage fee
    """
    return units * price_per_unit
  def net_purchase_price(self, units, price_per_unit):
    gross_amount = self.gross_amount(units, price_per_unit)
    total_fee = self.total_fee(units, price_per_unit)
    return gross_amount + total_fee
  def net_sell_price(self, units, price_per_unit):
    """
      Calculate the final sell price 
    """
    gross_amount = self.gross_amount(units, price_per_unit)
    total_fee = self.total_fee(units, price_per_unit)
    return gross_amount - total_fee
  def profit_or_losses(self, units, price_per_unit_buy, price_per_unit_sell):
    """
      Calculate the profit or loss gain
      by selling the stock at the given price
    """
    net_sell_price = self.net_sell_price(units, price_per_unit_sell)
    net_purchase_price = self.net_purchase_price(units, price_per_unit_buy)
    return net_sell_price - net_purchase_price
  def profit_or_losses_percent(self, units, price_per_unit_buy, price_per_unit_sell):
    """
      Calculate the profit or loss gain
      by selling the stock at the given price
    """
    net_sell_price = self.net_sell_price(units, price_per_unit_sell)
    net_purchase_price = self.net_purchase_price(units, price_per_unit_buy)
    return (net_sell_price - net_purchase_price) / net_purchase_price * 100
  def minimum_units_for_brokerage(self, price_per_unit):
    """
      Calculates the number of units that needs to be purchased
      in order to exceed the minimum brokerage value
    """
    return math.ceil(self.MINIMUM_BROKERAGE_FEE / price_per_unit * 100 / self.BROKERAGE_FEE)
  def lowest_price_for_brokerage(self, units):
    """
      Calculates the minimum price that needs to be paid
      in order to achieve the minimum brokerage price
    """
    return math.ceil(self.MINIMUM_BROKERAGE_FEE / units * 100 / self.BROKERAGE_FEE * 100) / 100
  def minimum_sell_price(self, units, price_per_unit_buy):
    """
      Calculates the minimum cost of the sell
      price per unit in order to gain a profit
    """
    net_purchase_price = self.net_purchase_price(units, price_per_unit_buy)
    if price_per_unit_buy > self.lowest_price_for_brokerage(units):
      price = net_purchase_price / units
      diff = 1 - (0.42 / 100 + 0.03 / 100 + 1 / 1000 + 6 / 100 * (0.42 / 100 + 0.03 / 100))
      return math.ceil(price / diff * 100) / 100
    else: 
      price = (net_purchase_price + 12 + (6 / 100 * 12)) / units
      diff = 1 - (0.03 / 100 + 1 / 1000 + 6 / 100 * (0.03 / 100))
      return math.ceil(price / diff * 100) / 100
  def projected_values(self, units, price_per_unit_buy, price_per_unit_sell):
    """
      Calculates a list of projected values and
      the corresponding loss/gain
    """
    lower_boundary = math.floor(price_per_unit_buy)
    upper_boundary = math.ceil(price_per_unit_buy) + 1
    diff = upper_boundary - lower_boundary
    step = 0.01
    data = []
    for i in range(int(diff / step)):
      sell_price = lower_boundary + i * step
      item = {}
      item['sell_price'] = sell_price
      item['profit_or_loss'] = self.profit_or_losses(units, price_per_unit_buy, sell_price)
      data.append(item)
    return data
  def profit_or_losses_multiple_buy_lots(self, lots, sell_price):
    sum_of_net_purchase_price = sum([self.net_purchase_price(units, price) for units, price in lots])
    sum_of_units = sum(units for units, _ in lots)
    net_sell_price = self.net_sell_price(sum_of_units, sell_price)
    return net_sell_price - sum_of_net_purchase_price
  def target_sell_price_for_profit(self, units, price_per_unit, profit):
    if (profit <= 0):
      return None
    net_purchase_price = self.net_purchase_price(units, price_per_unit)
    # Get the Net Sell Price
    net_sell_price = profit + net_purchase_price
    # Check to see if minimum sell price has exceeded minimum brokerage fee
    if self.has_exceeded_minimum_brokerage_fee(units, price_per_unit):
      price = net_sell_price / units
      diff = 1 - (0.42 / 100 + 0.03 / 100 + 1 / 1000 + 6 / 100 * (0.42 / 100 + 0.03 / 100))
      return math.ceil(price / diff * 100) / 100
    else: 
      price = (net_sell_price + 12 + (6 / 100 * 12)) / units
      diff = 1 - (0.03 / 100 + 1 / 1000 + 6 / 100 * (0.03 / 100))
      return math.ceil(price / diff * 100) / 100
    # Reverse calculate the price per unit sell
    # self.net_sell_price(units, price_per_unit_sell)
    
