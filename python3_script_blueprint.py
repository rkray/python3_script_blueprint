#!/usr/bin/env python3
#
# author: rene@kray.info
# date: 2017-02-28
# purpose:
# - basic python3 script
#
# Todo
# - signal handling
# - cleanup function
# - logging

from optparse import OptionParser
#from re import match

################################################################################
# Class related things
################################################################################
class BluePrint:
    def __init__(self):
        print("init the class")
        # defiune defaults here
        self.conf=dict(
            filename="none",
            verbose=False
        )

    def run(self):
        print("running")
        print(self.conf)

    ############################################################################
    # geting commandline arguments
    ############################################################################
    def get_arguments(self):
        print("parse command line arguments")
        parser = OptionParser()
        parser.add_option(
            "-f", "--file",
            dest="filename",
            help="write report to FILE", metavar="FILE")
        parser.add_option(
            "-q", "--quiet",
            action="store_false", dest="verbose", default=True,
            help="don't print status messages to stdout")

        (options, args) = parser.parse_args()
        # join defaults with optons from command line
        self.conf.update(vars(options))

# END of BluePrint class

# Run this party only if this file is started as script
if __name__=="__main__":
   print("This is a script")
   bp=BluePrint()
   bp.get_arguments()
   bp.run()
