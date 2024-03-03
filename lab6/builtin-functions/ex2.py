from functools import reduce
from operator import mul
import time
import math
def count_case(s):
    upper = sum(1 for char in s if char.isupper())
    lower = sum(1 for char in s if char.islower())
    return upper, lower


s = "Salem, alem"
upper, lower = count_case(s)
print(f"Upper case letters: {upper}, Lower case letters: {lower}")
