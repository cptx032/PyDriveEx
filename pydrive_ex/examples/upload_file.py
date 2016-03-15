# -*- coding: utf-8 -*-
## @package pydrive_ex.examples.upload_file
#
#  Quick start guide for uploading a new file.
#  @author      tody
#  @date        2016/03/15

from pydrive_ex.drive import GoogleDrive

gdrive = GoogleDrive()          # Create Google Drive instance with default setting.

# Create directory.
gdrive.createDir("PDTest/TestDir")

# Upload a text file via GoogleDriveFile instance.
txt_file = gdrive.createFile("PDTest/Hello.txt", upload=False)
txt_file.setContentString("Hello World!\n") # Set the content string of the file.
txt_file.upload()                           # Upload the text file.

# Upload a image file via GoogleDriveFile instance.
image_file = gdrive.createFile("PDTest/Image/HelloImage.png", upload=False)
image_file.setContentFile("images/TestImage.png") # Specify a local file.
image_file.upload()                               # Upload the image file.

# For simpler usage, GoogleDrive object has uploadFile function.
gdrive.uploadFile("PDTest/Image/HelloImage.png", "images/TestImage.png")

# Print the file list in the given directory.
print gdrive.listdir("PDTest")