Some Python utils for handling FastFoto scans.

# Installation

```shell
pip3 install -r requirements.txt
```

# Usage

Use these just like a standard UNIX shell script

```shell
# Burn EXIF date onto enhanced photos

# Copy enhanced photos to temp
mkdir /tmp/enhanced
cp ~/Pictures/FastFoto/2018*/*_a.jpg /tmp/enhanced

ls -d /tmp/enhanced/* | ./bin/exifDate.py
```