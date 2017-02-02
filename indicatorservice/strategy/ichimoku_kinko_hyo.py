""" 
The Ichimoku Cloud, also known as Ichimoku Kinko Hyo, is a versatile
indicator that defines support and resistance, identifies trend direction,
gauges momentum and provides trading signals. Ichimoku Kinko Hyo translates into
“one look equilibrium chart”. With one look, chartists can identify the trend
and look for potential signals within that trend. The indicator was developed by
Goichi Hosoda, a journalist, and published in his 1969 book. Even though the
Ichimoku Cloud may seem complicated when viewed on the price chart, it is really
a straight forward indicator that is very usable. It was, after all, created by
a journalist, not a rocket scientist! Moreover, the concepts are easy to
understand and the signals are well-defined. 
"""


# Tenkan-sen (Conversion Line): (9-period high + 9-period low)/2)) 
# The default setting is 9 periods and can be adjusted. On a daily 
# chart, this line is the mid point of the 9 day high-low range, 
# which is almost two weeks.  

# Kijun-sen (Base Line): (26-period high + 26-period low)/2)) 
# The default setting is 26 periods and can be adjusted. On a daily 
# chart, this line is the mid point of the 26 day high-low range, 
# which is almost one month).  

# Senkou Span A (Leading Span A): (Conversion Line + Base Line)/2)) 
# This is the midpoint between the Conversion Line and the Base Line. 
# The Leading Span A forms one of the two Cloud boundaries. It is 
# referred to as "Leading" because it is plotted 26 periods in the future
# and forms the faster Cloud boundary. 

# Senkou Span B (Leading Span B): (52-period high + 52-period low)/2)) 
# On the daily chart, this line is the mid point of the 52 day high-low range, 
# which is a little less than 3 months. The default calculation setting is 
# 52 periods, but can be adjusted. This value is plotted 26 periods in the future 
# and forms the slower Cloud boundary.

# Chikou Span (Lagging Span): Close plotted 26 days in the past
# The default setting is 26 periods, but can be adjusted. 