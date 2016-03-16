
Simple PyDrive Extension. (Python)
====

PyDriveEx package adds simple utility functions to [PyDrive](http://pythonhosted.org/PyDrive/)
for easy handling of the Google Drive API.
You can handle Google Drive directories and files like built-in os module.

Main extensions:

* File path access for Google Drive directories and files.
* Easy create / upload function for Google Drive directories and files.
* Delete function for Google Drive directories and files.
* Google Drive file visitor like os.walk.

## Installation

*Note*: This program was only tested on **Windows** with **Python2.7**.
**Linux** and **Mac OS** are not officially supported,
but the following instructions might be helpful for installing on those environments.

### Dependencies
Please install the following required python modules.

* [**google-api-python-client**](https://code.google.com/archive/p/google-api-python-client/)
* [**PyDrive**](http://pythonhosted.org/PyDrive/)

You can easily install these packages with the following commands.

``` bash
  > pip install --upgrade google-api-python-client
  > pip install PyDrive
```

### Install main modules

You can use **pip** command for installing main modules.
Please run the following command from the shell.

``` bash
  > pip install git+https://github.com/tody411/PyDriveEx.git
```

## Quick Start

PyDriveEx can make the GoogleDrive instance in just one line with the default PyDrive authentication setting.

``` python
from pydrive_ex.drive import GoogleDrive

gdrive = GoogleDrive()          # Create Google Drive instance with default setting.
gfile_list = gdrive.listdir()   # Get the file list of the root directory.
print gfile_list                # Print the file list.
```

The output will be:

``` bash
1 directories, 2 files.
  <Dir>  Dir1
  <Dir>  Dir2
  <File> Text.txt
  <File> image.png
```

To make this code work, you need to prepare the your Google Drive setting to run PyDrive.

1. Go to APIs Console and make your own project.
2. On **Services** menu, turn Drive API on.
3. On **API Access** menu, create OAuth2.0 client ID.
  * Select *Application type* to be Web application.
4. Download **client_secrets.json** and put it in your working directory.

I highly recommend you to create **settings.yaml** to save credentials file.

``` yaml
client_config_backend: file
client_config_file: client_secrets.json

save_credentials: True
save_credentials_backend: file
save_credentials_file: credentials.json
```

If the file is put in the same working directory,
the authentication process will be skipped from the second time.

You can run PyDriveEx examples in ```pydrive_ex/examples```
by putting your own **client_secrets.json** in the directory
(**settings.yaml** is included in ```pydrive_ex/examples```).


## File Management

### Upload a new file

[```pydrive_ex/examples/upload_file.py```](pydrive_ex/examples/upload_file.py)

You can easily upload a new file via GoogleDriveFile instance or
GoogleDrive.uploadFile function.

``` python
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

```

GoogleDrive.uploadFile combines the creation and uploading.
If the given file path already exists, this method will just update the file.
Most of the case, GoogleDrive.uploadFile is simpler than

You can specify the directory structure via "/" like a usual local file path.

### Download a file

[```pydrive_ex/examples/download_file.py```](pydrive_ex/examples/download_file.py)

This simple three lines will download the Google Drive file to the local.

``` python
from pydrive_ex.drive import GoogleDrive

gdrive = GoogleDrive()          # Create Google Drive instance with default setting.

# Download the Google Drive file to the local.
gdrive.downloadFile("PDTest/Image/HelloImage.png", "images/TestDownloadedImage.png")

```

### Delete a file

[```pydrive_ex/examples/delete_file.py```](pydrive_ex/examples/delete_file.py)

Since the original PyDrive does not support a delete function,
I extend the delete functionality in PyDriveEx.

``` python
from pydrive_ex.drive import GoogleDrive

gdrive = GoogleDrive()          # Create Google Drive instance with default setting.

gdrive.deleteFile("PDTest/Hello.txt")  # Delete a single Google Drive File.
print gdrive.listdir("PDTest")          # Print the file list.

gdrive.deleteFile("PDTest/Image")    # Delete whole Google Drive folder.
print gdrive.listdir("PDTest")          # Print the file list.

```

The output will be:

``` bash
2 directories, 0 files.
  <Dir>  PDTest/Image
  <Dir>  PDTest/TestDir

1 directories, 0 files.
  <Dir>  PDTest/TestDir

```

If the target file does not exist, "File is not found" will be printed.
If the Google Drive access fails, FileDeleteError will be raised.

## Google Drive Traversal

### Find a file via file path

[```pydrive_ex/examples/find_file.py```](pydrive_ex/examples/find_file.py)

You can access a Google Drive file via a file path in a way similar to the local file system.

``` python
from pydrive_ex.drive import GoogleDrive

gdrive = GoogleDrive()          # Create Google Drive instance with default setting.
gfile = gdrive.file("PDTest/Image/HelloImage.png")  # Find a file with the given file path.

# Print Google Drive file attributes.
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


```

GoogleDriveFile provides attributes and functions to access Google Drive file properties.

The output will be:

``` bash
<File> PDTest/Image/HelloImage.png
 title        :  HelloImage.png
 file_path    :  PDTest/Image/HelloImage.png
 file_size    :  19251
 isDir        :  False
 isFile       :  True
 id           :  0B73BaE77JCgfZU1Jc2RDMVpuMEC
 mime_type    :  image/png
 created_date :  2016-03-15T05:58:07.607Z
 modified_date:  2016-03-15T05:58:09.870Z
```

### Walk a Google Drive directory

[```pydrive_ex/examples/walk_drive.py```](pydrive_ex/examples/walk_drive.py)

GoogleDrive.walk provides a directory visitor similar to os.walk.

``` python
from pydrive_ex.drive import GoogleDrive

gdrive = GoogleDrive()          # Create Google Drive instance with default setting.

# Create test directories.
gdrive.deleteFile("WalkTest")
gdrive.createDir("WalkTest/Dir1")
gdrive.createDir("WalkTest/Dir2")
gdrive.createFile("WalkTest/Dir1/TestFile1.txt")
gdrive.createFile("WalkTest/TestFile2.txt")

# Walk Google Drive for the given directory path.
for root, gdirs, gfiles in gdrive.walk("WalkTest"):
    print root
    for gdir in gdirs:
        print gdir
    for gfile in gfiles:
        print gfile
    print ""


```

The output will be:

``` bash
WalkTest
<Dir>  WalkTest/Dir2
<Dir>  WalkTest/Dir1
<File> WalkTest/TestFile2.txt

WalkTest/Dir2

WalkTest/Dir1
<File> WalkTest/Dir1/TestFile1.txt
```

## License

The MIT License 2016 (c) tody