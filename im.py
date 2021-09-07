import numpy as np
import math
import random
##############################
# Similarity
##############################
def sim1(a,b):
    t = [math.sqrt(2)*math.cos((a[i]-b[i])*math.pi/4) for i in range(4)]
    out = (math.sqrt(2)+1)/4*(sum(t)-4)
    return out
#########
def sim2(a,b):
    t = [abs(a[i]-b[i]) for i in range(4)]
    out = 1-sum(t)/len(t)
    return out
#########
def sim3(a,b):
    t = [abs(a[i]-b[i]) for i in range(4)]
    out = math.log(2-sum(t)/len(t),2)
    return out
#########
def sim4(a,b):
    t = [abs(a[i]-b[i]) for i in range(4)]
    out = 1-math.log(1+sum(t)/len(t),2)
    return out
#########
def sim5(a,b):
    t = [abs(a[i]-b[i]) for i in range(4)]
    out = (math.exp(-sum(t)/len(t))-math.exp(-1))/(1-math.exp(-1))
    return out
#########
def sim6(a,b):
    t = [abs(a[i]-b[i]) for i in range(4)]
    out = 1-math.sin(sum(t)*math.pi/8)
    return out
#########
def sim7(a,b):
    t = [abs(a[i]-b[i]) for i in range(4)]
    out = math.cos(sum(t)*math.pi/8)
    return out
#########
def sim8(a,b):
    t = [abs(a[i]-b[i]) for i in range(4)]
    out = 1-math.tan(sum(t)*math.pi/16)
    return out
#########
def sim9(a,b):
    t = [abs(a[i]-b[i]) for i in range(4)]
    out = math.cos(math.pi/4+sum(t)*math.pi/16)/math.sin(math.pi/4+sum(t)*math.pi/16)
    return out
#########
def sim(a,b):
    out = [sim1(a,b),sim2(a,b),sim3(a,b),sim4(a,b),sim5(a,b),sim6(a,b),sim7(a,b),sim8(a,b),sim9(a,b)]
    return np.array(out)
##############################
# Similarity on NF-sets
##############################
def s(a,b):
    temp = np.zeros(9)
    for i in range(len(a)):
        temp += sim(a[i],b[i])
    t = temp/len(a)
    out = [round(i,3) for i in t]
    return out
##############################
# Entropy on NF-sets
##############################
def e(a):
    ac = []
    for i in range(len(a)):
        ac.append([1-j for j in a[i]])
    temp = np.zeros(9)
    for i in range(len(a)):
        temp += sim(a[i],ac[i])
    t = temp/len(a)
    out = [round(i,3) for i in t]
    return out
##############################
# Cross Entropy on NF-sets
##############################
def c(a,b):
    temp = np.zeros(9)
    for i in range(len(a)):
        temp += 1-sim(a[i],b[i])
    t = temp/len(a)
    out = [round(i,3) for i in t]
    return out
