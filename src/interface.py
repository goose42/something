#!/usr/bin/env python

class interface:
  def __init__(self):
    self.buy=self.get_lower()
    self.sell=self.get_upper()
  def get_lower(self):
    f=open('lower_value.txt','r')
    val=f.read()
    f.close()
    return int(val)
  def get_upper(self):
    f=open('upper_value.txt','r')
    val=f.read()
    f.close()
    return int(val)
  def what_to_do(self, value):
    if value >= self.sell:
      print("SELL!")
      return
    if value <= self.buy:
      print("BUY!!")
      return
    print("Dont do anything right now")


if __name__== "__main__":
  trader=interface()
  price=raw_input("whats the current price?")
  trader.what_to_do(int(price))



