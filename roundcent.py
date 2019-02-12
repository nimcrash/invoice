from math import *

def to_nearest(number):

    x = number / 0.01
    return (ceil(x) if modf(x)[0] >= 0.5 else floor(x)) * 0.01

def to_nearest_even(number):

    x = number / 0.01
    x = modf(x)[1]
    return x * 0.01 if fmod(x, 2) == 0 else (x + 1) * 0.01