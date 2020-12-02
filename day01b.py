#!/usr/local/bin/python3
def solve(data, low, target, product):
    high = len(data) - 1
    if 2*data[low] > target:
        return
    while(low < high):
        if (data[low] + data[high] == target):
            print(product*data[low]*data[high])
            quit()
        elif (data[low] + data[high] < target):
            low += 1
        else:
            high -= 1
    return
with open("day01a.txt",'r') as f:
    (data, target) =  (sorted(list(map(int, f.readlines()))), 2020)
    for i in range(0, len(data) -3):
        solve(data, i + 1, target - data[i], data[i])
