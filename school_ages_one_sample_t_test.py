import numpy as np
import pandas as pd
import scipy.stats as stats
import math
np.random.seed(6)
school_ages=stats.poisson.rvs(loc=18,mu=35,size=1500) # age starts from18, mean is 35
classA_ages=stats.poisson.rvs(loc=18,mu=30,size=60)
#H0= there is no difference between sample and population mean
#print(np.mean(classA_ages))
t_value, p_value= stats.ttest_1samp(classA_ages, school_ages.mean())
if p_value < 0.05:
    print("we are rejecting null hypothesis")
else:
    print("we are accepting null hypothesis")