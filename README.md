# Python Microservice Finance

Simple microservice written in python that holds stock related apis

Endpoint available [here](https://whispering-reef-73372.herokuapp.com).

API Documentation available [here](http://docs.pyfinance.apiary.io/).


## Indicators

### Bolinger Band

#### Type:
Volatility indicator

#### Description:
Volatility bands placed above and below a moving average. Use it to measure the __highness__ or __lowness__ of the price relative to previous trades.

#### Signals:
1. When bands are narrow, period of __low__ volatility.
2. When bands expand, increase in price action/market volatility. 

> Similar to: Keltner channel

------

### Moving Average (MA)

#### Type: 
Smoothing trendline

#### Description:
Smooth the price data by reducing noise to form a trend following indicator. They do not predict price direction, but rather define the current direction with a lag. Moving averages lag because they are based on past prices.

> Related to: Exponential moving average (EMA), Simple moving average (SMA)

---

### Simple Moving Average (EMA)

#### Type: 
Moving average

#### Description:
A simple moving average is formed by computing the average price of a security over a specific number of periods.

---
### Exponential Moving Average (EMA)

#### Type: 
Moving average

#### Description:
Reduce lag by applying more weight to recent prices.

---



+ Price Channel (Done)
+ Simple Moving Average Envelope (Done)
+ Accumulation Distribution Line (ADL) (Done)
+ Absolute True Range (ATR) (Done) - measures volatility
+ Chaikin Money Flow (Done) - measures the amount of Money Flow Volume over a specific period
+ Commodity Channel Index (Done) - identify a new trend or warn of extreme conditions
+ Force Index (Done)
+ Money Flow Index (Done) - an oscillator that uses both price and
volume to measure buying and selling pressure
+ Moving Average Convergence/Divergence Oscillator (MACD) (Done) - trend following and momentum
+ Keltner-Channel - (Done) - volatility-based envelopes
+ Percentage Price Oscillator (Done) - momentum oscillator
+ Relative Strength Index (Done)
+ Williams' %R (Done)

In Progress

+ Exponential Moving Average Envelope 
+ Ichimoku Kinko hyo (Not enough data)
+ Parabolic SAR (Not enough data)
+ Average Directional Index (Not enough info)
+ ElderRay (Not enough data)
+ Elder Impulse (Not enough data)
+ Elliot Wave Oscillator (Not enough data)
+ Guppy Multiple Moving Average
+ Momentum
+ On Balance Volume (OBV) (Not enough data)
+ Price Volume Trend (Not enough data)
+ Rate of Change 
+ Smoothed Relative Strength Index
+ Smoothed Stochastic
+ Stochastic
+ Volume

## Glossary

### Volatility

Volatility is a statistical measure of the dispersion of returns for a given security or market index. Volatility can either be measured by using the standard deviation or variance between returns from that same security or market index. Commonly, the higher the volatility, the riskier the security.
