from models import Calculator

units = 3500
buy_price = 1.43
sell_price = 1.51

calculator = Calculator()

print 'minimum sell price', calculator.minimum_sell_price(units, buy_price)
print 'profit_or_losses', calculator.profit_or_losses(units, buy_price, sell_price)
projected_values = calculator.projected_values(units, buy_price, sell_price)
for _, v in enumerate(projected_values):
  print v
print 'has_exceeded_minimum_brokerage_fee', calculator.has_exceeded_minimum_brokerage_fee(units, buy_price)
# print 'Profit or Losses of multiple buy lots', calculator.profit_or_losses_multiple_buy_lots([(100, 4.85), (900, 5.05)], 5.05)
print 'target_sell_price_for_profit', calculator.target_sell_price_for_profit(units, buy_price, 1000)