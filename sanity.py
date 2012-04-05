#!/usr/bin/env python
# encoding: utf-8
from optparse import OptionParser
import sys
import os
import re
from clint.textui import colored
from clint.textui import puts

testfile_pattern = 'test_(.+)\.[json|yaml]'


def run_tests(folder):
    """
    searches for testfiles in a folder recursively
    """

    for root, subfolder, files in os.walk(folder):
        for file_ in files:
            match_ = re.match(testfile_pattern, file_)
            if match_:
                testfile = os.path.abspath(file_)
                puts(colored.red(testfile))
                puts(colored.green(testfile))
                #json testfiles
                if testfile.endswith('json'):
                    pass
                #yaml testfiles
                else:
                    pass


def main():

    usage = 'usage: %prog [options] user -h for help'
    parser = OptionParser(usage)
    parser.add_option('-f', '--testfolder', action='store',
    type='string', dest='testfolder', help='folder containg the tests')
    #parser.add_option('-t', '--type', action='store',
    #type='string', dest='testfolder', help='folder containg the tests')

    (options, args) = parser.parse_args()
    if options.testfolder:
        run_tests(options.testfolder)
    else:
        parser.print_help()

if __name__ == '__main__':
    status = main()
    sys.exit(status)
