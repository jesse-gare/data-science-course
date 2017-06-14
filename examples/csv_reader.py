import csv
with open('EOD-KO.csv','r') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=',')
     for row in spamreader:
         print('|'.join(row))
