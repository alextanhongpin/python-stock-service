"""
    contains the fundamentals formula
"""
import json

from flask import request, jsonify
from .models import DividendDiscountModel
from .utils import pretty_currency, pretty_percent

from . import fundamentals

@fundamentals.route('/')
def index():
    return 'Navigate to fundamentals/dividend-discount-model to get started'

@fundamentals.route('/fundamentals/dividend-discount-model', methods=['POST'])
def dividend_discount_model():
    """
        Calculates the DDM

        TODO: 
        Carry out validation
    """
    request.get_json(force=True)
    body = json.loads(request.data)

    # Load the class that will be used for the calculation
    ddm = DividendDiscountModel()

    # Step 1: Calculate WACC
    rd = ddm.cost_of_debt(body['interest_rate'], body['business_tax_rate'])
    re = ddm.cost_of_equity(body['risk_free_rate'], 
                            body['stock_beta'], 
                            body['market_risk_free_premium'])
    wd = ddm.weight_of_debt(body['market_value_of_debt'], body['total_market_value_of_debt_and_equity'])
    we = ddm.weight_of_equity(body['market_value_of_equity'], body['total_market_value_of_debt_and_equity'])
    
    wacc = ddm.weighted_average_cost_of_capital(rd, re, wd, we)

    # STEP 2 - Calculate Discounted Free Cash Flow (DCFC)
    dcf = ddm.discounted_cash_flow(body['years'], 
                                   body['long_term_growth_rate'], 
                                   body['free_cash_flow'], 
                                   body['discount_rate'])

    npv = ddm.net_present_value(dcf)

    discount_rate = wacc
    year_ten_projected_free_cash_flow = dcf[-1][0]
    year_ten_discount_factor = dcf[-1][1]

    # STEP 3 - Calculate company's Terminal value
    terminal_value = ddm.terminal_value(year_ten_projected_free_cash_flow, 
                                        year_ten_discount_factor, 
                                        body['perpetuity_growth_rate'], 
                                        discount_rate)
    ivps = ddm.intrinsic_value_per_share(npv,
                                         terminal_value,
                                         body['cash_and_cash_equivalent'],
                                         body['total_liabilities'],
                                         body['shares_outstanding'])
    output = {
        're': re,
        'rd': rd,
        'wd': wd,
        'we': we,
        'wacc': wacc,
        'wacc_pretty': pretty_percent(wacc),
        'dcf': dcf,
        'npv': npv,
        'npv_pretty': pretty_currency(npv),
        'tv': terminal_value,
        'tv_pretty': pretty_currency(terminal_value),
        'ivps': ivps,
        'ivps_pretty': pretty_currency(ivps)
    }

    return jsonify(output)
