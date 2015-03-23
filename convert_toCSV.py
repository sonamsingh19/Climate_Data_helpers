# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 00:53:15 2015

@author: sonam
"""

from netCDF4 import Dataset
import os 
import pandas as pd
import numpy as np
import csv
from multiprocessing import Process
import os
import sys



def to4dim_csv(ncf_var, var_name, filename):
      var = ncf_var.variables[var_name] #e.g. data for 'H2O' values
      shapes = var.shape #variable dimension shape e.g. (551,42,94)
      dims = var.dimensions #dimensions e.g. (time,lat,lon)
     
      data = [ (ncf_var.variables[dims[0]][i], ncf_var.variables[dims[1]][j], ncf_var.variables[dims[2]][k], ncf_var.variables[dims[3]][l],\
        var[i,j,k,l]) for l in xrange(shapes[3]) for k in xrange(shapes[2]) for j in xrange(shapes[1]) for i in range(shapes[0])]
      
      cols = list(dims)
      cols.append(var_name)
      pd.DataFrame(data).to_csv(filename+ var_name+ '.csv', index = False, headers = cols)
      
def to_3dim(ncf_var, var_name, filename):
      var = ncf_var.variables[var_name] #e.g. data for 'H2O' values
      shapes = var.shape #variable dimension shape e.g. (551,42,94)
      dims = var.dimensions #dimensions e.g. (time,lat,lon)
      print var,shapes, dims
      data = [ (ncf_var.variables[dims[0]][i], ncf_var.variables[dims[1]][j], ncf_var.variables[dims[2]][k],var[i,j,k]) \
      for k in xrange(shapes[2]) for j in xrange(shapes[1]) for i in range(shapes[0])]
     
      cols = list(dims)
      cols.append(var_name)
      pd.DataFrame(data).to_csv(filename+ var_name+ '.csv', index = False, headers = cols)
                 
def process_netcdf_to_csv(filename):
    dataset = Dataset(filename, diskless = True)
    
    for var_name in dataset.variables:
       print var_name
       if len(dataset.variables[var_name].shape)==3:
           to_3dim(dataset, var_name, filename )
           print var_name,"3"
       else:
        if len(dataset.variables[var_name].shape)==4:
                to4dim_csv(dataset, var_name, filename )
                print var_name, "4"
            
   


if __name__ == "__main__":
         

          filename= sys.argv[1]

          process_netcdf_to_csv(filename)
         
#         dirs = os.listdir(os.getcwd())
#         files=  [d for d in dirs if ( (not os.path.isdir(d)) and  d.endswith('.nc'))]
#         datasets= [Dataset(f, 'r') for f in files[:3]]
#         r = Parallel(n_jobs=-1, verbose=5) (delayed(process_netcdf_to_csv)(ds) for ds in datasets  )
#          filename ="MERRA100.prod.assim.inst6_3d_ana_Np.19790101.hdf.nc"
#          ncf_var = Dataset(filename,diskless=True)
#          var_name="SLP"
#          var = ncf_var.variables[var_name] #e.g. data for 'H2O' values
#          shapes = var.shape #variable dimension shape e.g. (551,42,94)
#          dims = var.dimensions #dimensions e.g. (time,lat,lon)
#          d=[]
#          for i in range(shapes[0]):
#               for j in xrange(shapes[1]):
#                   for k in xrange(shapes[2]):
#                       d.append(( i,j,k))
#                       data = [ var[i,j,k]   for k in xrange(shapes[2]) for j in xrange(shapes[1]) for i in range(shapes[0])]
#   
#    
#   
#   
#          data = [ (i,j,k)      for k in xrange(shapes[2]) for j in xrange(shapes[1]) for i in range(shapes[0])]
#   
#    
   