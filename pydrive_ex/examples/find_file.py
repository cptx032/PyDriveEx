# -*- coding: utf-8 -*-
## @package pydrive_ex.examples.find_file
#
#  Quick start guide for finding a file.
#  @author      tody
#  @date        2016/03/15

from pydrive_ex.drive import GoogleDrive

gdrive = GoogleDrive()          # Create Google Drive instance with default setting.
gfile = gdrive.file("gimages/TestImage.png")  # Find a file with the given file path.

## Print Google Drive file attributes.
print gfile
print " title        : ", gfile.title
print " file_path    : ", gfile.file_path
print " file_size    : ", gfile.file_size
print " isDir        : ", gfile.isDir()
print " isFile       : ", gfile.isFile()
print " id           : ", gfile.id
print " mime_type    : ", gfile.mime_type
print " created_date : ", gfile.created_date
print " modified_date: ", gfile.modified_date
