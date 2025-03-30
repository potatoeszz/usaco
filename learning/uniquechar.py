"""
Given a string, e.g. "elephant"
Write a program (function) to find the first unique character in this string

"elephant" -> 'l'
"maggie" -> 'm'
"Gloria" -> 'G'
"aaaaa" -> ''
"""
from collections import defaultdict

def findUseDict(input):
    charDict = defaultdict(int)
    for c in input:
        charDict[c] += 1
    
    for c in input:
        if charDict[c] == 1:
            return c


def findUniqueChar(input):
    for i in input:
        if input.count(i) == 1:
            return i
        