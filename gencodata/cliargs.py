#!/usr/bin/env python
"""
 python-codata.py -

    prints selected CODATA constants as Fortran 77 syntax
    for use in a header file.

 creation: 11/11/2017

 author: drh
"""

# ISO Python modules


import sys
import argparse
#import cliargs
import codata
#import outputs

parser = None
#______________________________________________________

def argvParse (args=None):
    '''
    If called with an argument, it requires a string LIST, viz.,

        argvParse(['randomArg'])

    Dick with argparse to minimally
    handle these command line arguments:

    <no args>   - print usage message and list of constant categories

    <category>  - print all constants within one or more categories

    -l,--list   - list constants, either all or within a category
    -s,--syntax - generate results in C, Fortran, or Python syntax.

    -i,--input  - print constants from list in file
    -o,--output - write results to an output file

    -c,--csv    - write results to a CSV file
    -j,--json   - write results to a JSON file

    TO DO:  -m,--module  - write constants as importable python module
    '''
    global parser
    if parser is None:

        parser =  argparse.ArgumentParser()

        catstr = 'Print constant declarations from one or more categories. \
                    \nCategories are: all, '

        catstr += ', '.join([cat for cat in codata.Categories()])

        parser.add_argument('category',nargs='*',
                            help=catstr,
                            default=[]) #default=argparse.SUPPRESS)

        parser.add_argument('-l','--list',action='store_true',
                            help='list constant names within a category. \
                            Overrides file output.',
                            default=False)  # default=None)

        parser.add_argument('-i','--input',
                            nargs=1,
                            help='select constants from list in file',
                            type=str,
                            default='')    # default=argparse.SUPPRESS)

        parser.add_argument('-o','--output',
                            nargs=1,
                            help='write results to an output file',
                            type=str,
                            default='')    # default=argparse.SUPPRESS)

        parser.add_argument('-c','--csv',
                            nargs=1,
                            help='write results to a CSV file',
                            type=str,
                            default='')    # default=argparse.SUPPRESS)

        parser.add_argument('-j','--json',
                            nargs=1,
                            help='write results to a JSON file',
                            type=str,
                            default='')    # default=argparse.SUPPRESS)

        parser.add_argument('-s','--syntax',
                            nargs=1,
                            help='Use C,C99, F,Fortran,F77, Fortran90,F90, or Python (default) output, case-insensitive',
                            type=str,
                            default=['python'])    # default=argparse.SUPPRESS)

        #print('*** initial parser state')
        #print(parser)

    #print("args type is %s" % type(args))

    if args == None:
        args = sys.argv[1:]

    if len(args) == 0:
        print('%s generates CODATA physical constants\nheader files in C, Fortan, or Python(default) syntax.\n' %
            (sys.argv[0]))
        parser.print_usage()
        return None

    try:
        #print('args is %s' % args)
        results = parser.parse_args(args)
        #print('**** parse results')
        #print(results)
    except:
        results = None
        #print('argparse shit the bed again.')

    '''
    argparse result is of type <class 'argparse.Namespace'>
    For command line = "gencodata atomic --syntax fortran"
    it looks like:

    dir(results) = Namespace(category=['atomic'], csv='',
        input='', json='', list=False, output='', syntax=['fortran'])
    '''
    return results

#______________________________________________________


def _test_cliargs ():

    cli_errors = 0

    def test_list ():
        global cli_errors
        parsed = argvParse(['-l'])
        if parsed.list == False:
            print('!-l list arg failed')
            cli_errors += 1

        parsed = argvParse(['--list'])
        if parsed.list == False:
            print('!--list list arg failed')
            cli_errors += 1

    def test_input ():
        global cli_errors
        parsed = argvParse(['-i','dummy'])
        if parsed.input[0] != 'dummy':
            print('!-i input arg failed')
            cli_errors += 1

        parsed = argvParse(['--input','dummy'])
        if parsed.input[0] != 'dummy':
            print('!--input input arg failed')
            cli_errors += 1

    def test_output ():
        global cli_errors
        parsed = argvParse(['-o','dummy'])
        if parsed.output[0] != 'dummy':
            print('!-o output arg failed')
            cli_errors += 1

        parsed = argvParse(['--output','dummy'])
        if parsed.output[0] != 'dummy':
            print('!--output output arg failed')
            cli_errors += 1

    def test_csv ():
        global cli_errors
        parsed = argvParse(['-c','dummy'])
        if parsed.csv[0] != 'dummy':
            print('!-c csv arg failed')
            cli_errors += 1

        parsed = argvParse(['--csv','dummy'])
        if parsed.csv[0] != 'dummy':
            print('!--csv csv arg failed')
            cli_errors += 1

    def test_json ():
        global cli_errors
        parsed = argvParse(['-j','dummy'])
        if parsed.json[0] != 'dummy':
            print('!-j json arg failed')
            cli_errors += 1

        parsed = argvParse(['--json','dummy'])
        if parsed.json[0] != 'dummy':
            print('!--json json arg failed')
            cli_errors += 1

    def test_syntax ():
        global cli_errors
        parsed = argvParse(['-s','dummy'])
        if parsed.syntax[0] != 'dummy':
            print('!-s syntax arg failed')
            cli_errors += 1

        parsed = argvParse(['--syntax','dummy'])
        if parsed.syntax[0] != 'dummy':
            print('!--syntax syntax arg failed')
            cli_errors += 1

    print('\n#### BEGIN %s test\n' % __file__.upper())

    test_list ()
    test_input ()
    test_output ()
    test_csv ()
    test_json ()
    test_syntax ()
    print("\t%d parse errors" % cli_errors)

    print('\n#### END %s test\n' % __file__.upper())

if __name__ == '__main__':

    _test_cliargs()

    sys.exit()
