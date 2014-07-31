from datetime import *
import requests

import ticks.util as util

import os

import code

class Downloader(object):
  FEEDS = [
    'AUDUSD',
    'EURUSD',
    'GBPUSD',
    'NZDUSD',
    'USDCAD',
    'USDCHF',
    'USDJPY',
    'USDNOK',
    'USDSEK',
    'USDSGD',
    'XAGUSD',
    'XAUUSD'
  ]
  base_url = "http://www.dukascopy.com/datafeed/"
  tick_name  = "{symbol}/{year}/{month}/{day}/{hour}h_ticks.bi5"

  def __init__(self):
    super(Downloader, self).__init__()

  def download_all(self, start_date, end_date):
    map(lambda feed: self.download(feed, start_date, end_date), self.FEEDS)

  def download(self, symbol, start_date, end_date):
    print "Downloading {0}, {1} - {2}".format(symbol, start_date, end_date)

    for time in util.hour_range(start_date, end_date):
      tick_path = self.tick_name.format(
        symbol = symbol,
        year = str(time.year).rjust(4, '0'),
        month = str(time.month).rjust(2, '0'),
        day = str(time.day).rjust(2, '0'),
        hour = str(time.hour).rjust(2, '0')
      )

      print tick_path

      out_path = "tick_data/" + tick_path
      if not os.path.exists(out_path):
        tick_request = requests.get(self.base_url + tick_path)
        # code.interact(local=locals())
        if not os.path.exists(os.path.dirname(out_path)):
          os.makedirs(os.path.dirname(out_path))

        data_file = open(out_path, "wb+")
        data_file.write(tick_request.content)
        data_file.close()
