# Construct dataset of n human heights with p% recorded in English (feet) and rest with metric
# Use statistical tests to determine whether one distribution is distinguishable from another
# What is the boundary as a function of n and p where it becomes clear there is a problem?

# Data for Canada obtained from SOCR height dataset and converted with excel

def statsig(df):
    """
    Return p-value of t-test between height measured in m and height measured in feet
    """

    feet = df.loc[df['calc_height_units'] == 'feet']['calc_height']
    mets = df.loc[df['calc_height_units'] == 'meters']['calc_height']

    return(st.ttest_ind(feet, mets, equal_var=False)[1])


# Approach
# 1) Read in data to pandas
# 2) Randomly sample n cases from the dataset
# 3) Create a new column called modified heights
# 4) Track p% as meters and the remaining in feet
# 5) Run a function to calculate statistical significance of distributions t-test should be fine, can compare two continous distribution means
# 6) Genreate a plot of two distributions
# 7) For various values of n and p, n incremented in 500, p incremented in 0.01, I can create a heat map that shows statistical significance as a colour.

import matplotlib
import numpy as np
import pandas as pd
import scipy.stats as st
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

data = pd.read_csv('/Users/sorensabet/Desktop/ds_design_manual/chap3_preprocessing/height_data.csv')[['Height(Inches)']]
data.rename(columns={'Height(Inches)': 'inches'}, inplace=True)
data = data.sample(frac=1, random_state=0).reset_index(drop=True)

# data['calc_height'] = np.where(data.index < int(p*len(data)), data['inches']/12, data['inches']*0.0254)
# data['calc_height_units'] = np.where(data.index < int(p*len(data)), 'feet', 'meters')

# Okay. Now that I have a way of calculating statistical significance and splitting the dataset, What's the next step?
# Loop over various values of n and p
# Calculate statistical significance for each
# Plot this information on a heat map.
results = []

for n in np.linspace(25, 50, num=51):
    print(n)
    for p in np.linspace(0, 1, 21):
        temp = data.sample(n=int(n), random_state=0).reset_index(drop=True)
        #temp['calc_height'] = np.where(temp.index < int(p*len(temp)), temp['inches']/12, temp['inches']*0.0254)
        temp['calc_height'] = np.where(temp.index < int(p*len(temp)), temp['inches']/12, temp['inches']/12)

        temp['calc_height_units'] = np.where(temp.index < int(p*len(temp)), 'feet', 'meters')
        sig = statsig(temp)
        results.append({'n': n, 'p': p, 'sig': sig})

results_df = pd.DataFrame.from_records(results)

print(results_df)

# P-values are all <0, showing that it is almost immediately obvious when the heights are coming from two different distributions.
# If I use the same units and randomly split which people go into each distribution, the p-values are all above 0.5, showing that
# the data is likely coming from the same distribution (failing to reject the null hypothesis that they are the same distribution).