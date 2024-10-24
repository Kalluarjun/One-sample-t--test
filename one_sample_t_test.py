import numpy as np
from scipy.stats import ttest_1samp
#population 
ages=[10,20,35,50,28,40,55,18,16,55,30,25,43,18,30,28,14,24,16,17,32,35,26,27,65,18,43,23,21,20,19,70]

#taking sample
sample_size= 10
# H0= there is no difference between sample and population mean
age_sample= np.random.choice(ages, sample_size)
ttest, p_value= ttest_1samp(age_sample, 30) # 30-> population mean

if p_value < 0.05:
    print("we are rejecting null hypothesis")
else:
    print("we are accepting null hypothesis")
    