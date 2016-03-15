# -*- coding: utf-8 -*-
## @package pydrive_ex.examples.find_file
#
#  Quick start guide for walking Google Drive.
#  @author      tody
#  @date        2016/03/15

from pydrive_ex.drive import GoogleDrive

gdrive = GoogleDrive()          # Create Google Drive instance with default setting.

# Create test directories.
gdrive.deleteFile("WalkTest")
gdrive.createDir("WalkTest/Dir1")
gdrive.createDir("WalkTest/Dir2")
gdrive.createFile("WalkTest/Dir1/TestFile1.txt")
gdrive.createFile("WalkTest/TestFile2.txt")

# Walk Google Drive for the given directory path.
for root, gdirs, gfiles in gdrive.walk("WalkTest"):
    print root
    for gdir in gdirs:
        print gdir
    for gfile in gfiles:
        print gfile
    print ""
