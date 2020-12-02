#!/usr/local/bin/python3
target = 2020
with open("day01a.txt",'r') as f:
    data =  sorted(list(map(int, f.readlines())))
    low, high = (0, len(data) - 1)
    while(low < high):
        if (data[low] + data[high] == target):
            print(data[low]*data[high])
            quit()
        elif (data[low] + data[high] < target):
            low += 1
        else:
            high -= 1
