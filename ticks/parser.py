#!/usr/bin/env python

import struct
from collections import namedtuple
from datetime import datetime, timedelta

try:
    import lzma
except ImportError:
    from backports import lzma

def chunks(list, n):
  if n < 1:
      n = 1
  return [list[i:i + n] for i in range(0, len(list), n)]

def main():
  f = open("2012/11/03/01h_ticks.bi5", "r")
  data = lzma.decompress(f.read())

  Tick = namedtuple('Tick', 'time ask bid askv bidv')
  epoch = datetime(2012, 11, 3, 1)

  def row_data(row):
    row_data = Tick._asdict(Tick._make(struct.unpack(">LLLff", row)))
    row_data['time'] = (epoch + timedelta(0,0,0,row_data['time']))
    return row_data

  mapped_data = map(lambda row : row_data(row), chunks(data, 20))

  print mapped_data[-1]





if __name__ == '__main__':
  main()
