# -*- coding: utf-8 -*-
## @package pydrive_ex.examples.delete_file
#
#  Quick start guide for deleting a file.
#  @author      tody
#  @date        2016/03/15

from pydrive_ex.drive import GoogleDrive

gdrive = GoogleDrive()          # Create Google Drive instance with default setting.

gdrive.deleteFile("Hello.txt")  # Delete Google Drive File with 'Hello.txt'
gdrive.deleteFile("gimages")    # You can specify Google Drive Directory with 'gimages'

print gdrive.listdir()          # Print the file list.
