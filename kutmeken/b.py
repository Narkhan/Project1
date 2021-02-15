import csv
import codecs

stream = codecs.open("ez1.csv", "w", "utf-8")
f1 = open ("tochki.out","r")

with open('ez.csv', newline='') as csvfile:
    ss = csv.reader(csvfile, delimiter=',', quotechar='"')
    cnt = 0
    for row in ss:
        cnt = cnt + 1
        if(len(row) <= 2):
            continue
        for i in range(0, 5):
            stream.write('"' + row[i] + '"' + ',')
        if cnt >= 3:
            stream.write(',,,,,,' + f1.readline())
        else:
            stream.write('\n')
stream.close()
f1.close()   