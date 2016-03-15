# -*- coding: utf-8 -*-
## @package pydrive_ex.examples.delete_file
#
#  Quick start guide for deleting a file.
#  @author      tody
#  @date        2016/03/15

from pydrive_ex.drive import GoogleDrive

gdrive = GoogleDrive()          # Create Google Drive instance with default setting.

gdrive.deleteFile("PDTest/Hello.txt")  # Delete a single Google Drive File.
print gdrive.listdir("PDTest")          # Print the file list.

gdrive.deleteFile("PDTest/Image")    # Delete whole Google Drive folder.
print gdrive.listdir("PDTest")          # Print the file list.
