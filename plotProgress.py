#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 02:18:05 2018

@author: biprodip
"""

def plotProgress(som,rMap,cMap):  
 import matplotlib.pyplot as plt
 import numpy as np  
 
 color=np.array([]);
 x=np.array([]);
 y=np.array([]);

 for tx in range(rMap):
   for ty in range(cMap):    
    x=np.append(x,tx);
    y=np.append(y,ty);
    color=np.append(color,som[:,tx,ty]); ####
 
 chkRes=color>1;   
 if(color[chkRes].shape):
   print("RGB value in SOM >1");
   maxVal=color.max(axis=0)
   color=color/maxVal   
 
## color=color.reshape(25,3);######
 color=color.reshape(rMap*cMap,3);######
 [fig, ax] = plt.subplots();
 ax.scatter(x, y, s=420, facecolors=color);
 plt.show();
   
 return 0;
 
 