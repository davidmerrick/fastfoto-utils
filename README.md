Some Python utils for handling FastFoto scans.

# Installation

```shell
pip3 install -r requirements.txt
```

# Usage

Use these just like a standard UNIX shell script

```shell
# Burn EXIF date onto enhanced photos

ls ~/Pictures/FastFoto/2018_March/*_a.jpg | ./bin/exifDate.py

# Move enhanced photos to temp
mkdir /tmp/enhanced
mv ~/Pictures/FastFoto/2018_March/*_a.jpg /tmp/enhanced
```