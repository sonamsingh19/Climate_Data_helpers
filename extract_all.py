
import os 
import pandas as pd
import numpy as np
from functools import partial
from multiprocessing.dummy import Pool
from subprocess import call
def chunker(seq, size):
    return (seq[pos:pos + size] for pos in xrange(0, len(seq), size))
    
if __name__ == '__main__':
     data_Folder = 'data'
     dirs = os.listdir(os.path.join(os.getcwd(), data_Folder))
     files=  [d for d in dirs if ( (not os.path.isdir(d)) and  d.endswith('.nc'))]
     
     commands =[]
     for filename in files:
              
               commands.append( "python convert_toCSV.py " + os.path.join( data_Folder,filename)  )
            
    

     pool = Pool(1) # two concurrent commands at a time
     for i, returncode in enumerate(pool.imap(partial(call, shell=True), commands)):
        if returncode != 0:
           print("%d command failed: %d" % (i, returncode))
     for d in dirs:
         if ( (not os.path.isdir(d)) and  d.endswith('.nc')):
             print d