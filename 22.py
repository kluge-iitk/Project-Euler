''' Using names.txt, a 46K text file containing over 5000 first names, begin by
sorting it into alphabetical order. Then working out the alphabetical value for
each name, multiply this value by its alphabetical position in the list to
obtain a name score.

What is the total of all the name scores in the file?'''

import os.path
import functools

def p22():
    names = []
    with open(os.path.join(os.path.abspath(''),'files\p022_names.txt'),'r') as f:
        for line in f:
            names.extend(k.strip('"') for k in line.split(','))

    names.sort()

    s = 0

    for i, name in enumerate(names):
        name_score = functools.reduce(int.__add__,map(lambda x: ord(x)-ord('A')+1, name))*(i+1)
        s += name_score

    print(s)


import time
s = time.clock()
p22()
print(time.clock() - s)

