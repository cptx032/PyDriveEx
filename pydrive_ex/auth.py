# -*- coding: utf-8 -*-
## @package pydrive_ex.auth
#
#  Simple extension of pydrive.auth utility package.
#  @author      tody
#  @date        2016/03/15

import pydrive.auth
import os


## Simple extension of pydrive.auth.GoogleAuth.
#  @param   auth_dir  directory to store client_secrets.json and credentials.json.
#  @retval  gauth     pydrive.auth.GoogleAuth object
def GoogleAuth(auth_dir=None):
    cwd = os.getcwd()
    if auth_dir is not None:
        os.chdir(auth_dir)
    gauth = pydrive.auth.GoogleAuth()
    gauth.LocalWebserverAuth()
    if auth_dir is not None:
        os.chdir(cwd)
    return gauth
