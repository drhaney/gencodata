import sys
import time
import codata

LINELEN=78

class LanguageFormat:

    def __init__(self,language,comment,indent,block='',endblock=''):
        self._language  = language
        self._comment   = comment
        self._indent    = indent

        '''C/C++, Python, et.al. have block commenting (/**/, """block""")
            Fortran has only line commenting.
        '''
        self._block     = block
        self._endblock  = endblock


    def language(self):
        return self._language

    def _camelCase(self,s=''):
        ''' "Planck constant" --> PlanckConstant '''
        slist = s.replace('.','').replace('-',' ').split(' ')
        camelID = ''
        for word in slist:
            camelID += word.capitalize()

        return camelID

    def Value (self,val):
        #  '123' --> '123.0'
        if ('.' not in val and \
            'e' not in val and \
                'E' not in val):
            val += '.0'
        return val

    def Units (self,_unit=''):
        if _unit == '':
            unitstr = "dimensionless"
        else:
            unitstr = ("in units \'%s\'" % _unit)
        return unitstr

    def Uncertainty (self,_uncert=''):
        if _uncert == '0.0':
            uncerts = "(exact)"
        else:
            uncerts = ("+/-%s" % _uncert)
        return uncerts

    def Symbol (self,sym,name):
        if sym == '':
            return self._camelCase(name)
        else:
            return sym

    def Description (self,name,cat):
        offset = 39 - (len(self._comment) + 1)
        fmtstr = ('%%-%ds(%%s)' % (offset))
        #print('format str: [%s]' % fmtstr)
        s = (fmtstr % (name,cat))
        return s

    def Define (self,sym,val):
        '''---language-specific string---
        Default equate
        '''
        s =  ("%s = %s" % (sym,val))
        return ("%-39s" % s)

    def Wrapline (self, line,start,end,width=78):
        commentlen = len(start) + len(end) + 2
        ''' fmtstr looks like [%s %-66s %s] '''

        fmtstr = ('%%s %%-%ds %%s' % (width-commentlen))
        wrapped = (fmtstr % (start, line, end))
        return wrapped

    def FileHead (self):
        '''
        ---language-specific string---
        return a file header containing
            title, date, and CODATA citation.
        '''

        cites = codata.Citation().split('\n')

        PAD = self._indent

        # if syntax permits block comments, use it.
        if self._block != '':
            STARTBLOCK  = self._block
            ENDBLOCK    = self._endblock
            if ENDBLOCK == '':
                ENDBLOCK = STARTBLOCK

            citebody = ''.join([('   %s\n' % line.strip()) for line in cites])

            fheader = STARTBLOCK + '\n' + \
                    PAD + 'CODATA 2014 CONSTANTS FROM NIST SRD121\n' + \
                    PAD + time.asctime() + '\n\n' + \
                    citebody + \
                    ENDBLOCK + '\n'

        # no block comments, comment every line
        else:
            CMNT = self._comment
            CMNTSP = CMNT + ' '

            citebody = CMNTSP.join([('%s\n' % line.strip()) for line in cites])

            fheader = CMNT + '\n' + \
                    CMNT + PAD + 'CODATA 2014 CONSTANTS FROM NIST SRD121\n' + \
                    CMNT + PAD + time.asctime() + '\n' + \
                    CMNT + '\n' + \
                    CMNT + ' ' + citebody + \
                    CMNT + '\n'

        return fheader

    #________________________________________________

    def formatMembers(self,cname,cdict):

        description = self.Description( cname, cdict['Category'])

        '''value & symbol fold into /defines/ string'''
        value       = self.Value( cdict['Value'])
        symbol      = self.Symbol( cdict['Symbol'], cname)
        defines     = self.Define( symbol, value)

        uncerts     = self.Uncertainty( cdict['Uncertainty'])
        units       = self.Units( cdict['Unit'])

        return description,defines,uncerts,units

    #________________________________________________

    def BuildDefinition (self,cname,cdict):
        ''''construct a declaration for a CODATA constant.

        Python output looks like:

        # Planck constant               (universal)
        h = 6.626070040e-34             # +/-0.000000081e-34 in units: 'J s'
        '''
        description,defines,uncerts,units = self.formatMembers(cname,cdict)

        # language-specific string
        CMNT = self._comment
        PAD = self._indent

        definition =CMNT + PAD + description + '\n' + \
                    defines + CMNT + PAD + uncerts + PAD + units + '\n'

        return definition

    # _______________________________________________________

    def FileTail(self,fname='<stdout>'):

        ftail = self._comment + \
            (' END file: %s as %s %s\n' % \
            (fname,self._language,time.asctime()))

        return ftail

# __________________________________________________________________________________

class FormatPython(LanguageFormat):
    def __init__(self): #,language,comment,indent,block,endblock):

        self._language    = 'Python'
        self._comment     = '#'
        self._indent      = ' '
        self._block       = "'''"
        self._endblock    = "'''"

    def Define (self,sym,val):
        s =  ("%s = %s" % (sym,val))
        return ("%-39s" % s)


# __________________________________________________________________________________

