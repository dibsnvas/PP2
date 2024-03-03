from functools import reduce
from operator import mul
import time
import math
def ispolindrome(a):
    return a == "".join(reversed(a))

print(ispolindrome("level"))
print(ispolindrome("moon"))
