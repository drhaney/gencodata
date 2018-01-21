"""
 outputs.py -

    provides all output functionality for gencodata

 creation: 11/21/2017

 author: drh
"""

# ISO Python modules

import os
import sys

# CODATA database module

import codata

# language output class module for C, Fortran, and Python

import formats
global Fmt              # used by genericWrite()

# _______________________________________________________

def SetFormat(syntaxObj=''):
    ''' Select output format from argparse object '''

    global Fmt

    ''' argparse flags have a list wrapper '''
    if type(syntaxObj).__name__ == 'list':
        syntax = syntaxObj[0].lower()

    elif type(syntaxObj).__name__ == 'str':
        syntax = syntaxObj.lower()

    else:
        syntax = 'python'           # default


    if syntax == 'c' or syntax == 'cansi' or syntax == 'k&r' or syntax == 'k&rc':
        Fmt = formats.FormatCansi()

    elif syntax == 'c99':
        Fmt = formats.FormatC99()

    #elif syntax == 'f' or syntax == 'f77' or syntax == 'fortran':
    elif syntax in ['f','f77','fortran','fortran77']:
        Fmt = formats.FormatFortran77()

    elif syntax == 'f90' or syntax == 'fortran90':
        Fmt = formats.FormatFortran90()

    elif syntax in ['python','python2','python3']:
        Fmt = formats.FormatPython()

    else:
        Fmt = formats.FormatPython()

# _______________________________________________________

def fileExists (fname):
    """Test file existence"""
    if os.path.exists(fname):
        return True
    else:
        print("Error: " + fname + " not found")
        return False
#______________________________________________________

def doCategories (category_args=[]):
    ''' construct dictionary of requested constants by category '''

    const_dict = {}

    if 'all' in category_args:
        const_dict = codata.Dictionary()

    else:
        catlist = sorted(codata.Categories())

        for category in category_args:

            if category in catlist:
                tempdict = codata.Constants(category)
                const_dict.update(tempdict)

            else:
                print('\'%s\' category not found' % category)

    return const_dict

#______________________________________________________

def readFileList (fname=''):
    '''
    Read list of constants from a text file.
    Constant names are one per line.
        blank lines ignored
        # commented lines ignored
    '''

    if fileExists(fname) is False:
        return {}

    constants_dict = {}

    with open(fname,'r') as ifp:
        for line in ifp:
            name = line.strip()

            if name != '' and name[0] != '#':
                name = codata._strip_name(name)
                if name in codata.Names():

                    constants_dict[name] = codata.Properties(name)

                else:
                    print('\'%s\' constant not found' % name)

    ifp.close()

    return constants_dict

#______________________________________________________
def dumpList (cdict={}):
    '''
    Print list of constants in category to console.

    if no categories were specified,
    do nothing.
    '''

    if len(cdict)<1:
        print('No constants in list')

    else:
        namelist = sorted(cdict.keys())
        for name in namelist:
            print(cdict[name]['Quantity '])

    return

#______________________________________________________

def genericWrite(outfp,constants_dict={}):

    global Fmt

    #print('genericWrite: syntax = %s' % Fmt.language())

    # file header with date and provenance info
    citation = Fmt.FileHead()
    outfp.write(citation + '\n')

    # sort by name for easier visual search
    constants_list = sorted(constants_dict.keys())

    for key in constants_list:
        property = constants_dict[key]

        # use uncooked CODATA constant name instead of stripped lowercase key
        name = property['Quantity ']

        decl = Fmt.BuildDefinition(name,property)
        outfp.write(decl + '\n')

    # file tail with file name, time info
    outfp.write(Fmt.FileTail(outfp.name))

    outfp.flush()

    if outfp is not sys.stdout:
        outfp.close()

    return


#______________________________________________________

def writeConsole (constants_dict={}):

    genericWrite(sys.stdout,constants_dict)
    return

#______________________________________________________

def writeFile (constants_dict={}, outFileName=''):

    if (outFileName == ''):
        print("WRITE ERROR: no file name")
        return

    try:
        ofp = open(outFileName,'wa')
        genericWrite(ofp,constants_dict)
    except:
        print("ERROR: can\'t open file %s" % outFileName)

    return

#______________________________________________________

