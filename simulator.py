# D&D Dice Simulator
#
# This program contains various functions to simulate die outcomes in D&D
# Note: in D&D shorthand, rolling a Y-sided die X times and adding Z is abbreviated to "XdY+Z"
#

import math
import random

DEBUG = True

def xdyz(x, y, z=0):

    # Simulates rolling XdY+Z

    for i in range(x):

        z += random.randint(1,y)

    return z

def discard_n_lowest(n, x, y, z=0):

    # Simulates rolling XdY+Z, with the lowest N die rolls being ignored
    # Note that this can be used to simulate rolling with advantage (1, 2, 20, 0)
    # Can also be used in character creation (1, 4, 6, 0)
    #

    lst = []

    for i in range(x):

        lst.append(random.randint(1,y))

    lst.sort()
    lst = lst[n:]

    return sum(lst, z)

def discard_n_highest(n, x, y, z=0):

    # Simulates rolling XdY+Z, with the highest N die rolls being ignored
    # Note that this can be used to simulate rolling with disadvantage (1, 2, 20, 0)
    #

    lst = []

    for i in range(x):

        lst.append(random.randint(1,y))

    lst.sort()
    lst = lst[:-n]

    return sum(lst, z)

def reroll_range(lst, x, y, z=0, repeat=True):

    # Simulates rolling XdY+Z, rerolling any dice that result in a value within the range given
    # "repeat" determines whether the new result is kept if it is in that range; by default, it is rerolled again
    #

    if (repeat):

        die = range(1, y+1)
        die = [i for i in die if not in lst]

        for i in range(x):

            z += random.choice(die)

        return z

    else:

        for i in range(x):

            j = random.randint(1, y)

            if (j in lst): # This result needs to be rerolled

                j = random.randint(1, y)

            z += j

        return z

