# Problem: Counting Valleys
# Jun Ho Lee

import math
import os
import random
import re
import sys

'''
Variables:
INTEGER steps
STRING path
'''

## Solution Logic: If person comes 'UP' and then the sea level becomes 0, person automatically came out from a 'valley'!

def countingValleys(steps, path):
    sea_level = valley = 0
    for i in range(steps):
        if path[i] == 'U':
            sea_level += 1
        else:
            sea_level -= 1

        if sea_level == 0 and path[i] == 'U':
            valley += 1
    return valley
