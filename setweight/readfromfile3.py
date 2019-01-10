import csv
import numpy as np
     

def readfl(fil):
    csvf=open(fil,'r')
    csvRD=csv.reader(csvf,delimiter=',')
    
    
    data=[]
    for row in csvRD:
        intdata=[]
        for col in row:
            
            intdata.append(float(col))
        data.append(intdata)
    
    return data
    csvf.close()

def sweight_max(v):
    hash1=np.zeros(dim, dtype=np.float)
    i=0
    while i<len(v):
        idx=int(v[i])
        hash1[idx]=v[i+1]
        i=i+2
    return hash1

names=['FordA2','CinCECGtorso','Url','Rcv','News20',
       'Webspam','Realsim','kdda2010','Syn','HandOutlines2']
dm=[500,10000,8737,34464,197415,
    100,7693,86293,10,2709]
#dm=[10000,10000,3231961,47236,1355191,16609143,20958,20216830,10]
indd=7
dim=dm[indd]

fl=names[indd]+'train.txt'


train=readfl(fl)
fl=names[indd]+'test.txt'
test=readfl(fl)

trinst=len(train)
tinst=len(test)

print("size of training",trinst)
print("size of testing",tinst)

ps=0

for i in range(trinst):
    if train[i][0]==1.0:
        ps=ps+1
print("training positive=",ps)

ps=0
for i in range(tinst):
    if test[i][0]==-1.0:
        ps=ps+1
print("testing positive=",ps)
maxi=np.zeros(dim,dtype=np.float)
for i in range(trinst):
    j=1
    while j<len(train[i][1:]):
        indx=int(train[i][j])
        maxi[indx]=max(maxi[indx],train[i][j+1])
        j=j+2
        

for i in range(tinst):
    j=1
    while j<len(test[i][1:]):
        indx=int(test[i][j])
        maxi[indx]=max(maxi[indx],test[i][j+1])
        j=j+2

flg=0
for i in range(dim):
    if maxi[i]==0.0:
        flg=1
        break
   
if flg==0:
    print("size of features",len(maxi))
