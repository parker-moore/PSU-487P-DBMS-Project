import random
import csv
import string

def buildUnique(maxTuples, rand):
    list = [i for i in range(0,maxTuples)]
    if rand:
        random.shuffle(list)
    print(list)
    return list

def buildModlist(unique1, modValue):
    list = []
    for i in unique1:
        list.append(i % modValue)
    print(list)
    return list

def buildPercent(onePercent, even):
    list = []
    for i in onePercent:
        if even:
            list.append(i * 2)
        else:
            list.append((i * 2) + 1)
    print(list)
    return list
    
def buildLists(size):
    unique1 = buildUnique(size, True)
    unique2 = buildUnique(size, False)
    two = buildModlist(unique1, 2)
    four = buildModlist(unique1, 4)
    ten = buildModlist(unique1, 10)
    twenty = buildModlist(unique1, 20)
    onePercent = buildModlist(unique1, 100)
    tenPercent = buildModlist(unique1, 10)
    twentyPercent = buildModlist(unique1, 5)
    fiftyPercent = buildModlist(unique1, 2)
    unique3 = unique1.copy()
    evenOnePercent = buildPercent(onePercent, True)
    oddOnePercent = buildPercent(onePercent, False)