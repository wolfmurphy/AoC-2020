#!/usr/local/bin/python3
import re
def extract_data(s):
    pattern = re.compile(r"""\s*(?P<start>\d*?)\s*?
                            -\s*?
                            (?P<end>\d*?)\s*?
                            (?P<letter>[a-zA-Z]?)\s*?
                            :\s*?
                            (?P<str>\w\w*)\s*?""", re.VERBOSE)
    match = pattern.match(s)
    start = int(match.group("start"))
    end = int(match.group("end"))
    letter = match.group("letter")
    str = match.group("str")
    match1 = int(str[start-1]==letter)
    match2 = int(str[end-1]==letter)
    return int(match1+match2==1)
with open("day02a.txt",'r') as f:
    print(sum(list(map(extract_data, f.readlines()))))
