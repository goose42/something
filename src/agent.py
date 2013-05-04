#!/usr/bin/env python

class Agent(object):
  def __init__(self):
    pass

  def sell(self, value, upper_bound):
    print "SELL: %.2f at bound %.2f" % (value, upper_bound)

  def buy(self, value, lower_bound):
    print "BUY: %.2f at bound %.2f" % (value, lower_bound)

  def hold(self, value, lower_bound, upper_bound):
    print "HOLD: %.2f at bounds (%.2f, %.2f)" % (value, lower_bound, upper_bound)


