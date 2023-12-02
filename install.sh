#!/bin/bash

PLATFORM=linux64
sudo apt install curl
sudo apt install libarchive-tools
VERSION=$(curl http://chromedriver.storage.googleapis.com/LATEST_RELEASE)
curl http://chromedriver.storage.googleapis.com/$VERSION/chromedriver_$PLATFORM.zip | bsdtar -xvf - -C .

# eof