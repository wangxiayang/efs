#!/usr/bin/python

try:
	print 'first line'
	2 / 0
	print 'second line'
except Exception, e:
	print e