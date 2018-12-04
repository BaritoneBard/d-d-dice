# D&D Dice Calculator
#
# This program contains various functions to calculate die outcomes in D&D
# Note: in D&D shorthand, rolling a Y-sided die X times and adding Z is abbreviated to "XdY+Z"
#

import random
import math

def choose(n,k):

    # Calculates N choose K

    if (n < 0):

        return ((-1)**k)*choose(n+k-1, k)

    if (n == 0):

        return 0

    else:

        return (math.factorial(n)/math.factorial(k))/math.factorial(n-k)

def average(x, y, z=0):

    # Calculates the average outcome of rolling XdY+Z

    return (x*(y+1.0)/2.0)+z

def maximum(x, y, z=0):

    # Returns the maximum value of rolling XdY+Z

    return (x*y)+z

def minimum(x, y, z=0):

    # Returns the minimum value of rolling XdY+Z

    return x+z

def num_equal(n, x, y, z=0):

    # Returns the number of outcomes of rolling XdY+Z equal to N
    # Using a mathematical function to derive this solution
    #
    # Credit to G Cab on Stack Exchange for providing this formula
    # https://math.stackexchange.com/questions/992125/if-i-roll-three-dice-at-the-same-time-how-many-ways-the-sides-can-sum-up-to-13/1680420#1680420
    #
    # All arguments for this function should be nonnegative integers
    #

    n = n-z
    t = 0

    if (n < x): return 0
    if (n > x*y): return 0

    for j in range(int((n-x)/y)+1):

        t += ((-1)**j)*choose(x,j)*choose(n-1-(j*y), n-x-(j*y))

    return t

def chance_equal(n, x, y, z=0):

    # Returns the probability that XdY+Z results in N

    return num_equal(n, x, y, z)/(y**x)

def chance_greater(n, x, y, z=0):

    # Returns the probability that XdY+Z results in M > N

    if (n < average(x, y, z)): # Faster to count the negative cases

        return 1.0-chance_leq(n, x, y, z)

    else:

        t = 0.0

        for i in range(n+1, maximum(x,y,z)+1):

            t += chance_equal(i,x,y,z)

        return t

def chance_less(n, x, y, z=0):

    # Returns the probability that XdY+Z results in M < N

    if (n > average(x,y,z)): # Faster to count the negative cases

        return 1.0-chance_geq(n,x,y,z)

    else:

        t = 0.0

        for i in range(minimum(x,y,z), n):

            t += chance_equal(i,x,y,z)

        return t

def chance_geq(n, x, y, z=0):

    # Returns the probability that XdY+Z results in M >= N

    if (n < average(x, y, z)): # Faster to count the negative cases

        return 1.0-chance_leq(n, x, y, z)

    else:

        t = 0.0

        for i in range(n, maximum(x,y,z)+1):

            t += chance_equal(i,x,y,z)

        return t

def chance_leq(n, x, y, z=0):

    # Returns the probability that XdY+Z results in M <= N

    if (n > average(x,y,z)): # Faster to count the negative cases

        return 1.0-chance_geq(n,x,y,z)

    else:

        t = 0.0

        for i in range(minimum(x,y,z), n+1):

            t += chance_equal(i,x,y,z)

        return t
