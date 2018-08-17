# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 12:07:54 2018

@author: Galactic Empire
"""

#plotting bootstrap Cumulative Distribution Functions
for _ in range(50):
    # Generate bootstrap sample: bs_sample
    bs_sample = np.random.choice(rainfall, size=len(rainfall))

    # Compute and plot ECDF from bootstrap sample
    x, y = ecdf(bs_sample)
    _ = plt.plot(x, y, marker='.', linestyle='none',
                 color='gray', alpha=0.1)

# Compute and plot ECDF from original data
x, y = ecdf(rainfall)
_ = plt.plot(x, y, marker='.')
#hi
# Make margins and label axes
plt.margins(0.02)
_ = plt.xlabel('yearly rainfall (mm)')
_ = plt.ylabel('ECDF')

# Show the plot
plt.show()

#get a bootstrap measurement of statistic func
def bootstrap_replicate_1d(data, func):
    return func(np.random.choice(data, size=len(data)))