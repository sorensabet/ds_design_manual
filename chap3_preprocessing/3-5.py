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
    return c1*np.exp(c2*t) + c3*t

data = pd.read_excel('/Users/sorensabet/Desktop/ds_design_manual/chap3_preprocessing/disk_drive_prices.xlsx', header=0)
data['x'] = (data['date'] - min(data['date'])).astype(int)

print(data.head())

# Okay. I first want to come up with a guess that describes the observed curve
g = [0.68*10e7, -0.44, 0.00005]
y_pred = price(data['x'].values, g[0], g[1], g[2])

c, cov = curve_fit(price, data['date'], data['$/Mbyte'].values, p0=[g[0], g[1], g[2]], method='dogbox') # Fit isn't working for some reason.
print(c)                                                                                                # Not worth spending more resources on this problem, I've learned what I needed to learn

y_pred_2 = price(data['x'].values, c[0], c[1], c[2])

plt.figure(figsize=(20,10))
plt.plot(data['date'], data['$/Mbyte'], label='historical')
plt.plot(data['date'], y_pred, 'r-', label='guess')
plt.plot(data['date'], y_pred_2, 'g-', label='fit')
plt.grid(True)
plt.xlabel('Years since 1957')
plt.ylabel('$/Mbyte')
plt.yscale('log')
plt.title('$/Mbyte by year since 1957')
plt.legend()
#plt.show()
plt.savefig('/Users/sorensabet/Desktop/ds_design_manual/chap3_preprocessing/fig.png')

print('Completed plot')

# Part 1 of question: Prices in 5 years:
p_5 = price(2025-1957, g[0], g[1], g[2])
p_0 = price(2020-1957, g[0], g[1], g[2])

print('Price in 2020: %0.10f $/MByte' % (p_0))
print('Price in 5 years: %0.10f $/MByte' % (p_5))
# Testing on dummy data

# My model isn't a good fit on this data; I should exclude older results since the rate of improvement decreases.
# Spline interpolation might be better way to try to fit this curve rather than fitting an exponential function.

# x = np.array([399.75, 989.25, 1578.75, 2168.25, 2757.75, 3347.25, 3936.75, 4526.25, 5115.75, 5705.25])
# y = np.array([109,62,39,13,10,4,2,0,1,2])
#
# def func(x, a, c, d):
#     return a*np.exp(-c*x)+d
#
# popt, pcov = curve_fit(func, x, y, p0=[100, 0.001, 1])
#
# print(popt)
# print(pcov)
#
# xx = np.linspace(min(x), max(x), 100)
# yy = func(xx, *popt)
#
# plt.figure(figsize=(20,10))
# plt.plot(x,y, 'ro-', label='true')
# plt.plot(xx,yy,'g-', label='fit')
#
# plt.grid(True)
# plt.xlabel('Years since 1957')
# plt.ylabel('$/Mbyte')
# #plt.yscale('log')
# plt.title('$/Mbyte by year since 1957')
# plt.legend()
# plt.savefig('/Users/sorensabet/Desktop/ds_design_manual/chap3_preprocessing/fig.png')
#
