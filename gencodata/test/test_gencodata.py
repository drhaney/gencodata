#!/usr/bin/env python

import sys

from gencodata import *

def main():

    codata._test_codata()

    formats._test_formats()

    outputs._test_outputs()

    cliargs._test_cliargs()



if __name__ == '__main__':
    main()
    sys.exit()
