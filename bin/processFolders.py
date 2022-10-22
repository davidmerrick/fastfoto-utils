#!/usr/local/bin/python3

# Walks the FastFoto directory (default: ~/Pictures/FastFoto)
# Steps into subdirs and moves enhanced photos into an "enhanced" directory
# and original photos into an "original" directory

import sys
from pathlib import Path

fastfotoDir = f"{Path.home()}/Pictures/FastFoto"

def main():
    for subPath in Path(fastfotoDir).iterdir():
        if subPath.is_dir():
            processDir(subPath)

def processDir(dir):
    print(f"Processing dir {dir}")

    originalPath = dir.joinpath("original")
    enhancedPath = dir.joinpath("enhanced")

    Path(originalPath).mkdir(parents=True, exist_ok=True)
    Path(enhancedPath).mkdir(parents=True, exist_ok=True)

    # Handle enhanced images
    for image in dir.glob("*_a.jpg"):
        image.rename(enhancedPath / image.name)
    # Handle original images
    for image in dir.glob("*.jpg"):
            image.rename(originalPath / image.name)

if __name__ == '__main__':
    main()