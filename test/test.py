#!/usr/bin/env python

import unittest

class FirstTest(unittest.TestCase):
  def setUp(self):
    pass
  def test_do_something(self):
    self.assertTrue(True)

if __name__ == "__main__":
  unittest.main()

