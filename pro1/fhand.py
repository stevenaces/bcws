import numpy as np
import csv
import os,sys

def rtovec_sweight(rfl):
    curpath = os.path.abspath(os.getcwd())
    newpath=os.path.split(curpath)
    tarpath=os.path.join(newpath[0],'setweight',rfl)
    csvf=open(tarpath,'r')
    csvRD=csv.reader(csvf,delimiter=',')
    
    data=[]
    #c=0
    for row in csvRD:
        intdata=np.zeros(dim+1,dtype=np.float)#for class also
        flg=0
        for col in row:
            if flg==0:
                intdata[0]=float(col) #put class
                flg=1
            elif flg==1:
                f=float(col)
                indx=int(f) #read index
                flg=2
                continue
            elif flg==2:
                intdata[indx+1]=float(col) #put weight
                flg=1
        #print(intdata)
        #input()
        data.append(intdata)
##        if c==20:
##            break
##        c=c+1
    
    return data
    csvf.close()

def rtoset_sweight(rfl): #reads weight as the set
    curpath = os.path.abspath(os.getcwd())
    newpath=os.path.split(curpath)
    tarpath=os.path.join(newpath[0],'setweight',rfl)
    csvf=open(tarpath,'r')
    csvRD=csv.reader(csvf,delimiter=',')
    data=[]
    for row in csvRD:
        intdata=[]
        
        for col in row:
            f=float(col)
            intdata.append(f)
            
        data.append(intdata)
    return data
    csvf.close()

def rtovec_weight(rfl): #reads weight as the vec
    curpath = os.path.abspath(os.getcwd())
    newpath=os.path.split(curpath)
    tarpath=os.path.join(newpath[0],'weight',rfl)
    csvf=open(tarpath,'r')
    csvRD=csv.reader(csvf,delimiter=',')
    data=[]
    for row in csvRD:
        intdata=[]
        
        for col in row:
            f=float(col)
            intdata.append(f)
            
        data.append(intdata)
    return data
    csvf.close()

def msewfl(errr,trtime,ttime,etime):
    saveFile=open(wfl_mse,'a')
    saveFile.write(str(errr)+',')
    saveFile.write(str(trtime)+',')
    saveFile.write(str(ttime)+',')
    saveFile.write(str(etime)+'\n')
    saveFile.close()
    
def knnwfl(errr,trtime,ttime,etime,cltime):
    saveFile=open(wfl_cl,'a')
    saveFile.write(str(errr)+',')
    saveFile.write(str(trtime)+',')
    saveFile.write(str(ttime)+',')
    saveFile.write(str(etime)+',')
    saveFile.write(str(cltime)+'\n')
    saveFile.close()
    
def topkwfl(p,flag):
    saveFile=open(wfl,'a')
    if flag==3:
        saveFile.write(str(p)+'\n')
    else:
        saveFile.write(str(p)+',')
    saveFile.close()
    
def topktm(p):
    saveFile=open('time'+wfl,'a')   
    saveFile.write(str(p)+'\n')
    saveFile.close()

def wr_accsim(rec):
    saveFile=open(wfl,'a')
    for i in range(len(rec)):
        if i==len(rec)-1:
            saveFile.write(str(rec[i])+'\n')
        else:
            saveFile.write(str(rec[i])+',')
    saveFile.close()
        


    
names=['News20','Rcv','Realsim','gisette','kdda2010',
       'Syn','Url','FordA','StarLightCurves','HandOutlines',
       'webspam','CinCECGtorso','Leukemia']
dm=[541956,34464,18517,5000,62207,
    10,52509,500,1024,2709,
    144488,1639,7129]
