Some Python utils for handling FastFoto scans.

# Installation

```shell
pip3 install -r requirements.txt
```

# Usage

Use these just like a standard UNIX shell script

```shell
# Burn the "datetime_original" exif tag into the image
ls -d ~/Pictures/FastFoto/1999*/*.jpg | ./bin/exifDate.py

# Process FastFoto directory
./bin/processFolders.py
```