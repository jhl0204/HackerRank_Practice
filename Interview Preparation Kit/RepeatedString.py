# Problem: Repeated String
# Jun Ho Lee

import math
import os
import random
import re
import sys

# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#
## Approach 1:
## - find the 'a's in substring s
## - length of substring s will be repeated x times with remainder r in length of n
## - multiply x * 'a' found in substring s
## - remainder r might also have a, thus count # of 'a's in the remaining list
## - add the two values together!

def repeatedString(s, n):
    multiple = n // len(s)
    remainder = n % len(s)
    substring_count = 0
    remainder_count = 0
    for i in range(len(s)):
        if s[i] == 'a':
            substring_count += 1
    for i in range(len(s[:remainder])):
        if s[:remainder][i] == 'a':
            remainder_count += 1

    # return remainder
    return multiple * substring_count + remainder_count
