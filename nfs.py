import numpy as np
import math
import random
from im import *
##############################
# Input
##############################
def nfs(m):
    with open(m) as fm:
        content = fm.readlines()
        n = [x.strip() for x in content]
    s = [int(k) for k in n[0].split()]
    out = []
    for j in range(1,s[0]+1):
        t = [float(k) for k in n[j].split()]
        out.append(np.resize(t,(s[1],4)).tolist())
    return out
#########
def nf(o,c):
#    o = int(input("Number of objects: "))
#    c = int(input("Number of criteria: "))
#    s = int(input("Seed: "))
    random.seed(7)
    out = []
    for i in range(c):
        out_c = []
        for j in range(o):
            out_o = []
            for k in range(4):
                if k == 0:
                    out_o.append(random.randint(1,9)/10)
                else:
                    out_o.append(random.randint(1,9)/10)
            out_c.append(out_o)
        out.append(out_c)
    return out
##############################
# NF-matrix to RNF-matrix
##############################
def neg(a):
    out = []
    for i in range(len(a)):
        out.append([1-j for j in a[i]])
    return out
#########
def rnf(a,m):
    out = []
    for i in range(len(a)):
        if i in m:
            out.append(neg(a[i]))
        else:
            out.append(a[i])
    return out
##############################
# Entropy
##############################
def ecj(a,k):
    ac = []
    for i in range(len(a)):
        ac.append([1-j for j in a[i]])
    t = 0
    for i in range(len(a)):
        t += sim(a[i],ac[i])[k]
    out = t/len(a)
    return out
#########
def ej(a,k):
    out = []
    for i in range(len(a)):
        out.append(ecj(a[i],k))
    return out
##############################
# Cross Entropy
##############################
def ccj(a,k):
    out = []
    for i in range(len(a)):
        temp = 0
        for j in range(len(a)):
            temp += 1-sim(a[i],a[j])[k]
        out.append(temp/(len(a)-1))
    return out
#########
def cj(a,k):
    out = []
    for i in range(len(a)):
        out.append(np.mean(ccj(a[i],k)))
    return out
##############################
# Weight
##############################
def w(a,k):
    temp = []
    for i in range(len(a)):
        temp.append(1-ej(a,k)[i]+cj(a,k)[i])
    out = [i/np.sum(temp) for i in temp]
    return out
##############################
# Ranking
##############################
def Spos(a,k):
    pos = [1,1,0,0]
    out = []
    for i in range(np.array(a).shape[1]):
        temp = 0
        for j in range(np.array(a).shape[0]):
            temp += w(a,k)[j]*sim(a[j][i],pos)[k]
        out.append(temp)
    return out
#########
def Sneg(a,k):
    neg = [0,0,1,1]
    out = []
    for i in range(np.array(a).shape[1]):
        temp = 0
        for j in range(np.array(a).shape[0]):
            temp += w(a,k)[j]*sim(a[j][i],neg)[k]
        out.append(temp)
    return out
#########
def S(a,k):
    out = []
    for i in range(np.array(a).shape[1]):
        out.append(Spos(a,k)[i]/(Sneg(a,k)[i]+Spos(a,k)[i]))
    return out
##############################
# Result
##############################
def rank(a,k):
    out = np.argsort(S(a,k))+1
    return out
#########
def alt(a,k):
    out = rank(a,k)[-1]
    return out

