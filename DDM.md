# Dividend Discount Model (DDM)
Intrinsic value is the `real value` of a company. In order to know if the company's shares is worth buying, we first need to know the real value of the company.

This can be calculated through the `Dividend Discount Model`.

## Language

Started with JavaScript, but then switched to Python for the following reasons:

1. Numbers in JavaScript are "double-precision 64-bit format IEEE 754 values". E.g. `0.1 + 0.2 == 0.30000000000000004`.
2. Python has matplotlib, a 2D plotting library. 
3. List comprehension in Python makes it easier to perform calculations.

# Glossary

Market value of equity is the total dollar market value of all of a company's outstanding shares. Market value of equity is calculated by multiplying the company's current stock price by its number of outstanding shares. (a.k.a Market Cap)

Written Tuesday 10 January 2017
https://wealthyeducation.com/how-to-calculate-intrinsic-value/


1. Current Share Price - the price at which a company's stock is selling
2. Shares outstanding - The total number of shares that are issued and currently owned by the company's shareholders
3. Free cash flow - this figure represents the company's capacity for generating free cash, which is used for its future expansion, paying off debts and enhancing its shareholder value.
4. Long-term growth rate - the expected rate at which the company will grow
5. Business tax rate - the business income tax paid to the goverment. This tax rate varies among different countries.
6. Business interest rate - The effective rate that the company is charged on its loans and borrowings.
7. Perpertuity growth rate - often known as `terminal growth rate` or `implied perpetuity growth rate`. The rate that the company is expected to grow at after our flow projection period. We'll use the country's GDP growth rate as Perpertuity Growth Rate.
8. Market value of debt - the total dollar market value of a company's short-term and long-term debts
9. Market value of equity - often know as `market cap`, the total dollar market value of a company's outstanding shares.
10. Stock beta - ofter known as `beta coefficient`. Beta is a measure of how much the price of the company's stock tends to fluctuate.
11. Risk free rate -  the minimum rate of return that investors expect to earn from an investment without any risks. We'll use the 10-year goverment's bond as a Risk-Free Rate.
12. Market Risk Premium - the rate of return over the risk-free-rate required by investors. For calculating the discount rate, you can use the market risk premium data from NYU Stern School of business.
13. Total Business debt - the total liabilities of the company
14. Total business cash - the total cash and cash equivalents of the company
15. Cash and cash equivalents - The term cash and cash equivalents includes: currency, coins, checks received but not yet deposited, checking accounts, petty cash, savings accounts, money market accounts, and short-term, highly liquid investments with a maturity of three months or less at the time of purchase such as U.S. treasury bills and commercial paper. The items included as cash and cash equivalents must also be unrestricted.

The amount of cash and cash equivalents will be reported on the balance sheet as the first item in the listing of current assets. The change in the amount of cash and cash equivalents during an accounting period is explained by the statement of cash flows.

### Step 1 - Calculate the Cost of Debt (R_d)

```
Cost of Debt = Interest Rate x (1 - Tax Rate)

Formula for interest rate = periodic interest rate x number of periods per year
e.g.
Procter and Gamble first quarter 2016.
Paid $146 million in Interest Expenses
and had a debt (short + long term) of $32.8 billion.

Periodic interest rate = 146 / 32800 = 0.45%
Interest Rate = 0.45% x 4 (quarterly financial statements)
= 1.9%

Business Tax rate in US = 35% for profit above 18 million
```

## Step 2 - Calculate the company's Cost of Equity

Use Capital Asset Pricing Model (CAPM) to calculate the company's Cost of Equity
```
Cost of equity R_e = Risk Free Rate + Stock Beta x Market Risk Premium
```
Risk Free Rate = 10 year government bond = 4.255% in Malaysia
Market Risk premium can be obtained here: http://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/ctryprem.html
Market risk premium for malaysia is Country Risk Premium = 1.92% (2017)


### Step 3 - Calculate the WACC

WACC weighted average Cost of Capital will be used as discount rate.

W_e = market value of equity / total market value of debt and equity x 100% 
W_d = market value of debt / total market value of debt and equity x 100%

```
Discount Rate = W_e x R_e + W_d x R_d
```

### Step 4 - Calculate the Discounted Cash Flow (DCF)
```
DCF = Projected Cash Flow x Discount Factor

Projected Cash Flow = cash flow x (1 + long-term-growth rate)^n
Discount Factor = 1 / (1 + Discount rate)^n
```
### Step 5 - Calculate the net Present Value

### Step 6 - Calculate the Perpetuity value

The perpetuity value, or terminal value, is simply the total present value of a company's future free cash flows beyond our forecast period.

GDP Growth Rate (Perpetuity growth rate) = 3%
Year 10 Projected FCF = $259.37
Discount Rate (WACC) = 6%
Year-10 discount factor = 0.558
```
Terminal value = a / b x c
a = Year-10 PFCF x (1 + Perpetuitu growth rate)
b = dicount rate - perpetuity growth rate
c = year 10 discount factor
```
### Step 7 - Calculate the. intrinsic value

You can easily calculate the company's net cash by subtracting its total liabilities from its total cash and cash equivalents ("less debt, plus cash").


Intrinsic Value = Net presetn value + Discounted terminla value

Intrinsic Value per share = (Intrinsic Value + cash - debt) / Total number of shares outstanding
