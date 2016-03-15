
# -*- coding: utf-8 -*-
## @package pydrive_ex.examples.upload_file
#
#  Quick start guide for uploading a new file.
#  @author      tody
#  @date        2016/03/15

from pydrive_ex.drive import GoogleDrive

gdrive = GoogleDrive()          # Create Google Drive instance with default setting.
txt_file = gdrive.createFile("Hello.txt")   # Create Google Drive File instance with 'Hello.txt'
txt_file.setContentString("Hello World!\n") # Set the content string of the file.
txt_file.upload()                           # Upload the text file.

image_file = gdrive.createFile("gimages/TestImage.png")       # Create Google Drive File instance with 'TestImage.png'
image_file.setContentFile("images/TestImage.png") # Specify the local file.
image_file.upload()                               # Upload the text file.

# For more convenient, GoogleDrive object has uploadFile function.
gdrive.uploadFile("gimages/TestImage.png", "images/TestImage.png")

print gdrive.listdir()          # Print the file list.