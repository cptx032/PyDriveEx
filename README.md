
Simple PyDrive Extension. (Python)
====

This package provides a simple extension of [PyDrive](http://pythonhosted.org/PyDrive/) that wraps the Google Drive API tasks as like a common os module.

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
4. Download client_secrets.json and put it in your working directory.

I recommend you to create **settings.yaml** to save credentials file.

``` yaml
client_config_backend: file
client_config_file: client_secrets.json

save_credentials: True
save_credentials_backend: file
save_credentials_file: credentials.json
```

## License

The MIT License 2016 (c) tody