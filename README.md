# photo-organizer

**Code to re-organize photo libraries. Photos/Videos are renamed to their creation DateTime using the following format `YYYY-MM-DD_HHMMSSa.jpg/png/mp4/mov/etc`, where `a` stands for a letter which is incremented whenever there are more than one Photo/Video for a given DateTime. New library is oranized in a tree by calendar-month `YYYY/MM`.**


## Step-00
Import directory tree of photo library with photos and videos

## Step-01
Flatten directory structure with `step01-flattenDirectories.py`
A unique increamental number is added to the filename to avoid accidental deletion of duplicate filenames in the tree.
Make all file extensions lowercase using regex:

`rename 's/\.JPG$/.jpg/' *.JPG`

Separate files into directories by file extension

## Step-02
Automatically rename files to their caputre DateTime with `step02-PhotoRenameDateTimeOriginal.py`
Define an input, output (for correctly dated photos), zerodir (for photos with `DateTime == 0000-00-00 00:00:00`), and fileextension.
Photos without defined DateTime will not be moved.

## Step-03
Create DateTimes for photos with no DateTimes based on Directory Name (which should be the Date in YYYY-MM-DD format), Time will be increamented for each photograph by a second starting from 00:00:00.

(a) For a single directory use `step03a-SingleFolderNameToPhotoDateTimeOriginal.py` after defining the inputdir (date) and fileextension.

(b) For multiple dates, place all date-directories inside a directory (inputdir) and run `step03b-MultipleFolderNameToPhotoDateTimeOriginal.py` after defining inputdir and fileextension.
