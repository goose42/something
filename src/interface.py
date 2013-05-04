#!/usr/bin/env python

from price_source import RandomPriceSource
from agent import Agent

class Controller:
  '''
    The Controller is the entry point to the system
    and acts as the market.
  '''
  def __init__(self, agent, lower, upper):
    self.agent = agent
    self.lower = lower
    self.upper = upper

  def what_to_do(self, value):
    lower_bound, upper_bound = self.lower(), self.upper()
    if value < lower_bound:
      self.agent.buy(value, lower_bound)
    elif value >= upper_bound:
      self.agent.sell(value, upper_bound)
    else:
      self.agent.hold(value, lower_bound, upper_bound)

def main():
  o, h, l, c = 100, 130, 70, 90
  source = RandomPriceSource(o, h, l, c)

  lower_bound = lambda: o - 10
  upper_bound = lambda: o + 10

  agent = Agent()
  controller = Controller(agent, lower_bound, upper_bound)

  for price in source:
    controller.what_to_do(*price)

if __name__== "__main__":
  main()


