import numpy as np
import time
import cws
import timetak
import random


def genrand(nhash):
    alg=4
    r1 =np.zeros((maxh,dim),dtype=np.float)
    r2=np.zeros((maxh,dim),dtype=np.float)
    r=np.zeros((maxh,dim),dtype=np.float)
    c1=np.zeros((maxh,dim),dtype=np.float)
    c2=np.zeros((maxh,dim),dtype=np.float)
    c=np.zeros((maxh,dim),dtype=np.float)
    cr=np.zeros((maxh,dim),dtype=np.float)
    b =np.zeros((maxh,dim),dtype=np.float)
    alg_ttak=np.zeros((alg,nhty),dtype=np.float)
    
    i=0
    for j in range(nhty):
        flg=0
        while i<nhash:
            generator = np.random.RandomState(seed[i])
            
            start=time.time()
            r1[i] = generator.uniform(0, 1, dim).astype(np.float)
            r2[i] = generator.uniform(0, 1, dim).astype(np.float)
            c1[i] = generator.uniform(0, 1, dim).astype(np.float)
            b[i] = generator.uniform(0, 1, dim).astype(np.float)
            end=time.time()
            c_all=end-start

            start=time.time()
            c2[i] = generator.uniform(0, 1, dim).astype(np.float)
            end=time.time()
            o_i=end-start
            
            start=time.time()
            r[i]=r1[i]*r2[i]
            end=time.time()
            c_inp=end-start
            
            start=time.time()
            c[i]=c1[i]*c2[i]
            end=time.time()
            c_inc=end-start
            
            start=time.time()
            cr[i]=np.sqrt(r1[i])
            end=time.time()
            o_c=end-start

            if flg==0:
                o_b=c_all+c_inp+c_inc+o_i
                flg=1
            alg_ttak[1][j]+=c_all+c_inp
            alg_ttak[2][j]+=c_all+c_inp+c_inc+o_i
            alg_ttak[3][j]+=c_all+c_inc+o_c
            #print(alg_ttak[1])
            i=i+1
        nhash=nhash*2
        alg_ttak[0][j]=o_b
        
        
    #print(alg_ttak[0])
    #print(alg_ttak[1])
    for j in range(1,nhty):
        alg_ttak[1][j]+=alg_ttak[1][j-1]
        alg_ttak[2][j]+=alg_ttak[2][j-1]
        alg_ttak[3][j]+=alg_ttak[3][j-1]
    #print(alg_ttak[0])
    #print(alg_ttak[1])

    
        
    cws.r=r
    cws.b=b
    cws.c=c
    cws.c1=c1 #pcws
    cws.r1=r1 #pcws
    cws.cr=cr #r for ccws
    
    return alg_ttak

def chnh(nh):
    cws.nhash=nh
    uni=set(np.arange(nh))
    cws.uni=uni
    cws.hty=hty
    #cws.std_sz=std_sz
    
def gjs_fset(v1, v2):
    vec1=sweight_vect(v1)
    vec2=sweight_vect(v2)
    min_sum=0
    max_sum=0
    for i in range(dim):
        min_sum = min_sum+np.minimum(vec1[i], vec2[i])
        max_sum = max_sum+np.maximum(vec1[i], vec2[i])     
    if max_sum==0:
        return 0
    else:
        return float(min_sum) / float(max_sum)

def sweight_vect(v):
    hash1=np.zeros(dim, dtype=np.float)
    i=0
    while i<len(v):
        idx=int(v[i])
        hash1[idx]=v[i+1]
        i=i+2
    #print("hi")
    #print(hash1[366])
    return hash1

def gjs_fvec(v1, v2):
    start=time.time()
    min_sum=0
    max_sum=0
    for i in range(dim):
        min_sum = min_sum+np.minimum(v1[i], v2[i])
        max_sum = max_sum+np.maximum(v1[i], v2[i])
    end=time.time()
    timetak.tt=end-start
    if max_sum==0:
        simv= 0
    else:
        simv= float(min_sum) / float(max_sum)
    return round(simv,4)

def gjs_fvec_neg(v1, v2):
    min_sum=0
    max_sum=0
    
    for i in range(len(v1)):
        if v1[i]<0:
            a=0
        else:
            a=v1[i]
            
        if v2[i]<0:
            b=0
        else:
            b=v2[i]
        min_sum = min_sum+np.minimum(a, b)
        max_sum = max_sum+np.maximum(a, b)  
            
    if max_sum==0:
        sivm=0
    else:
        simv= float(min_sum) / float(max_sum)
    return round(simv,4)

    
def egjs_list(v1,v2):
    start=time.time()
    intersection=0
    for k in range(len(v1)):
        if np.array_equal(v1[k],v2[k]):
            intersection += 1
            
    end=time.time()
    timetak.tt=end-start
    #print(intersection/len(v1))
    return intersection


def egjs_num(v1,v2):
    start=time.time()
    intersection=0
    for k in range(len(v1)):
        if v1[k]==v2[k]:
            intersection += 1
            
    end=time.time()
    timetak.tt=end-start
    return intersection

def setdimseed(seed,dim):
    cws.seed=seed
    cws.dim=dim
    
def selhash(hs,v,ic,hidx):
    if ic==0:
        cws.bcws_set(hs,v,hidx)
    elif ic==1:
        cws.pcws_set(hs,v, hidx)
    elif ic==2:
        cws.icws_set(hs,v, hidx)
    else:
        cws.ccws_set(hs,v,hidx)

def bhash(hs,v,ic):
    if ic==0:
        cws.bcws(hs,v)
        
if __name__== "__main__":
    main()  

