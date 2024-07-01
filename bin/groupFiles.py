#!/usr/local/bin/python3

# Takes a directory, chunks the files, and moves them to their own directories under /tmp
# Useful for when you need to import, say, 1000 photos at a time into Photos

import sys
from pathlib import Path

sourceDir = f"{Path.home()}/Downloads/2000s"
destDir = f"/tmp/batched"
# Chunk size
n = 1000

def main():
    i = 0
    chunk = 0
    Path(dirName(chunk)).mkdir(parents=True, exist_ok=True)
    # Handle enhanced images
    for sourceFile in Path(sourceDir).glob("*"):
        i = i + 1
        if(i % n == 0):
            print(f"Incrementing chunk")
            chunk = chunk + 1
            Path(dirName(chunk)).mkdir(parents=True, exist_ok=True)
        sourceFile.rename(destDir + "/" + str(chunk) + "/" + sourceFile.name)

def dirName(chunk):
    return destDir + "/" + str(chunk)


if __name__ == '__main__':
    main()
