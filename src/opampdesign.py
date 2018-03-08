#  A program to find a good balance of op amps and money to get the  output specs needed
#  By Alex Salois March 2018

import numpy as np
import math as mt

# op-amp = [Low f Gain, Unity gain, slew rate]
op1t = np.array([2*10**5,1.5*10**6, 0.7*10**-6])
op1m = np.array([2*10**4, 0.4*10**6, 0.3*10**-6])
op2t = np.array([15*10**5, 8*10**6, 2.8*10**-6])
op2m = np.array([7*10**5, 5*10**6, 1.7*10**-6])

# target specs = [Gain, input resistance, Vpp out, full power bandwidth]
targets = np.array([100, 50, 4, 150*10**3])


# input the op-amp
def get_gpb(array):
    gbp = array[1] * array[3]
    return gbp


# input k the gain and the op-amp
def find_corner(k, array):
    corner = array[1] / k
    return corner


# input output voltage Vpp and frequency needed
def find_sr(v, f):
    sr = v*mt.pi*f
    return sr


# input f is the bandwidth
def calc_pole_mag(f):
    p = targets[4] / f
    mag = mt.sqrt(1 + p**2)
    return mag


# input (array of closed loop bandwidths)
def is_3db(array):
    mag = 1
    for i, line in enumerate(array):
        mag = mag * calc_pole_mag(array[i])
    if mag < mt.sqrt(2):
        return True
    else:
        return False


sr = find_sr(5, 130000)
print('sr=', sr/10**6, 'V/us')
