#here we define every function to get basic stats
import pandas as pd
# --------- MIN-----------------
def fmin(a):
    x=min(a)
    return x
# ----MAX-----------------
def fmax(a):
    x=max(a)
    return x

#----------range------------
def frange(a):
    x=fmax(a)-fmin(a)
    return x
#------------MEAN-----------
def fmean(a):
    x=sum(a)/len(a)
    return x

#------------median---------
def fmed(a):
    x=len(a)
    #odd
    if x%2!=0:
        x1=int((x-1)/2)
        return a[x1]
    else:
        x1=int(x/2) - 1
        x2=((a[x1+1]+a[x1])/2)
        return x2
    
'''l1=[10,20,30]
l2=[10,20,30,30]

#testing

print(fmean(l2),fmed(l2),fmin(l2),fmax(l2),frange(l2))
print(fmean(l1),fmed(l1),fmin(l1),fmax(l1),frange(l1))'''

#-------MODE---------
def fmod(a):
    #mode -- no havong max freq
    #pandas value count is used

    df=pd.Series(a)
    print(df)
    c=pd.DataFrame(df.value_counts())
    print(c)
    d=c[df.iloc[:,0]==df.iloc[0,0]]
    print(d)
fmod([10,20,30,30,40,40])







