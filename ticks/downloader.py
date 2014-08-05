from datetime import *
import requests

import ticks.util as util
from ticks.celery import app

import os
import code
import redis

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

      out_path = "tick_data/" + tick_path
      if not os.path.exists(out_path):
        print tick_path
        if not os.path.exists(os.path.dirname(out_path)):
          os.makedirs(os.path.dirname(out_path))
        download_tick.delay(tick_path)


@app.task(ignore_result=True, acks_late=True, timeout=30, soft_timeout=10)
def download_tick(tick_path):
  out_path = "tick_data/" + tick_path
  tick_url = "http://www.dukascopy.com/datafeed/" + tick_path
  tick_request = requests.get(tick_url)
  data_file = open(out_path, "wb+")
  data_file.write(tick_request.content)
  data_file.close()
