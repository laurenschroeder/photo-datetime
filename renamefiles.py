# -*- coding: utf-8 -*-
"""
Created on Sun Nov 06 16:52:16 2016

@author: schro

Renames .jpg files with a timestamp. Useful to understand which photos were
taken on the same day.

To use, just replace the folder location in lines 12 and 19
     with the location of the files.
 +1 was added to the year to adjust for an error with my file creation dates
     
It will replace the name of all files in the folder 
with timestamp in the format:
YYYY-MM-DD-HR-MN-SC
"""

import os
import time
filelist=os.listdir(r"C:\Users\schro\Desktop\Photographs\Oct18")
#r tells python to interpret it as a string and nothing else

for x in filelist:
    filey=str(x)


    pathy='C:\Users\schro\Desktop\Photographs\Oct18\\'
    total=pathy+filey
    timey=os.path.getctime(pathy+x)
    realtime=time.localtime(timey)
    
    year=realtime[0]+1
    month=realtime[1]
    day=realtime[2]
    hour=realtime[3]
    minute=realtime[4]
    second=realtime[5]

    namey=str(year)+'-'+str(month)+'-'+str(day)+'-'+str(hour)+'-'+str(minute)+'-'+str(second)
    print pathy+namey+'.jpg'
    os.rename(pathy+x,pathy+namey+'.jpg')
    
  