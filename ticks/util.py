__author__ = "Eric Nelson"

from datetime import timedelta

def hour_range(start_date, end_date):
  delta_t = end_date - start_date

  delta_hours = (delta_t.days *  24.0) + (delta_t.seconds / 3600.0)
  for n in range(int (delta_hours)):
      yield start_date + timedelta(0, 0, 0, 0, 0, n) # Hours
