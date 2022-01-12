# Problem: Sales by Match
# Jun Ho Lee

import math
import os
import random
import re
import sys

'''
Variables:
int n
array ar
'''

def sockMerchant(n, ar):
    # Write your code here
    ## set(ar) returns the unique elements in the list
    ## using that list, use modulus to find pairs!
    ## Note that count method returns the # of times it appears on the list!
    ## (similar to value_counts() in pandas)

    ## One-liner using list comprehension
    # return sum([ar.count(i)//2 for i in set(ar)])

    ## List Comprehension expanded out
    total_pairs = 0
    for i in set(ar):
        total_pairs += ar.count(i)// 2
    return total_pairs
