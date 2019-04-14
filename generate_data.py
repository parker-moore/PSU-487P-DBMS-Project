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

def buildString(size, rand):
    alpha = [i for i in range(ord('A'),ord('W'))]
    list = []
    c = 0
    
    for i in alpha:
        for j in alpha:
            for k in alpha:
                if c < size:
                    list.append(str(chr(k)) + "x"*25 + str(chr(j)) + "x"*24 + str(chr(i)))
                    c += 1
                else:
                    break
                
    if(rand):
        random.shuffle(list)
    #print(list)
    return list

def buildString4(size):
    list = []
    list.append("A" + "x"*25 + "A" + "x"*24 + "A")
    list.append("H" + "x"*25 + "H" + "x"*24 + "H")
    list.append("O" + "x"*25 + "O" + "x"*24 + "O")
    list.append("V" + "x"*25 + "V" + "x"*24 + "V")
    c = 0
    string4 = []
    while c < size:
        string4.append(list[c%4])
        c += 1
    print (string4)
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
    stringu1 = buildString(size, True)
    stringu2 = buildString(size, False)
    string4 = buildString4(size)
    
    with open('test.csv',mode='w',newline='') as testFile:
        wr = csv.writer(testFile,quoting=csv.QUOTE_ALL)
        wr.writerow(unique1)
        wr.writerow(unique2)
        wr.writerow(two)
        wr.writerow(four)
        wr.writerow(ten)
        wr.writerow(twenty)
        wr.writerow(onePercent)
        wr.writerow(tenPercent)
        wr.writerow(twentyPercent)
        wr.writerow(fiftyPercent)
        wr.writerow(unique3)
        wr.writerow(evenOnePercent)
        wr.writerow(oddOnePercent)
        wr.writerow(stringu1)
        wr.writerow(stringu2)
        wr.writerow(string4)


def main():
    buildLists(10)

if __name__ == '__main__':
    main()