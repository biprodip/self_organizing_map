# -*- coding: utf-8 -*-
"""
Created on Sun May  6 10:25:28 2017

@author: biprodip
"""
import numpy as np

#input data (dx1 vector)
data = np.array(np.random.randint(0, 255, (3, 100)), dtype=float);
data.astype(float);
d = data.shape[0];
totSample = data.shape[1];

#define grid mxn (not more than totSample)
rMap=10;
cMap=10;

#initialize weights mxnxd
#random numbers between [0,1)
som=np.random.random((d,rMap, cMap))  #3 slice of 5x5  3d arrays are stored as (depth=3,row,col)

#initialize eta,rad0,totIteration,timeConstant
eta0= 0.5
totIterations = 90
rad0 = max(rMap, cMap) / 2
# radius decay parameter
time_constant = totIterations / np.log(rad0)

#normalization axis=0(column wise max,highest val of a sample)   axis=1(row wise max,highest val of an attribute)   
maxVal=data.max(axis=1)
data_tmp=data.T/maxVal
data_tmp=data_tmp.T;


data=data_tmp;

#iteration
for iteraton in range(totIterations):
  tmpMax=np.inf;
  #pick a random input data
  sampleIndex=np.random.randint(0,totSample);
  sample=data[:,sampleIndex];  #1d
 
  for r in range(rMap):   
   for c in range(cMap):    
    #find BMU
    mapNode=som[:,r,c]; #1d
    sq_dist = np.sum((sample - mapNode) ** 2)
    if(sq_dist<tmpMax):
     tmpMax=sq_dist;
     [bmuIndexR,bmuIndexC]=[r,c];
     bmu=mapNode;
    
  #update neighborhood radious
  #update eta
  rad= rad0 * np.exp(-iteraton / time_constant);
  eta  = eta0 * np.exp(-iteraton / time_constant);
  
  #update weight of BMU (move it closer to representative pattern)
  som[:,bmuIndexR,bmuIndexC]=bmu + eta*(sample-bmu);


  for x in range(rMap):
   for y in range(cMap):    
    #update weight of neighbours of BMU (move similar ones in the radious, closer to BMU thus form a similar region)
    #sampleNode is at point (x,y)  and BMU is at [bmuIndexR,bmuIndexC]   thus find the line distance
    dist = np.sum((np.array([x, y]) - [bmuIndexR,bmuIndexC]) ** 2)
    if (dist<(rad**2)):
     mapNode=som[:,x,y];
     influence = np.exp(-(dist**2) / (2* (rad**2)))
     # now update the neuron's weight using the formula:
     newMapNode = mapNode + (eta * influence * (sample - mapNode))
     # commit the new weight
     som[:,x, y] = newMapNode.reshape(1, d) 
     
     if(iteraton%10==0):
      #chk=input("Visualize progress? (1/0)");
     #if(chk):
      plotProgress(som,rMap,cMap);  