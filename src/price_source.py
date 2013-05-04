#!/usr/bin/env python

import random
import math
from collections import Iterator
import time

def delay():
  time.sleep(0.1)

class RandomPriceSource(Iterator):
  '''
    Log normal distribution price source with (open, high, low, close)
  '''
  def __init__(self, o, h, l, c):
    self.open, self.close = o, c
    self.high, self.low = h, l
    self.current = self.open
    self.sigma = math.fabs(0.01 * (self.open - self.close))

  def next(self):
    change = random.lognormvariate(0, self.sigma)
    if self.current + change > 0 and random.choice((True, False)):
      change = -change
    self.current += change
    delay()
    yield self.current

  def __iter__(self):
    return self

