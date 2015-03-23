# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 00:16:03 2015

@author: sonam
"""

import os 
import pandas as pd
import numpy as np
from subprocess import call
def absoluteFilePaths(directory):
   for dirpath,_,filenames in os.walk(directory):
       for f in filenames:
           yield os.path.abspath(os.path.join(dirpath, f))
if __name__ == "__main__":
    
    dirs = os.listdir(os.getcwd())
    dirs=  [d for d in dirs if os.path.isdir(d)]
    for d in dirs:
        
        g=[x for x in absoluteFilePaths(d)]
        for path in g:
            if path.endswith(".grb2"):
                
                newPath= os.path.join("total",os.path.basename(path)[:-4]+"nc")
                
                command = "java -Xmx512m -classpath netcdfAll-4.5.jar ucar.nc2.dataset.NetcdfDataset -in "+ path +" -out "+newPath
    
                return_code = call(command, shell=True) 
                print return_code