def handleArgs (parsed):

    ''' Assign actions to parsed arguments.
    parsed is of type <class 'argparse.Namespace'>.
    Looks like:

    Namespace(category=['atomic'], csv='', input='', json='',
                     list=False, output='', syntax=['C99'])

    Note that args retrieved from command line have a list wrapper
    while default values do not.
    '''

    constants_dict = {}
    if parsed == None:
        return

    '''build constants dict from category list'''

    if len(parsed.category)>0:
        category_list = parsed.category
        constants_dict = doCategories(category_list)

    '''
    read constant names from file
    and build dictionary of them.
    '''
    if parsed.input != '':
        infile = parsed.input[0]
        tempdict = readFileList(infile)
        constants_dict.update(tempdict)

    '''dump the constant names to console and QUIT'''
    if parsed.list is True:
        dumpList(constants_dict)
        return

    # bail if nothing to do
    if len(constants_dict)<1:
        return

    ''' Select language syntax/format for output '''
    SetFormat(parsed.syntax)


    # If NO output files,  write to console
    if (parsed.output == '' and \
        parsed.csv == '' and \
        parsed.json == ''):

        writeConsole(constants_dict)

    # write to output file(s)
    # Header, CSV, and JSON file outputs are not mutually exclusive
    else:
        # generate a Simplified Header Interface File
        if parsed.output != '':
            outFileName = parsed.output[0]
            writeFile(constants_dict,outFileName)

        # generate a CSV database file
        if parsed.csv != '':
            csvFileName = parsed.csv[0]
            codata.WriteCSV(constants_dict,csvFileName)

        # generate a JSON data export file
        if parsed.json != '':
            jsonFileName = parsed.json[0]
            codata.WriteJSON(constants_dict,jsonFileName)

#______________________________________________________

def _test_outputs ():
    _test_dict = \
        {
          "molar gas constant": {
            "Category": "physicochemical",
            "Symbol": "Rgas",
            "Uncertainty": "0.0000048",
            "Quantity ": "molar gas constant",
            "Value": "8.3144598",
            "Unit": "J mol^{-1} K^{-1}"
          },
          "planck constant": {
            "Category": "universal",
            "Symbol": "h",
            "Uncertainty": "0.000000081e-34",
            "Quantity ": "Planck constant",
            "Value": "6.626070040e-34",
            "Unit": "J s"
          },
          "speed of light in vacuum": {
            "Category": "universal",
            "Symbol": "c",
            "Uncertainty": "0.0",
            "Quantity ": "speed of light in vacuum",
            "Value": "299792458",
            "Unit": "m s^{-1}"
          },
          "hartree energy": {
            "Category": "atomic",
            "Symbol": "E_h",
            "Uncertainty": "0.000000054e-18",
            "Quantity ": "Hartree energy",
            "Value": "4.359744650e-18",
            "Unit": "J"
          },
          "avogadro constant": {
            "Category": "physicochemical",
            "Symbol": "N_A",
            "Uncertainty": "0.000000074e23",
            "Quantity ": "Avogadro constant",
            "Value": "6.022140857e23",
            "Unit": "mol^{-1}"
          },
          "boltzmann constant": {
            "Category": "physicochemical",
            "Symbol": "k_B",
            "Uncertainty": "0.00000079e-23",
            "Quantity ": "Boltzmann constant",
            "Value": "1.38064852e-23",
            "Unit": "J K^{-1}"
          }
        }


    print('\n#### BEGIN %s test\n' % __file__.upper())

    print('\n ----- syntax arg test -----\n')
    ArgList =   ['C','C99','K&R','K&RC',
                'F','F77','Fortran','Fortran77',
                'Fortran90','F90',
                'Python','Python2','Python3']

    for i in range(0,len(ArgList)):
        SetFormat(ArgList[i])
        print("arg=[%s]\t\tformat language=[%s]" %
            (ArgList[i], Fmt.language()))
    print('')

    # default to Python syntax output
    SetFormat('')

    print('\n ----- category(alpha) test -----\n')

    # build small dictionary of a category
    alphadict = doCategories(['alpha'])

    # print constant names to console
    print('Alpha category constant names:')
    dumpList(alphadict)

    print('\n----- Alpha category constant definitions -----\n')
    writeConsole(alphadict)

    print('\n ----- synthetic dictionary test -----\n')

    # build a small test dictionary from data structure above
    testkeys = _test_dict.keys()
    tempdict = {}
    for tkey in testkeys:
        if tkey not in codata._phys_const_keys_:
            print("Error: couldn\'t find \'%s\'." % tkey)

        else:
            tempdict[tkey] = codata.Properties(tkey)

    lentempdict  = len(tempdict)
    len_test_dict = len(_test_dict)
    if lentempdict != len_test_dict:
        print('temporary dict truncated at %d records, expected %d' % \
                (lentempdict,len_test_dict))
    else:
        print("test dictionary correctly built:")
        writeConsole(tempdict)

    print('\n#### END %s test\n' % __file__.upper())
    return

#________________________________________

# TO TEST: python outputs.py

if __name__ == "__main__":
    _test_outputs()
    sys.exit()


