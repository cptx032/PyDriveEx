# -*- coding: utf-8 -*-
## @package pydrive_ex.examples.quick_start
#
#  Quick start guide for pydrive_ex package.
#  @author      tody
#  @date        2016/03/15

from pydrive_ex.drive import GoogleDrive

gdrive = GoogleDrive()          # Create Google Drive instance with default setting.
gfile_list = gdrive.listdir()   # Get the file list of the root directory.
print gfile_list                # Print the file list.
