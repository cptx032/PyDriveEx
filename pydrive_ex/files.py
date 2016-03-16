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


## Simple extension of PyDrive GoogleDriveFile class.
#
#  The instance is created from pydrive_ex.drive.GoogleDrive functions.
#
#  Attributes:
#  - title          file name.
#  - id             file id.
#  - mime_type      mime type.
#  - file_path      file path.
#  - created_date   created date.
#  - modified_date  modified date.
#  - file_size      file size (byte).
class GoogleDriveFile:

    ## Create GoogleDriveFile instance.
    #
    #  @param gfile      original PyDrive GoogleDriveFile instance.
    #  @param file_path  file path for the Google Drive file.
    def __init__(self, gfile, file_path=""):
        self._gfile = gfile
        self.title = self._gfile['title']
        self.id = None
        self.mime_type = None
        self.file_path = file_path
        self.created_date = None
        self.modified_date = None
        self.file_size = None
        self._updateAttr()

    ## Return the original meta data of PyDrive GoogleDriveFile.
    def metaData(self):
        return self._gfile

    ## Return if the Google Drive file is directory or not.
    def isDir(self):
        return self.mime_type == "application/vnd.google-apps.folder"

    ## Return if the Google Drive file is file or not.
    def isFile(self):
        return not self.isDir()

    ## Download the content file to the give local file.
    #
    #  @param  local_file   target local file path.
    def getContentFile(self, local_file):
        self._gfile.GetContentFile(local_file)

    ## Download the content string.
    def getContentString(self):
        self._gfile.GetContentString()

    ## Upload the local file to the Google Drive file.
    #
    #  @param  local_file   target local file path.
    def setContentFile(self, local_file):
        self._gfile.SetContentFile(local_file)

    ## Upload the content string to the Google Drive file.
    #
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
        self._updateAttr()

    ## Return the string representation of the Google Drive file.
    def __str__(self):
        ret_str = ""

        if self.isDir():
            ret_str += "<Dir>  "
        else:
            ret_str += "<File> "
        ret_str += self.file_path
        return ret_str

    ## Update the inner attributes.
    def _updateAttr(self):
        self.title = self._gfile['title']
        if self._gfile.has_key('id'):
            self.id = self._gfile['id']
        if self._gfile.has_key('mimeType'):
            self.mime_type = self._gfile['mimeType']
        if self._gfile.has_key('createdDate'):
            self.created_date = self._gfile['createdDate']
        if self._gfile.has_key('modifiedDate'):
            self.modified_date = self._gfile['modifiedDate']
        if self._gfile.has_key('quotaBytesUsed'):
            self.file_size = self._gfile['quotaBytesUsed']


## Simple extension of pydrive.files.GoogleDriveFileList.
class GoogleDriveFileList:

    ## Create GoogleDriveFileList instance.
    #
    #  @param gfile_list  python list of GoogleDriveFile.
    def __init__(self, gfile_list):
        self._gfile_list = gfile_list

    ## Return the iterator for Google Drive file list.
    def __iter__(self):
        return iter(self._gfile_list)

    ## Return the number of directories and files.
    def __len__(self):
        return len(self._gfile_list)

    ## Return the number of directories.
    def numDirs(self):
        return len(self.dirs())

    ## Return the number of files.
    def numFiles(self):
        return len(self.files())

    ## Return the directory list.
    #
    #  @retval gdirs  GoogleDriveFileList instance.
    def dirs(self):
        gdirs = [gfile for gfile in self._gfile_list if gfile.isDir()]
        return GoogleDriveFileList(gdirs)

    ## Return the file list.
    #
    #  @retval gfiles  GoogleDriveFileList instance.
    def files(self):
        gfiles = [gfile for gfile in self._gfile_list if gfile.isFile()]
        return GoogleDriveFileList(gfiles)

    ## Return the string representation of the Google Drive file list.
    def __str__(self):
        ret_str = "%d directories, %d files.\n" %(self.numDirs(), self.numFiles())

        for gfile in self._gfile_list:
            ret_str += "  " + str(gfile) + "\n"
        return ret_str
