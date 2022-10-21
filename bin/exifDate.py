#!/usr/local/bin/python3

# Takes the filename from stdin
# Burns the EXIF date based on the filename
# Example: 
# 2020_Summer.jpeg

import sys
from pathlib import Path    
from exif import Image
import re

def main():
    for line in sys.stdin:
        imageFile = Path(line.rstrip())
        if not imageFile.is_file():
            print(f"Not a file: {line}")
            sys.exit(1)

        fileName = imageFile.name
        year = parseYear(fileName)
        print(year)


def parseYear(fileName):
    return re.search(r"^\d\d\d\d", fileName).group()

def parseMonth(fileName):
    return re.search("^\d\d\d\d", fileName).group()

if __name__ == '__main__':
    main()