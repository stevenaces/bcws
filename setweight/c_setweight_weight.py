import csv
import os,sys
import numpy as np


def wf_setweight(db):
    saveFile=open(wfl,'a')
    cl=int(db[0])
    saveFile.write(str(cl))
    i=1
    while i< len(db):
        if db[i]>0:
            saveFile.write(','+str(i-1)+','+str(db[i]))
        i=i+1
        
    saveFile.write('\n')       
    saveFile.close()


    
def readfl(rfl):
    curpath = os.path.abspath(os.getcwd())
    newpath=os.path.split(curpath)
    tarpath=os.path.join(newpath[0],'weight',rfl)
    
    data=[]
    csvf=open(tarpath,'r')
    csvRD=csv.reader(csvf,delimiter=',')
    
    
    data=[]
    for row in csvRD:
        intdata=[]
        for col in row:
            intdata.append(float(col))
        data.append(intdata)
    
    return data
    csvf.close()
    
names=['CinCECGtorso','Rcv','News20','Webspam2','Realsim2','Syn']
#dm=[8737,10635,197415,100,7693,10]


indd=0


wfl=names[indd]+'train.txt'

train=readfl(wfl)
trinst=len(train)

for i in range(trinst):
    wf_setweight(train[i])
    
wfl=names[indd]+'test.txt'
test=readfl(wfl)
tinst=len(test)

for i in range(tinst):
    wf_setweight(test[i])
 
