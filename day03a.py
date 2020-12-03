#!/usr/local/bin/python3
import re
(xInc, tree) = (3, '#')
def strip(s):
    return list (s.strip())
def doSlope(data, xInc, step):
    (maxY, maxX, x, numTrees) = (len(data), len(data[0]), 0, 0)
    for y in range(0, maxY, step):
        numTrees += int(data[y][x] == tree)
        x = (x + xInc) % maxX
    return numTrees
with open("day03a.txt",'r') as f:
    data = list (map(strip, f.readlines()))
    print(doSlope(data, 3, 1))
