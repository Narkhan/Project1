import csv
import codecs


for i in range(1, 5):
    stream = codecs.open(str(i) + ".out", "w", "utf-8")
    with open('ez.csv', newline='') as csvfile:
        ss = csv.reader(csvfile, delimiter=',', quotechar='"')
        cnt = 0
        for row in ss:
            cnt = cnt + 1
            if(len(row) <= 2):
                continue
            if cnt >= 3:
                stream.write(row[i])
                stream.write('\n')
        stream.close()
