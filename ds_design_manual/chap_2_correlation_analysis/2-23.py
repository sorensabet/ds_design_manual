import sympy as sym
import numpy as np
import pandas as pd
import scipy.misc as sm
import scipy.stats as st
import matplotlib

matplotlib.use('TkAgg')

import matplotlib.pyplot as plt

# Tool to calculate probability of making at least k of n shots with probability p where each shot is independent and p remains constant
# P(X>=k) = SUM(i=k,n)(nCk)p^k (1-p)^k

# Planned approach
# Use symbolic math to generate the expression for each case
# Use matplotlib to plot the result for varying P to see which case is better

# Case a) Get 2 of 3 shots
# Case b) Get 5 of 8 shots

# Constants
k1 = 2
n1 = 3

k2 = 5
n2 = 8

# Symbols
p = sym.Symbol('p')

# Blank expressions
exp1 = 0
exp2 = 0

for k in range(k1, n1 + 1):
    exp1 += sm.comb(n1, k) * (p ** k) * ((1 - p) ** (n1 - k))

for k in range(k2, n2 + 1):
    exp2 += sm.comb(n2, k) * (p ** k) * ((1 - p) ** (n2 - k))

print('Finished creating expressions')

f1 = sym.lambdify(p, exp1, "numpy")
f2 = sym.lambdify(p, exp2, "numpy")

print('Finished lambdifying expressions')

# Okay. Now that I have general expressions, I want to evaluate them for p from p=0 to p = 1
label1 = ('%d of %d shots' % (k1, n1))
label2 = ('%d of %d shots' % (k2, n2))

p_shots = np.linspace(0, 1, 50)
plt.plot(p_shots, f1(p_shots), label=label1)
plt.plot(p_shots, f2(p_shots), label=label2)
plt.xlabel('Probability of scoring successfully')
plt.ylabel('Probability of winning game')
plt.title('Probability of winning as a function of scoring probability')
plt.legend()
plt.grid(True)
plt.show()

print('Finished generating plot')

# The results are interesting because around p_shot ~ 0.66, the probability of winning is higher if you get 5 shots than if you get 8 shots.
# Intuiitively, this doens't make sense to me, since I would assume that if you score with the same probability, the scenario with fewer shots overall would be better.
# Perhaps the reason is that there is a chance of missing one of the shots, whereas in the other scenairo you have more chances to miss as you win the game.
# It might also depend on how many shots you have to get compared to how many shots you are taking overall.
