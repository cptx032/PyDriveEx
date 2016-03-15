# -*- coding: utf-8 -*-
## @package setup
#
#  setup utility package.
#  @author      tody
#  @date        2016/03/15

from setuptools import setup, find_packages
from pydrive_ex import __author__, __version__, __license__

setup(
        name = 'pydrive_ex',
        version = __version__,
        description = 'Simple PyDrive Extension.',
        license = __license__,
        author = __author__,
        url = 'https://github.com/tody411/PyDriveEx.git',
        packages = find_packages(),
        )