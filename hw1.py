import random
import numpy as np
import pandas as pd

def Simulate(n):
    Res=[]
    for i in range(10000):
        Res.append(np.sqrt(sum(i*i for i in [(random.uniform(0,1)-random.uniform(0,1))for i in range(n)])))
        #Generate a series of difference between two uniform random value in N dimension.
    return Res

N = [2,5,10,20,40,60,80,100, 200, 400, 600, 800, 1000]#the range of dimensions
Res=pd.DataFrame([],index=range(10000))#Build a dataframe to save data

for n in N:
    Res[str(n)]=Simulate(n)#Save simulated data
    
print(Res.head())#Show the first 5 row