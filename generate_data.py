import random
import csv
import string

def buildUnique(maxTuples, rand):
    list = [i for i in range(0,maxTuples)]
    if rand:
        random.shuffle(list)
    #print(list)
    return list

def buildModlist(unique1, modValue):
    list = []
    for i in unique1:
        list.append(i % modValue)
    #print(list)
    return list

def buildPercent(onePercent, even):
    list = []
    for i in onePercent:
        if even:
            list.append(i * 2)
        else:
            list.append((i * 2) + 1)
    #print(list)
    return list

def convert(unique):
    i = 6
    rem = 0
    tmp = ""
    while unique > 0:
        rem = unique % 26
        tmp = chr(ord('A') + rem) + tmp
        unique //= 26
        i -= 1
    tmp = "A"*i + tmp
    return tmp


def buildString(unique):
    list = []
    for i in unique:
        converted = convert(int(i))
        list.append(converted + "x"*45)
    return list

def buildString4(size):
    list = []
    list.append("A"*4 + "x"*45)
    list.append("H"*4 + "x"*45)
    list.append("O"*4 + "x"*45)
    list.append("V"*4 + "x"*45)
    c = 0
    string4 = []
    while c < size:
        string4.append(list[c%4])
        c += 1
    #print (string4)
    return string4
    
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
    stringu1 = buildString(unique1)
    stringu2 = buildString(unique2)
    string4 = buildString4(size)
    
    list = []

    with open('test_data.csv',mode='w',newline='') as testFile:
        #add 7 to list, write row to csv
        i = 0
        while i < size:
            list.append([])
            list[i].append(unique1[i])
            list[i].append(unique2[i])
            list[i].append(two[i])
            list[i].append(four[i])
            list[i].append(ten[i])
            list[i].append(twenty[i])
            list[i].append(onePercent[i])
            list[i].append(tenPercent[i])
            list[i].append(fiftyPercent[i])
            list[i].append(unique3[i])
            list[i].append(evenOnePercent[i])
            list[i].append(oddOnePercent[i])
            list[i].append(stringu1[i])
            list[i].append(stringu2[i])
            list[i].append(string4[i])               
            i += 1 

        wr = csv.writer(testFile,quoting=csv.QUOTE_ALL)
        i = 0
        while i < size:
            wr.writerow(list[i])
            i += 1


def main():
    buildLists(50)

if __name__ == '__main__':
    main()