class FormatCansi(LanguageFormat):

    def __init__(self): #,language,comment,indent,block,endblock):

        self._language    = 'C-K&R'
        self._comment     = ''
        self._indent      = ' '
        self._block       = "/*"
        self._endblock    = "*/"

    '''
    output is:
    #define symbol = numeric ASCII
    '''
    def Define (self,sym,val):
        s =  ("#define %s %s" % (sym,val))
        return ("%-39s" % s)

    ''' ANSI C wraps lines in block comments'''

    def BuildDefinition (self,cname,cdict):
        description,defines,uncerts,units = self.formatMembers(cname,cdict)
        uu = uncerts+' '+units
        definition = self.Wrapline(description,self._block,self._endblock,78) + \
                    '\n' + \
                    defines + \
                    self.Wrapline(uu,self._block,self._endblock,39) + \
                    '\n'
        return definition

    def FileTail(self,fname='<stdout>'):
        notes = ('END file: %s as %s %s' % \
            (fname,self._language,time.asctime()))
        ftail = self.Wrapline(notes,self._block,self._endblock) + '\n'
        return ftail
# __________________________________________________________________________________

class FormatC99(LanguageFormat):

    def __init__(self): #,language,comment,indent,block,endblock):

        self._language    = 'C99'
        self._comment     = '//'
        self._indent      = ' '
        self._block       = "/*"
        self._endblock    = "*/"

    '''
    output is:
    #define symbol = numeric ASCII
    '''
    def Define (self,sym,val):
        s =  ("#define %s %s" % (sym,val))
        return ("%-39s" % s)
# ________________________________________________________________________
class FormatFortran77(LanguageFormat):

    def __init__ (self):

        self._language    = 'Fortran 77'
        self._comment     = 'C'
        self._indent      = '      '
        self._block       = ''
        self._endblock    = ''

    def Define (self,sym,val):
        defs = self._indent + ("double precision %s\n" % (sym)) + \
               self._indent + ("parameter(%s = %s)\n" % (sym,val))
        return defs

    def Value (self,val):
        val = val.lower()

        ''' "1.23e4" --> "1.23d4" '''
        if 'e' in val:
            val = val.replace('e','d')

        ''' "123" --> "123.0" '''
        if '.' not in val:
            val += '.0'

        return val

    def BuildDefinition (self,cname,cdict):
        description,defines,uncerts,units = self.formatMembers(cname,cdict)

        # language-specific string
        ''''OUTPUT:
        C Planck constant                       (universal)
        C +/-0.000000081e-34 in units 'J s'
              double precision h
              parameter(h = 6.626070040e-34)
        '''
        CMNT = self._comment

        definition =CMNT + ' ' + description + '\n' + \
                    CMNT + ' ' + uncerts + ' ' + units + '\n' + \
                    defines

        return definition

# ________________________________________________________________________

class FormatFortran90(LanguageFormat):

    def __init__ (self):

        self._language    = 'Fortran 90'
        self._comment     = '!'
        self._indent      = '      '
        self._block       = ''
        self._endblock    = ''

    def Define (self,sym,val):
        defs = self._indent + ("real*8, parameter :: %s = %s\n" % (sym,val))
        return defs

    def Value (self,val):
        val = val.lower()

        ''' "1.23e4" --> "1.23d4" '''
        if 'e' in val:
            val = val.replace('e','d')

        ''' "123" --> "123.0" '''
        if '.' not in val:
            val += '.0'

        return val

    def BuildDefinition (self,cname,cdict):
        description,defines,uncerts,units = self.formatMembers(cname,cdict)

        ''''  OUTPUT:
        ! Planck constant                       (universal)
        ! +/-0.000000081e-34 in units 'J s'
              real*8, parameter :: h = 6.626070040e-34
        '''
        CMNT = self._comment

        definition =CMNT + ' ' + description + '\n' + \
                    CMNT + ' ' + uncerts + ' ' + units + '\n' + \
                    defines

        return definition

# ________________________________________________________________________
def _test_formats ():


    def ruler ():
        print('    +    1    +    2    +    3    +    4    +    5    +    6    +    7    +    8')
        print('12345678901234567890123456789012345678901234567890123456789012345678901234567890')
    # ________________________________________________________________________

    dictionary = {}

    key = "Planck constant"
    dictionary[key] = {
      "Value":      "6.626070040e-34",
      "Uncertainty":"0.000000081e-34",
      "Unit":       "J s",
      "Category":   "universal",
      "Symbol":     "h"
    }

    print('\n#### BEGIN %s test\n' % __file__.upper())

    ruler()
    py = FormatPython()
    #print (py.FileHead())
    print (py.BuildDefinition(key, dictionary[key]))
    print (py.FileTail())

    ruler()

    Cknr = FormatCansi()
    #print (Cknr.FileHead())
    print (Cknr.BuildDefinition(key, dictionary[key]))
    print (Cknr.FileTail())

    ruler()

    c99 = FormatC99()
    #print (c99.FileHead())
    print (c99.BuildDefinition(key, dictionary[key]))
    print (c99.FileTail())

    ruler()

    f77 = FormatFortran77()
    #print (f77.FileHead())
    print (f77.BuildDefinition(key, dictionary[key]))
    print (f77.FileTail())

    ruler()

    f90 = FormatFortran90()
    #print (f90.FileHead())
    print (f90.BuildDefinition(key, dictionary[key]))
    print (f90.FileTail())
    ruler()

    print('\n#### END %s test\n' % __file__.upper())

    return

# __________________________________________________________________________________

if __name__ == "__main__":

    _test_formats()
    sys.exit(0)

