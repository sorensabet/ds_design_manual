import numpy as np
import pandas as pd
import scipy.stats as st

data = pd.read_csv('/Users/sorensabet/Desktop/ds_design_manual/chap_2_correlation_analysis/olympics.csv')

print(data.head())
print(data.columns)

# Get correlation between GDP and # of gold medals
pear_corr = st.pearsonr(data['2011 GDP'], data['Gold medals'])
spear_corr = st.spearmanr(data['2011 GDP'], data['Gold medals'])
print(pear_corr)
print(spear_corr)

# both spearman and pearson coefficients are > 0.8 with p value < 0.0001, therefore we see (as expected)
# that richer countries have systematic advantages against poorer countries in the olympics
# (better nutrition, better training facilities, more funding for atheletes, etc.)
# as expected.