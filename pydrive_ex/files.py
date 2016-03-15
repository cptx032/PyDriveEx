# -*- coding: utf-8 -*-
## @package pydrive_ex.files
#
#  Simple extension of pydrive.files utility package.
#  @author      tody
#  @date        2016/03/15

from apiclient import errors


## Error trying to delete file that is not deletable.
class FileDeleteError(RuntimeError):
    pass


## Simple extension of pydrive.files.GoogleDriveFile.
#
#  The instance is created from pydrive_ex.drive.GoogleDrive functions.
class GoogleDriveFile:
    def __init__(self, gfile):
        self._gfile = gfile
        self.title = self._gfile['title']
        self.id = self._gfile['id']
        self.mime_type = self._gfile['mimeType']

    ## Return if the Google Drive file is directory or not.
    def isDir(self):
        return self.mime_type == "application/vnd.google-apps.folder"

    ## Return if the Google Drive file is file or not.
    def isFile(self):
        return not self.isDir()

    ## Download the content file to the give local file.
    #  @param  local_file   target local file path.
    def getContentFile(self, local_file):
        self._gfile.GetContentFile(local_file)

    ## Download the content string.
    def getContentString(self):
        self._gfile.GetContentString()

    ## Upload the local file to the Google Drive file.
    #  @param  local_file   target local file path.
    def setContentFile(self, local_file):
        self._gfile.SetContentFile(local_file)

    ## Upload the content string to the Google Drive file.
    #  @param  content_string  given string to store.
    def setContentString(self, content_string):
        self._gfile.SetContentString(content_string)

    ## Delete the file from the Google Drive.
    def delete(self):
        try:
            self._gfile.auth.service.files().delete(fileId=self.id).execute()
        except errors.HttpError, error:
            raise FileDeleteError()

    ## Upload the file to the Google Drive.
    def upload(self):
        self._gfile.Upload()

    ## Return the string representation of the Google Drive file.
    def __str__(self):
        ret_str = ""

        if self.isDir():
            ret_str += "<Dir>  "
        else:
            ret_str += "<File> "
        ret_str += self.title
        return ret_str


class GoogleDriveFileList:
    def __init__(self, gfile_list):
        self._gfile_list = gfile_list

    def __iter__(self):
        return iter(self._gfile_list)

    def numDirs(self):
        num_dirs = 0

        for gfile in self._gfile_list:
            if gfile.isDir():
                num_dirs += 1
        return num_dirs

    def numFiles(self):
        num_files = 0

        for gfile in self._gfile_list:
            if gfile.isFile():
                num_files += 1
        return num_files

    ## Return the string representation of the Google Drive file list.
    def __str__(self):
        ret_str = "%d directories, %d files.\n" %(self.numDirs(), self.numFiles())

        for gfile in self._gfile_list:
            ret_str += "  " + str(gfile) + "\n"
        return ret_str
