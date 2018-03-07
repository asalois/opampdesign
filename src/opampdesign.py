#  A program to find a good balance of op amps and money to get the  output specs needed
#  By Alex Salois March 2018

import numpy as np

# op-amp = [Low f Gain, Unity gain, slew rate]
op1t = np.array([2*10**5,1.5*10**6, 0.7*10**-6])
op1m = np.array([2*10**4, 0.4*10**6, 0.3*10**-6])
op2t = np.array([15*10**5, 8*10**6, 2.8*10**-6])
op2m = np.array([7*10**5, 5*10**6, 1.7*10**-6])

# target specs = [Gain, input resistance, Vpp out, full power bandwidth]
targets = np.array([100, 50, 4, 150*10**3])
