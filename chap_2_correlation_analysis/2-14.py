import numpy as np
import pandas as pd
import scipy.stats as st

# Uniform distribution of points (x, x^k)
df = pd.DataFrame(index=range(1,30))
df['x'] = df.index

for k in range(1, 10):
    df['y=x^' + str(k)] = df['x']**k

# Take a random sample of the data 50 times, and calculate pearson and spearman coefficients for each sample for each column

for i in range(0,50):
    print('Sample %d' % i)
    sample = df.sample(frac=0.5, random_state=i)


    for k in range(1,10):
        pearson = st.pearsonr(sample['x'], sample['y=x^' + str(k)])[0]
        spearman = st.spearmanr(sample['x'], sample['y=x^' + str(k)])[0]
        print('Pearson: %0.2f, Spearman: %0.2f' % (pearson, spearman))
        print('')

# Running the above shows that for each sample, pearson correlation decreases with increasing K (due to the nonlinear effects of x^k)
# whereas spearman correlation is always 1 because the rank is preserved since x^k is monotonic increasing.