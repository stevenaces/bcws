import random
import numpy as np
import gc
import time
from operator import itemgetter
import timetak
import fhand
#import cws
import mapping
from scipy import stats
    
def main():
    
     '''['News20','Rcv','Realsim','gisette','kdda2010',
       'Syn','Url','FordA','StarLightCurves','HandOutlines',
       'webspam','CinCECGtorso','Leukemia']'''

     algo=['bcws','pcws','icws','ccws']
     indd=2
     bhash=8
    
     nhty=5
     mapping.nhty=nhty
     maxh=bhash*(2**(nhty-1))
     mapping.maxh=maxh
     

     dim=fhand.dm[indd]
     mapping.dim=dim
     fhand.dim=dim

     seed =np.zeros((maxh),dtype=np.int)
     for i in range(maxh):
          seed[i]=random.randint(1,10000)

     mapping.seed=seed
     mapping.setdimseed(seed,dim)

     wfl_cl='knn1.txt'
     wfl_mse='mse1.txt'
     wfl_tt='ttest.txt'
     fhand.wfl_cl=wfl_cl
     fhand.wfl_mse=wfl_mse
     rfl=fhand.names[indd]


     train=fhand.rtoset_sweight(rfl+'train.txt')
     test=fhand.rtoset_sweight(rfl+'test.txt')
     


     trinst=len(train)
     tinst=len(test)

     # for ttest
##     accsim=fhand.rtoset_sweight(rfl+'accsim.txt')
##     avaracc=np.mean(np.var(accsim,axis=1))
##     amnacc=np.mean(np.mean(accsim,axis=1))
##
##     saveFile=open(wfl_tt,'a')
##     saveFile.write(rfl+' '+'  \n')
##     saveFile.write(str(avaracc)+','+str(amnacc)+'\n')
##     saveFile.close()

     alg_ttak=mapping.genrand(bhash)
     
     trhash=np.zeros((trinst,maxh,2), dtype=np.int)
     thash=np.zeros((tinst,maxh,2), dtype=np.int)
     flg=0
     for alg in range(1,len(algo)):
          
          hidx=0
          pretrtime=0
          prettime=0
          precltime=0
          preetime=0
          nhash=bhash
          
                
          saveFile=open(wfl_cl,'a')
          saveFile.write(rfl+' '+algo[alg]+'  \n')
          saveFile.close()

          saveFile=open(wfl_mse,'a')
          saveFile.write(rfl+' '+algo[alg]+'  \n')
          saveFile.close()

          preinter=np.zeros((nhty,tinst,trinst), dtype=np.int)
          hty=0
          nrep=1
          
          while hty<nhty:

               rerr_cl=np.empty(nrep, dtype=np.float)
               rerr_mse=np.empty(nrep, dtype=np.float)
               rtrtime=np.empty(nrep, dtype=np.float)
               rttime=np.empty(nrep, dtype=np.float)
               rcltime=np.empty(nrep, dtype=np.float)
               retime=np.empty(nrep, dtype=np.float)
               rep=0
               mapping.hty=hty # only required for setreq
               mapping.chnh(nhash)
                              
               if alg==0:
                    trhash=np.zeros((trinst,nhash,2), dtype=np.int)
                    thash=np.zeros((tinst,nhash,2), dtype=np.int)

               while rep<nrep:
                    trtime=0
                    cltime=0
                    ttime=0
                    etime=0
                    for i in range(trinst):
                         mapping.selhash(trhash[i],train[i][1:],alg,hidx)
                         trtime=trtime+timetak.tt
                         #print(99)
                     
                    for i in range(tinst):
                         #vec_t=mapping.sweight_vect(test[i][1:])
                         vec_t=test[i][1:]
                         mapping.selhash(thash[i],vec_t,alg,hidx)
                         ttime=ttime+timetak.tt
                         
                     
                    
                    estsim=np.zeros((tinst,trinst),dtype=np.float)
                    pc=0
                    pi=0
                    tr_terr = []
                    for i in range(tinst):
                         es=0
                         for j in range(trinst):
                              if alg==0:
                                   curinter=mapping.egjs_list(thash[i],trhash[j])
                              else:
                                   curinter=mapping.egjs_list(thash[i][hidx:nhash],trhash[j][hidx:nhash])
                              etime=etime+timetak.tt
                             
                              # find estsim
                              if hty==0 or alg==0:
                                   estsim[i][j]=round(curinter/nhash,4)
                                   preinter[hty][i][j]=curinter
                              else:
                                   estsim[i][j]=round((preinter[hty-1][i][j]+curinter)/nhash,4)
                                   preinter[hty][i][j]=preinter[hty-1][i][j]+curinter
                              #find the 1nn
                              if estsim[i][j]>es:
                                   onnidx=j
                                   es=estsim[i][j]
                              #tr_terr.append((accsim[i][j]-estsim[i][j])**2)
                         
                         start=time.time()
                         #number of incorrectly classified
                         if test[i][0]==train[onnidx][0]:# onnidx after checking all train            
                              pc=pc+1
                         else:
                              pi=pi+1
                         end=time.time()
                         cltime=end-start
                    #avgerr = np.mean(tr_terr)

                     
                    rtrtime[rep]=trtime
                    rcltime[rep]=cltime
                    rttime[rep]=ttime
                    retime[rep]=etime
                    rerr_cl[rep]=pi/tinst
                    #rerr_mse[rep]=avgerr
                    rep+=1
          
                 
               if alg!=0:           
                    pretrtime=pretrtime+np.mean(rtrtime)
                    precltime=precltime+np.mean(rcltime)
                    prettime=prettime+np.mean(rttime)
                    preetime=preetime+np.mean(retime)

               if alg==0:
                    fhand.knnwfl(np.mean(rerr_cl),alg_ttak[alg][hty]+np.mean(rtrtime),np.mean(rttime),np.mean(retime),np.mean(rcltime))
                    #fhand.msewfl(np.mean(rerr_mse),alg_ttak[alg][hty]+np.mean(rtrtime),np.mean(rttime),np.mean(retime))
               else:
                    fhand.knnwfl(np.mean(rerr_cl),pretrtime+alg_ttak[alg][hty],prettime,preetime,precltime)
                    #fhand.msewfl(np.mean(rerr_mse),pretrtime+alg_ttak[alg][hty],prettime,preetime)
                 
               #for ttest
##               if alg==0 and nhash==128:
##                    t=0
##                    p=0
##                    for i in range(tinst):
##                         tval, pval = stats.ttest_ind(estsim[i],accsim[i],axis=0,equal_var=0)
##                         t=t+tval
##                         p=p+pval
##                    tavg=t/tinst
##                    pavg=p/tinst
##                     
##                    avarest=np.mean(np.var(estsim,axis=1))
##                    amnest=np.mean(np.mean(estsim,axis=1))
##                     
##                    saveFile=open(wfl_tt,'a')
##                    saveFile.write(str(avarest)+','+str(amnest)+'  \n')
##                    saveFile.write(str(tavg)+','+str(pavg)+'\n')
##                    saveFile.close()
               hidx=nhash   
               nhash=nhash*2
               hty=hty+1
            
               print(hty)
               gc.collect()
    
     gc.collect()
    
    
if __name__== "__main__":
    main() 
