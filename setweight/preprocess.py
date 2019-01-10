import random
import numpy as np
import gc
import time
from operator import itemgetter
import csv
import os,sys
import math





def readfl(fil):
    curpath = os.path.abspath(os.getcwd())
    newpath=os.path.split(curpath)
    tarpath=os.path.join(newpath[0],'setweight',fil)
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
    

    
def trainfl(fl,db):
    saveFile=open(fl,'a')
    for i in range(len(db)):
        if i==len(db)-1:
            saveFile.write(str(db[i])+'\n')
        else:
            saveFile.write(str(db[i])+',')
    saveFile.close()
    
names=['Artif1','Artif2','Url','Rcv','News20','Webspam','Realsim','kdd20102','Syn']
#dm=[10000,10000,3231961,47236,1355191,16609143,20958,20216830,10]
dm=[10000,10000,3231961,47236,1355191,16609143,20958,86293,10]
indd=7
dim=dm[indd]

fl=names[indd]+'train.txt'

train=[]
test=[]
train=readfl(fl)
fl=names[indd]+'test.txt'
test=readfl(fl)
        

trinst=len(train)
tinst=len(test)



maxi=np.zeros(dim,dtype=np.float)
        
for i in range(trinst):
    j=1
    #print(len(row))
    while j<len(train[i][1:]):
        indx=int(train[i][j])
        #print(indx)
        
        #print(train[i][j+1])
        maxi[indx]=max(maxi[indx],train[i][j+1])
        #print(maxi[indx])
        j=j+2
        

for i in range(tinst):
    j=1
    #print(len(row))
    while j<len(test[i][1:]):
        indx=int(test[i][j])
        
        maxi[indx]=max(maxi[indx],test[i][j+1])
        
        j=j+2
        
empid=np.zeros(dim,dtype=np.int)
emp=[]

#maxi=[0.5,0.0,0.0,7,8.3,0.0,7.9,9.8]

i=0
while i<len(maxi):
    c=i
    flg=0
    
    while maxi[c]==0.0 :
        #print(maxi[c])
        empid[i]=empid[i]+1
        
        if flg==0:
            emp.append(c)
            flg=1
        c=c+1
        if c==len(maxi):
            break
        
    if c==len(maxi):
        break
        
    if maxi[i]==0.0:
        i=c
    else:
        i=i+1

c=0
for i in emp:
    c=c+empid[i]
    empid[i]=c

print(c)

for i in range(len(maxi)):
    print(maxi[i])
print(len(maxi))


fl=names[indd]+'3train.txt'
for k in range(trinst):
    temptr=[]
    temptr.append(train[k][0])
    i=1
    j=0
    while i<len(train[k][1:]):
        print(train[k][i])
        print(k,i)
        print(emp[j])
        if train[k][i]<emp[j]:
            temptr.append(train[k][i])
            temptr.append(train[k][i+1])
        elif train[k][i]>emp[j] and j==len(emp)-1:
            temptr.append(train[k][i]-empid[emp[j]])
            temptr.append(train[k][i+1])
        elif train[k][i]>emp[j] and train[k][i]<emp[j+1]:
            temptr.append(train[k][i]-empid[emp[j]])
            temptr.append(train[k][i+1])
        else:
            j=j+1
            i=i-2
        i=i+2
    
    trainfl(fl,temptr)


fl=names[indd]+'3test.txt'


for k in range(tinst):
    tempt=[]
    tempt.append(test[k][0])
    i=1
    j=0
    while i<len(test[k][1:]):
        if test[k][i]<emp[j]:
            tempt.append(test[k][i])
            tempt.append(test[k][i+1])
        elif test[k][i]>emp[j] and j==len(emp)-1:
            tempt.append(test[k][i]-empid[emp[j]])
            tempt.append(test[k][i+1])
        elif test[k][i]>emp[j] and test[k][i]<emp[j+1]:
            tempt.append(test[k][i]-empid[emp[j]])
            tempt.append(test[k][i+1])
        else:
            j=j+1
            i=i-2
        i=i+2
    
    trainfl(fl,tempt)
        

#print(emp)
#print(empid)

#for i in maxi:
    #print(i)
    
        
    

