import numpy as np
import time
import timetak
import math

def bcws_set(hs,st,hidx):
    start=time.time()
    i=hidx
    lbin=np.floor(dim/nhash)
    a = np.zeros(nhash, dtype=np.float)
    
    for k in range(nhash):
        hs[k][0]=-1
        hs[k][1]=-1
        a[k]=math.inf
    j=0
    nep=set()
    while j<len(st):
        p=int(st[j])
        hdx=int(np.floor(p/lbin))
        nep.add(hdx)
        if hdx>nhash-1:
            hdx=nhash-1
        t= np.floor((np.log(st[j+1])/ -np.log(r[i][p])) + b[i][p])#u1[p]*u2[p]
        y= np.exp((t - b[i][p]) * -np.log(r[i][p]))
        aint= -np.log(c1[i][p])*r1[i][p]/y
        
        if aint<a[hdx]:
            a[hdx]=aint
            hs[hdx][0]=p
            hs[hdx][1]=int(y)
        j+=2
    ep=uni-nep
    densify(ep,hs)
    end=time.time()
    timetak.tt=end-start

def bcws_set1(hs,st,hidx):
    start=time.time()
    if hty==0:
        nh=nhash
    else:
        nh=int(nhash/2)
    i=hidx
    lbin=np.floor(dim/nh)
    a = np.zeros(nh, dtype=np.float)
    
    for k in range(hidx,nhash):
        hs[k][0]=-1
        hs[k][1]=-1
        a[k-hidx]=math.inf
    j=0
    nep=set()
    while j<len(st):
        p=int(st[j])
        hdx=int(np.floor(p/lbin))
        nep.add(hdx+hidx)
        if hdx>nh-1:
            hdx=nh-1
        t= np.floor((np.log(st[j+1])/ -np.log(r[i][p])) + b[i][p])#u1[p]*u2[p]
        y= np.exp((t - b[i][p]) * -np.log(r[i][p]))
        aint= -np.log(c1[i][p])*r1[i][p]/y
        
        if aint<a[hdx]:
            a[hdx]=aint
            hs[hdx+hidx][0]=p
            hs[hdx+hidx][1]=int(y)
        j+=2
    ep=uni-nep
    densify(ep,hs)
    end=time.time()
    timetak.tt=end-start



def icws_set(hs,st,hidx):
    
    start=time.time()
    
    for i in range(hidx,nhash):
        amax=math.inf
        j=0
        while j<len(st):
            p=int(st[j])
            t= np.floor((np.log(st[j+1])/ -np.log(r[i][p])) + b[i][p])#u1[p]*u2[p]
            y= np.exp((t - b[i][p]) * -np.log(r[i][p]))
            aint= -np.log(c[i][p])*r[i][p]/y
            if aint<amax:
                amax=aint
                hs[i][0]=p
                hs[i][1]=int(y)
            j+=2
        
    end=time.time()
    timetak.tt=end-start

def pcws_set(hs,st,hidx):
    start=time.time()
    for i in range(hidx,nhash):
        amax=math.inf
        j=0
        while j<len(st):
            p=int(st[j])
            
            t= np.floor((np.log(st[j+1])/ -np.log(r[i][p])) + b[i][p])#u1[p]*u2[p]
            y= np.exp((t - b[i][p]) * -np.log(r[i][p]))
            aint= -np.log(c1[i][p])*r1[i][p]/y
            if aint<amax:
                amax=aint
                hs[i][0]=p
                hs[i][1]=int(y)
            j+=2
        
    end=time.time()
    timetak.tt=end-start

def ccws_set(hs,st,hidx):
    
    start=time.time()
    for i in range(hidx,nhash):
        amax=math.inf
        j=0
        while j<len(st):
            p=int(st[j])
            t= np.floor((st[j+1]/cr[i][p]) + b[i][p])
            y= (t - b[i][p]) * cr[i][p] #cr is r for ccws
            aint= (-np.log(c[i][p])/y)-2*cr[i][p]*-np.log(c[i][p]) 
            if aint<amax:
                amax=aint
                hs[i][0]=p
                hs[i][1]=int(y)
            j+=2
        
    end=time.time()
    timetak.tt=end-start
    
