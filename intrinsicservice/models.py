"""
  Dividend Discount Model (DDM)
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  The dividend discount model (DDM) is a method of valuing a 
  company's stock price based on the theory that its stock is 
  worth the sum of all of its future dividend payments, 
  discounted back to their present value

"""
from __future__ import division

class DividendDiscountModel():
    def cost_of_debt(self, interest_rate, business_tax_rate):
        """
          After-Tax Cost of Debt (Rd):
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

          Cost of debt is the interest a company pays 
          on its borrowings
        """
        return interest_rate*(1 - business_tax_rate)

    def cost_of_equity(self, risk_free_rate, stock_beta, market_risk_free_premium):
        """
        Cost of Equity (Re):
        ~~~~~~~~~~~~~~~~~~~

        In finance, the cost of equity is the return (often expressed
        as a rate of return) a firm theoretically pays to its equity
        investors, i.e., shareholders, to compensate for the risk they
        undertake by investing their capital.
        """
        return risk_free_rate + stock_beta*market_risk_free_premium

    def weight_of_debt(self, market_value_of_debt, total_market_value_of_debt_and_equity):
        """
        Calculate Weight of Debt (Wd)
        """
        return market_value_of_debt / total_market_value_of_debt_and_equity

    def weight_of_equity(self, market_value_of_equity, total_market_value_of_debt_and_equity):
        """
        Calculate Weight of Equity (We)
        """
        return market_value_of_equity / total_market_value_of_debt_and_equity


    def weighted_average_cost_of_capital(self, cost_of_debt, cost_of_equity, weight_of_debt, weight_of_equity):
        """
          Calculate Weighted Average Cost of Capital (WACC)
        """
        # wacc = re * we + rd * wd
        return cost_of_equity*weight_of_equity + cost_of_debt*weight_of_debt


    def projected_free_cash_flow(self, long_term_growth_rate, year, free_cash_flow):
        """
        The projected free cash flow gives information about the amount spent
        """
        return pow(long_term_growth_rate + 1, year) * free_cash_flow


    def discount_factor(self, discount_rate, year):
        """
        docstring
        """
        return 1 / pow((1 + discount_rate), year)

    def discounted_cash_flow(self, years, long_term_growth_rate, free_cash_flow, discount_rate):
        """
            Discounted cash flow
        """
        projected_growth_rate_for_n_years = [(
            self.projected_free_cash_flow(long_term_growth_rate, year + 1, free_cash_flow), 
            self.discount_factor(discount_rate, year + 1)
        ) for year in range(years)]
        return projected_growth_rate_for_n_years


    def net_present_value(self, projected_growth_rate_for_n_years):
        """
            NPV
        """
        return sum([pfc * df for pfc, df in projected_growth_rate_for_n_years])


    def terminal_value(self, year_ten_projected_free_cash_flow, year_ten_discount_factor, perpetuity_growth_rate, discount_rate):
        """
            Terminal Value
        """
        return (year_ten_projected_free_cash_flow*(1 + perpetuity_growth_rate)) / (discount_rate - perpetuity_growth_rate) * year_ten_discount_factor



    # # STEP 4 - Calculate Intrinsic Value per share
    def intrinsic_value_per_share (self, net_present_value, terminal_value, cash_and_cash_equivalent, total_liabilities, shares_outstanding):
        return (net_present_value + terminal_value + cash_and_cash_equivalent - total_liabilities) / shares_outstanding

