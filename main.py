# python libraries
import json
import requests
import os

# program modules
import api_calls
import filesystem
import download

if __name__ == '__main__':
    # create filesystem
    filesystem.create()

    # download images and metadata
    download.download_all()
