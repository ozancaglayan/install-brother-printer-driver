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
import glob
import shutil

from distutils.core import setup
from distutils.command.build import build
from distutils.command.install import install

PROJECT = "install-brother-printer"

class BuildPo(build):
    def run(self):
        build.run(self)
        self.build_po()

    def build_po(self):
        # Generate POT file
        os.system("xgettext -L Python --keyword=_ --output=po/%s.pot %s" % (PROJECT, PROJECT))

        # Update PO files
        for item in glob.glob1("po", "*.po"):
            print "Updating %s..." % item
            os.system("msgmerge --update --backup=off --no-wrap --sort-by-file po/%s po/%s.pot" % (item, PROJECT))

class Install(install):
    def run(self):
        install.run(self)
        self.install_l10n()

    def install_l10n(self):
        for po_file in glob.glob1("po", "*.po"):
            lang = po_file[:-3]
            print "Installing '%s' translations..." % lang
            os.system("msgfmt po/%s.po -o po/%s.mo" % (lang, lang))

            if not self.root:
                self.root = "/"

            dest = os.path.join(self.root, "usr/share/locale/%s/LC_MESSAGES" % lang)
            if not os.path.exists(dest):
                os.makedirs(dest)

            shutil.copy("po/%s.mo" % lang, os.path.join(dest, "%s.mo" % PROJECT))
            os.unlink("po/%s.mo" % lang)

setup(name=PROJECT,
      version="0.1",
      description="Simple tool to install Brother printer drivers",
      long_description="A GUI tool for installing Brother printer drivers over the Internet",
      author="Ozan Çağlayan",
      author_email="ozan@pardus.org.tr",
      url="http://github.com/ozancaglayan/install-brother-printer-driver",
      license="GPLv2",
      platforms=["Linux"],
      scripts=["install-brother-printer"],
      cmdclass = {'build_po'    : BuildPo,
                  'install'     : Install,
                 },
      data_files=[("/usr/share/brother-driver-installer", ["LICENSE.driver"]),],
      )
