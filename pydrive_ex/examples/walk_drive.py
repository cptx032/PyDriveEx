# -*- coding: utf-8 -*-
## @package pydrive_ex.examples.find_file
#
#  Quick start guide for walking Google Drive.
#  @author      tody
#  @date        2016/03/15

from pydrive_ex.drive import GoogleDrive

gdrive = GoogleDrive()          # Create Google Drive instance with default setting.

for root, gdirs, gfiles in gdrive.walk():
    for gdir in gdirs:
        print gdir.file_path