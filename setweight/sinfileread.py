import csv
import numpy as np
     

def readfl(fil):
    
    data=[]
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

def vectoriz(v):
    hash1=np.zeros(dim, dtype=np.float)
    i=0
    while i<len(v):
        idx=int(v[i])
        #print(idx)
        hash1[idx]=v[i+1]
        i=i+2
    return hash1

names=['FordA','Gisette','Url2','Rcv2','News202',
       'Webspam','Realsim2','kdd20102','Syn','HandOutlines2']
dm=[500,5000,8737,34464,197415,
    100,7693,86293,10,2709]
#dm=[10000,10000,3231961,47236,1355191,16609143,20958,20216830,10]
indd=1
dim=dm[indd]

fl=names[indd]+'accsim.txt'

train=readfl(fl)
trinst=len(train)

print("size of training",trinst)
print('sizse of features',len(train[0]))

for i in range(dim):
    print(train[0][i])

##ps=0
##
##for i in range(trinst):
##    if train[i][0]==0.0:
##        ps=ps+1
##print("training positive=",ps)
##for i in range(trinst):
##    vec=vectoriz(train[i][1:])
##print("size of features",len(vec))
