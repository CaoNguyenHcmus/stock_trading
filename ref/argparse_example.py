#!/usr/bin/python

import argparse
is_watchlist = False
parser = argparse.ArgumentParser(description="Stock trading script")

# action
parser.add_argument("-w", "--watchlist", help='display watch list', action="store_true")

args = parser.parse_args()

if args.watchlist:
	print "watchlist = %s" % args.watchlist
	is_watchlist = True
else:
	parser.print_help()