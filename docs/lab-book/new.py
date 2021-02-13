#!/usr/bin/python3

import datetime
import glob
import pathlib
import shutil

fileName = datetime.datetime.utcnow().strftime("%y%m%d%H%M%SZ.md")

try:
    newestExistingFileName = sorted(glob.glob("*.md"), reverse=True)[0]
    shutil.copyfile(newestExistingFileName, fileName)
except IndexError:
    pathlib.Path(fileName).touch()

print(fileName)
