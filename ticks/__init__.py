__author__ = 'Eric Nelson'

import sys
from datetime import *

import downloader as dl

def main():
  downloader = dl.Downloader()
  downloader.download_all(datetime(2010,1,1), datetime.now())
