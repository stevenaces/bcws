import time
import csv

def setonly(db):
    sett=[]
    j=0
    while j<len(db):
        sett.append(db[j])
        j=j+2
    return sett


data=[]
csvf=open('rcvtest.txt','r')
csvRD=csv.reader(csvf,delimiter=',')

start=time.time()
for row in csvRD:
    st=setonly(row)
end=time.time()
print(end-start)
