# photo-datetime
Renames .jpg folders in a file to the timestamp of creation
Useful to understand which photos were taken on the same day when browsing through a photo directory.

To use, just replace the folder location in lines 12 and 19
     with the location of the files.
     
 +1 was added to the year to adjust for an error with my personal file creation dates
     
It will replace the name of all files in the folder 
with timestamp in the format:
YYYY-MM-DD-HR-MN-SC

Example:

C:\Users\schro\Desktop\Photographs\July16\NIKON346.jpg --> C:\Users\schro\Desktop\Photographs\July16\2016-7-20-17-55-50.jpg
