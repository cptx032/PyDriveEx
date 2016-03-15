# -*- coding: utf-8 -*-
## @package pydrive_ex.drive
#
#  Simple extension of pydrive.drive utility package.
#  @author      tody
#  @date        2016/03/15


import pydrive.drive
import os

from auth import GoogleAuth
from files import GoogleDriveFile, GoogleDriveFileList, FileDeleteError


## Simple extension of pydrive.drive.GoogleDrive.
#
#  By default, GoogleAuth with the current working directory is used for the authentication.
class GoogleDrive:
    def __init__(self, auth=GoogleAuth()):
        self._auth = auth
        self._drive = pydrive.drive.GoogleDrive(auth)

    ## Create file for the given file path.
    #
    #  @param  file_path  target Google Drive file path.
    #  @param  mime_type  not required. GoogleDriveFile.setContentFile automatically assign it.
    #  @retval gfile      pydrive_ex.files.GoogleDriveFile object.
    #
    #  If parent directories do not exist, they are automatically created.
    #  This method would not upload.
    def createFile(self, file_path, mime_type=None):
        parent_dir = os.path.split(file_path)[0]
        if parent_dir != "":
            if not self.exists(parent_dir):
                self.createDir(parent_dir)

        file_name = os.path.split(file_path)[1]

        file_meta = {'title': file_name}

        if mime_type is not None:
            file_meta["mimeType"] = mime_type

        if parent_dir != "":
            gdir = self.file(parent_dir)
            file_meta["parents"] = [{"kind": "drive#fileLink", "id": gdir.id}]

        gfile = self._drive.CreateFile(file_meta)
        return GoogleDriveFile(gfile, file_path=file_path)

    ## Delete file from the given file path.
    #
    #  @param  file_path  target Google Drive file path.
    def deleteFile(self, file_path):
        gfile = self.file(file_path)
        if not gfile is None:
            gfile.delete()
        else:
            raise FileDeleteError()


    ## Upload local file to Google Drive.
    #
    #  @param  google_file  target Google Drive file path.
    #  @param  local_file   target local file path.
    def uploadFile(self, google_file, local_file=None):
        gfile = self.file(google_file)
        if gfile is None:
            gfile = self.createFile(google_file)

        if local_file is not None:
            gfile.setContentFile(local_file)

        gfile.upload()

    ## Download Google Drive file to local.
    #
    #  @param  google_file  target Google Drive file path.
    #  @param  local_file   target local file path.
    def downloadFile(self, google_file, local_file):
        gfile = self.file(google_file)
        gfile.getContentFile(local_file)

    ## Create Google Drive directory for the given directory path.
    #
    #  @param dir_path    target Google Drive directory path.
    #  @retval gfile      pydrive_ex.files.GoogleDriveFile object.
    #
    #  If parent directories do not exist, they are automatically created.
    def createDir(self, dir_path):
        parent_dir = os.path.split(dir_path)[0]

        if parent_dir != "":
            if not self.exists(parent_dir):
                self.createDir(parent_dir)

        dir_name = os.path.split(dir_path)[1]

        file_meta = {'title': dir_name,
                    "mimeType": "application/vnd.google-apps.folder"}

        if parent_dir != "":
            gdir = self.file(parent_dir)
            file_meta["parents"] = [{"kind": "drive#fileLink", "id": gdir.id}]

        gfile = self._drive.CreateFile(file_meta)
        gfile.Upload()

        return GoogleDriveFile(gfile, file_path=dir_path)

    ## Get Google Drive file from the given file path.
    #
    #  @param  file_path  target Google Drive file path.
    #  @retval gfile      pydrive_ex.files.GoogleDriveFile object.
    #
    #  This method would find the first Google Drive file that has the same file path.
    def file(self, file_path):
        dir_paths = file_path.split("/")
        file_name = dir_paths[-1]
        dir_paths = dir_paths[:-1]

        parent_id = "root"
        for dir_name in dir_paths:
            file_list = self._drive.ListFile({'q': "'%s' in parents and trashed=false" %parent_id}).GetList()
            for gfile in file_list:
                if gfile['title'] == dir_name:
                    parent_id = gfile['id']

        file_list = self._drive.ListFile({'q': "'%s' in parents and trashed=false" %parent_id}).GetList()
        for gfile in file_list:
            if gfile['title'] == file_name:
                return GoogleDriveFile(gfile, file_path=file_path)

    ## Return if the given Google Drive file path exists or not.
    #
    #  @param  file_path  target Google Drive file path.
    #  @retval True       file_path exists.
    #  @retval False      file_path does not exist.
    def exists(self, file_path):
        if self.file(file_path) is not None:
            return True
        return False

    ## Return the list of Google Drive files included in the given Google Drive direcotry.
    #
    #  @param  dir_path   target Google Drive directory path.
    #  @retval gfile_list list of pydrive_ex.files.GoogleDriveFile objects.
    def listdir(self, dir_path=None):
        parent_id = "root"

        if dir_path is not None:
            parent_id = self.file(dir_path).id
        file_list = self._drive.ListFile({'q': "'%s' in parents and trashed=false" %parent_id}).GetList()
        gfile_list = []
        for gfile in file_list:
            if dir_path is not None:
                file_path = os.path.join(dir_path, gfile['title'])
            else:
                file_path = gfile['title']
            gfile = GoogleDriveFile(gfile, file_path=file_path)
            gfile_list.append(gfile)
        return GoogleDriveFileList(gfile_list)
