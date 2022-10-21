#!/usr/local/bin/python3

# Takes the filename from stdin
# FastFoto sets the "datetime_digitized" prop of the file already,
# so we can use that to set the original date

import sys
from pathlib import Path    
from exif import Image

def main():
    for line in sys.stdin:
        filePath = line.rstrip()
        imageFile = Path(filePath)
        if not imageFile.is_file():
            print(f"Not a file: {line}")
            sys.exit(1)

        fileName = imageFile.name
        burnExifDate(filePath)

# Bail if image already has date
# Todo: Add a "--force" flag to this script
def burnExifDate(filePath):
    img = Image(filePath)
    if img.get("datetime_original"):
        print("Image already contains date. Bailing.")
        sys.exit(1)
    digitizedDate = img.get("datetime_digitized")
    img.datetime_original = digitizedDate
    with open(filePath, 'wb') as new_image_file:
        new_image_file.write(img.get_file())

if __name__ == '__main__':
    main()