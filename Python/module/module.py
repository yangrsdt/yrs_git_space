#!/usr/bin/python
# coding = utf8

"a test module"

__author__ = "yrs"

import sys

def test():
	args = sys.argv
	print(args)

def test1():
	print("I dont care")

if __name__ == "__main__":
	test()