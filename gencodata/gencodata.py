#!/usr/bin/env python
"""
 python-codata.py -

    prints selected CODATA constants as Fortran 77 syntax
    for use in a header file.

 creation: 11/11/2017

 author: drh
"""
VersionString = '0.1.dev.1'

# ISO Python modules


import sys

import cliargs
import outputs

#______________________________________________________

def main(argv=None):
    """pyLint"""

    parsed = cliargs.argvParse()

    outputs.handleArgs(parsed)

    sys.exit(0)


if __name__ == "__main__":
    """pyLint"""
    main()

