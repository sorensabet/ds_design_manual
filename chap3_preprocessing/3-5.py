# Calculate/estimate disk drive prices over time.
# Found data online at https://jcmit.net/diskprice.htm
# Downloaded data locally and copied
# Use scipy curve fit to guess the curve and plot it
# I should also try to guess the curve.

# Steps
# 1. get x-col as years since start year
# 2. plot x and y on a logarithmic chart
# 3. Fit a logarithmic equation
# 4. Use equation to calculate prices 5 years from now
# 5. Estimate prices 25 - 50 years from now.

import matplotlib
import numpy as np
import pandas as pd
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Exponential function: y = c1 + c2*x + c3*e^(c4*x)
def price(t, c1,c2, c3):
    return c1*c2**(c3*t)

data = pd.read_excel('/Users/sorensabet/Desktop/ds_design_manual/chap3_preprocessing/disk_drive_prices.xlsx', header=0)
data['x'] = (data['date'] - min(data['date'])).astype(int)

# Okay. I first want to come up with a guess that describes the observed curve
y_pred = price(data['x'].values, 0.4*10e8, 0.62, 1)

# c, cov = curve_fit(price, data['x'].values, data['$/Mbyte'])
# print(c)
# print(cov)

# y_pred_2 = price(data['x'].values, c[0], c[1], c[2])

plt.plot(data['date'], data['$/Mbyte'], label='historical')
plt.plot(data['date'], y_pred, 'r-', label='guess')
# plt.plot(data['date'], y_pred_2, 'g-', label='fit')
plt.grid(True)
plt.xlabel('Years since 1957')
plt.ylabel('$/Mbyte')
plt.yscale('log')
plt.title('$/Mbyte by year since 1957')
plt.legend()
plt.savefig('/Users/sorensabet/Desktop/ds_design_manual/chap3_preprocessing/fig.png')

print('Completed plot')


