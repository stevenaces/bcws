import csv
import numpy as np

def testfl(nm,db):
    fll=nm+"test.txt"
    saveFile=open(fll,'a')
    for i in range(len(db)):
        if i==len(db)-1:
            saveFile.write(db[i]+'\n')
        else:
            saveFile.write(db[i]+',')
    saveFile.close()
    
def trainfl(nm,db):
    fll=nm+"train.txt"
    saveFile=open(fll,'a')
    for i in range(len(db)):
        if i==len(db)-1:
            saveFile.write(db[i]+'\n')
        else:
            saveFile.write(db[i]+',')
    saveFile.close()


    
names=['Artif1','Artif2','Url2','Rcv2','News202','Webspam','Realsim','Syn']

indd=5


pc=0
nc=0
fl=names[indd]+'.txt'
csvf=open(fl,'r')
csvRD=csv.reader(csvf,delimiter=',')
for row in csvRD:
    #print(len(row))
    #print(row[0])
    #setonlytrain(names[indd],row)
    #break
    if row[0]=='1.0':
        pc=pc+1
    else:
        nc=nc+1
    if pc<=400 and row[0]=='1.0':
        trainfl(names[indd],row)
    elif nc<=400 and row[0]=='-1.0':
        trainfl(names[indd],row)
    else:
        testfl(names[indd],row)
    
        
csvf.close()