def bcws( hs,v,hidx):
       
    start=time.time()
    #ndm=std_sz*(nhash-1)+dim
    lbin=int(np.floor(dim/nhash))
    bidx=0
    numbin=0
    
    empid=[]
    while numbin<nhash:
        if numbin==nhash-1:
            ed = dim
        else:
            ed=bidx+lbin
        bins = v[bidx:ed]
            
        if getnzid(bins)==False:
            hs[numbin][0], hs[numbin][1] = -1,-1
            empid.append(numbin)
            numbin=numbin+1
            bidx=bidx+lbin
            continue

        a = np.zeros(len(bins), dtype=np.float)
        y = np.zeros(len(bins), dtype=np.float)
        
        rr = r[hty][bidx:ed]
        rr1 = r1[hty][bidx:ed]
        cc1 = c1[hty][bidx:ed]
        bb = b[hty][bidx:ed]
        
        for p in range(len(bins)):
            if bins[p]>0:
                t= np.floor((np.log(bins[p])/ -np.log(rr[p])) + bb[p])#u1[p]*u2[p]
                y[p]= np.exp((t - bb[p]) * -np.log(rr[p]))
                a[p]= -np.log(cc1[p])*rr1[p]/y[p]
            else:
              a[p]=math.inf
              
        k = np.nanargmin(a)
        hs[numbin][0], hs[numbin][1] = k+bidx, int(y[k])
        
        numbin=numbin+1
        bidx=bidx+lbin
    if len(empid)>0:
        densify(empid,hs)
    end=time.time()
    timetak.tt=end-start

def pcws(hs,v,hidx):
    
    start=time.time()
    
    for i in range(hidx,nhash):
        a = np.zeros(dim, dtype=np.float)
        y = np.zeros(dim, dtype=np.float)
        for p in range(dim):
            if v[p]>0: 
                t= np.floor((np.log(v[p])/ -np.log(r[i][p])) + b[i][p])#u1[p]*u2[p]
                y[p]= np.exp((t - b[i][p]) * -np.log(r[i][p]))
                a[p]= -np.log(c1[i][p])*r1[i][p]/y[p]
            else:
                a[p]=math.inf
        k = np.nanargmin(a)
        hs[i][0]=k
        hs[i][1]=int(y[k])
    end=time.time()
    timetak.tt=end-start
         
    
def icws(hs,v,hidx):
    start=time.time()
    for i in range(hidx,nhash):
        a = np.zeros(dim, dtype=np.float)
        y = np.zeros(dim, dtype=np.float)
        
        for p in range(dim):
            if v[p]>0:             
                t= np.floor((np.log(v[p])/ -np.log(r[i][p])) + b[i][p])#u1[p]*u2[p]
                y[p]= np.exp((t - b[i][p]) * -np.log(r[i][p]))
                a[p]= -np.log(c[i][p])*r[i][p]/y[p]
                #print(y[p])
            else:
                a[p]=math.inf
        k = np.nanargmin(a)
        hs[i][0]=k
        hs[i][1]=int(y[k])
    end=time.time()
    timetak.tt=end-start
    
        
def ccws(hs,v,hidx):
    start=time.time()
    for i in range(hidx,nhash):
        a = np.zeros(dim, dtype=np.float)
        y = np.zeros(dim, dtype=np.float)      
        for p in range(dim):
            if v[p]>0:
                t= np.floor((v[p]/cr[i][p]) + b[i][p])
                y[p]= (t - b[i][p]) * cr[i][p] #cr is r for ccws
                a[p]= (-np.log(c[i][p])/y[p])-2*cr[i][p]*-np.log(c[i][p]) 
            else:
                a[p]=math.inf
            
        k = np.nanargmin(a)

        hs[i][0], hs[i][1] = k, int(y[k])
    end=time.time()
    timetak.tt=end-start

def naivdensi(hs):
    print(len(hs))
    for i in range(len(hs)):
        if hs[i][0]<0:
            generator = np.random.RandomState(seed[i])
            while(True):
                u = generator.random_integers(0,len(hs)-1, 1 )
                if hs[u[0]][0]>=0:
                    break
            hs[i][0]=hs[u[0]][0]
            hs[i][1]=hs[u[0]][1]
        
def densify(emp,hs):
    for i in emp:
        generator = np.random.RandomState(seed[i])
        while(True):
            u = generator.random_integers(0,nhash-1, 1 )
            if hs[u[0]][0]>=0:
                break
        hs[i][0]=hs[u[0]][0]
        hs[i][1]=hs[u[0]][1]

def getnzid(st):
    flg=0
    for i in range(len(st)):
        if st[i]>0:
            flg=1
            break;
    if flg==1:
        return True
    else:
        return False
     
        
if __name__== "__main__":
    
    main()    
