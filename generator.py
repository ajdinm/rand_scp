from __future__ import print_function

import sys
import random

if(len(sys.argv) < 3):
    print ("Not enough arguments, exiting...")
    sys.exit()

m = int(sys.argv[1]) # number of contraints
n = int(sys.argv[2]) # number of variables
max_cover_coefficient = 0.5

covered = dict()

def get_min_subset_size():
    return 1
def get_max_subset_size():
    return  int(n * max_cover_coefficient)


# print problem size
print (m, n)
# print cost function
for i in range(0, n):
    print ('1 ', end="")
    if(i > 0 and i % 10 == 0):
        print ("\n", end="")
print ("\n")

# print constraints
for i in range(0, m):
    # print subset size
    size = random.randint(get_min_subset_size(), get_max_subset_size())
    print (size)
    for j in range(0, size):
        el = random.randint(1, n)
        covered[el] = 1
        print (str(el), end=" ")
    print ("\n")

if(len(covered) != n):
    print ("ERROR: Please restart algorithm and ignore previous result")




