# Problem: Jumping on the Clouds
# Jun Ho Lee

import math
import os
import random
import re
import sys

# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.

## Jumping twice is the limiting factor!
## So need to exhaust that option first and then check for +1 jump cases

def jumpingOnClouds(c):
    jump_count = 0
    current_position = 0
    last_position = len(c) - 1
    second_to_last_position = len(c) - 2

    while current_position < second_to_last_position:
        ## This proactively checks if you can make a double jump at any point along the array!!
        if c[current_position+2] == 0:
            current_position += 2    # make the double jump
        else:
            current_position += 1    # otherwise make a single jump
        jump_count += 1

    ## After the while loop, the position is either at LAST or SECOND_TO_LAST position! (since the max input to WHILE loop is third to last position)
    ## Following code covers the last two positions in array
    if current_position < last_position:
        jump_count += 1
    return jump_count
