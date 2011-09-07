#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2011 TUBITAK/UEKAE
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation; either version 2 of the License, or (at your
# option) any later version. Please read the COPYING file.

import os
import sys
import glob
import shutil

from distutils.core import setup

# Call distutils.setup

setup(name="brother-driver-installer",
      version="0.1",
      description="Simple tool to install Brother printer drivers",
      long_description="A GUI tool for installing Brother printer drivers over the Internet",
      author="Ozan Çağlayan",
      author_email="ozan@pardus.org.tr",
      url="http://github.com/ozancaglayan/install-brother-printer-driver",
      license="GPLv2",
      platforms=["Linux"],
      scripts=["install-brother-printer"],
      data_files=[("/usr/share/brother-driver-installer", ["LICENSE.driver"]),],
      )
