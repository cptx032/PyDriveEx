# -*- coding: utf-8 -*-
## @package pydrive_ex.examples.download_file
#
#  Quick start guide for downloading a file.
#  @author      tody
#  @date        2016/03/15

from pydrive_ex.drive import GoogleDrive

gdrive = GoogleDrive()          # Create Google Drive instance with default setting.
gdrive.downloadFile("gimages/TestImage.png", "images/TestDownloadedImage.png")  # Download the Google Drive file to the local.
