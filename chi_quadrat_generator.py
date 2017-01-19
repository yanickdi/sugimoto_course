from scipy.stats import chi2
import numpy as np
p = np.array([0.995, 0.99, 0.975, 0.95, 0.90, 0.10, 0.05, 0.025, 0.01, 0.005])
df = np.array(list(range(1,30)) + list(range(30, 101, 10))).reshape(-1, 1)
table = chi2.isf(p, df)

for i, line in enumerate(table):
    for j, col in enumerate(line):
        print('{}: {:.2f}'.format(i+1,col))