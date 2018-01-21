MANUAL
======

USAGE
-----

TYPE:

    gencodata

SEE:

    gencodata generates CODATA physical constants
    header files in C, Fortan, or Python(default) syntax.

    usage: gencodata [-h] [-l] [-i INPUT] [-o OUTPUT] [-c CSV] [-j JSON]
        [-s SYNTAX]
        [category [category ...]]

------------------------------------------------------------------------

### OPTIONS

TYPE:

    gencodata -h

> or  
> gencodata --help
>
SEE:

    usage: gencodata    [-h] [-l] [-i INPUT] [-o OUTPUT] [-c CSV] [-j JSON]
            [-s SYNTAX]
            [category [category ...]]

    positional arguments:
      category          Print constant declarations from one or more
                categories. Categories are: all, X-ray, alpha,
                physicochemical, equivalents, atomic units,
                electromagnetic, atomic, universal, electron, uncat,
                deuteron, electroweak, helion, muon, natural, neutron,
                proton, tau, triton

    optional arguments:
      -h, --help        show this help message and exit
      -l, --list        list constants, either all or within a category.
                Overrides file output.
      -i INPUT, --input INPUT
                print constants from list in file
      -o OUTPUT, --output OUTPUT
                write results to an output file
      -c CSV, --csv CSV     write results to a CSV file
      -j JSON, --json JSON  write results to a JSON file
      -s SYNTAX, --syntax SYNTAX
                Select C,C99,Fortran,F77,F90, or Python (default)
                output, case-insensitive

------------------------------------------------------------------------

### WHICH CONSTANT CATEGORY?

The 337 CODATA 2014 constants and equivalences are grouped by category and may be listed by name within a category.

| Category         | Count | Category        | Count |
|------------------|-------|-----------------|-------|
| alpha            | 7     | natural         | 10    |
| atomic           | 9     | neutron         | 24    |
| **atomic units** | 22    | physicochemical | 22    |
| deuteron         | 15    | proton          | 26    |
| electromagnetic  | 18    | tau             | 11    |
| electron         | 28    | triton          | 11    |
| electroweak      | 2     | uncat           | 15    |
| equivalents      | 58    | universal       | 20    |
| helion           | 18    | X-ray           | 4     |
| muon             | 17    |                 |       |

The 'uncat' category is transitional.

To list only names of the atomic constants, type:

    gencodata X-ray -l

> or  
> gencodata X-ray --list
>
with the result:

    Angstrom star
    Cu x unit
    Mo x unit
    {220} lattice spacing of silicon

Note that these are fully qualified CODATA names and not the symbols by which they are defined and used. The python output for "Angstrom star" is:

    # Angstrom star                        (X-ray)
    W_K_alpha = 1.00001495e-10             # +/-0.00000090e-10 in units 'm'

...where W\_K\_alpha refers to the tungsten K-alpha line wavelength, once so ubiquitous in crystallography that it has its own name. The underscores may seem to be overused but it is hoped they may ease the chore of referencing these constants in LaTex or MathML markup languages.

To list all constant names:

    gencodata all -l

> or  
> gencodata -l all
>
> or  
> gencodata --list all
>
The results of the above command are omitted for obvious eye-glazing reasons.

All other output flags are ignored when the '--list' flag appears in the command line. This command:

    gencodata atomic -l -s C99 -o outfile.h

is effectively truncated to:

    gencodata atomic -l

NOTE -- The **"atomic units"** category is distinct from **"atomic"** and must be quoted in the command string:

    gencodata "atomic units"

------------------------------------------------------------------------

### WHICH CONSTANTS?

To print the 9 atomic constant definitions at the console in Python syntax TYPE:

    gencodata atomic

Several categories may be specified:

    gencodata atomic universal physicochemical

------------------------------------------------------------------------

### USING SELECTED CONSTANTS

The constants we want usually reside in different categories. You can specify single CODATA constants in a text file, one name to a line.

Constant name searches are case insensitive -- pLaNcK CoNsTaNt is treated the same as Planck constant. Lines that begin with a \# hash are optional and ignored. Same goes for octothorpes. An example file follows:

    # ----------------file "a_few.txt" begins ----------------
    Speed of light in vacuum
    Avogadro constant
    #
    Planck constant
    Boltzmann constant
    #
    Hartree energy
    molar gas constant
    Joule-calorie relationship
    # ----------------file "a_few.txt" ends ------------------

Read in the file, print the output at console:

    gencodata -i a_few.txt

> or  
> gencodata --input a\_few.txt
>
The output should contain:

    ...
    # Avogadro constant                    (physicochemical)
    N_A = 6.022140857e23                   # +/-0.000000074e23 in units 'mol^{-1}'

    # Boltzmann constant                   (physicochemical)
    k_B = 1.38064852e-23                   # +/-0.00000079e-23 in units 'J K^{-1}'

    # Hartree energy                       (atomic)
    E_h = 4.359744650e-18                  # +/-0.000000054e-18 in units 'J'
    ...

The definitions are alphabetized by CODATA name to simplify visual searching through source code.

To write results as a Python (default) file:

    gencodata -i a_few.txt -o a_few.py

> or  
> gencodata --input a\_few.txt --output a\_few.py
>
------------------------------------------------------------------------

### LANGUAGE OUTPUT SYNTAX

You may select from several syntax formats with these command line arguments for the -s, or --syntax flags:

    C         - pre- C99, using /*,*/ block commenting
    C99       - uses C++ '//' line commenting where reasonable

    Fortran   - Fortran 77 'C' commenting and parameter syntax
        64-bit REAL is of type "double precision"
    F, F77    - as above

    Fortran90,F90 -
          - Fortran 90 '!' commenting and parameter syntax
        64-bit REAL is of type "real*8"

    python    - default output syntax

These are case-insensitive,i.e., 'c99' is the same as 'C99'.

To write the X-ray constants in Fortran 77 syntax to console, type:

    gencodata X-ray -s F77

Constant declarations are presented consistently:

**PYTHON**:

    # Avogadro constant                 (physicochemical)
    N_A = 6.022140857e23                # +/- 0.000000074e23 in units: 'mol^{-1}'

**FORTRAN 77**:

    C  Avogadro constant                (physicochemical)
    C  +/- 0.000000074e23      in units 'mol^{-1}'
          double precision N_A
          parameter( N_A = 6.022140857d23)

**C99**:

    // Avogadro constant                (physicochemical)
    #define N_A 6.022140857e23          // +/-0.000000074e23 units 'mol^{-1}'

------------------------------------------------------------------------

### WRITE OUTPUT TO FILE

TYPE:

    gencodata atomic -o fileName.py

> or  
> gencodata atomic --output fileName.py
>
To write the X-ray constants in Fortran 77 syntax to a file, type:

    gencodata X-ray -s F77 -o xrayconst.F

------------------------------------------------------------------------

CSV and JSON file output is optional using flags -c,-j (--csv,--json).

**Writing CSV files**

Sometimes, you need to examine the entire CODATA 2014 corpus, preferably as a spreadsheet. You can write all CODATA 2014 constants and their properties to a CSV file for import into a spreedsheet application.

TYPE:

    gencodata all -c codata2014.csv

> or  
> gencodata all --csv codata2014.csv
>
The CSV header is:

    "Quantity ","Category","Symbol","Uncertainty","Unit","Value"

Data is formatted as:

    "Planck constant","universal","h","0.000000081e-34","J s","6.626070040e-34"

All CSV data fields are quoted 7-bit ASCII strings in order to ensure an accurate representation of the published constant values. Accuracy of numerical text conversion to IEEE 754 binary floating point formats then depends on the user's software toolchain.

**Writing JSON files**

The JSON file output can usually be imported directly into Python source code for immediate use. **Gencodata**'s JSON output format is an unordered dictionary:

    "planck constant": {
      "Category":   "universal",
      "Symbol":     "h",
      "Uncertainty":    "0.000000081e-34",
      "Quantity ":  "Planck constant",
      "Value":      "6.626070040e-34",
      "Unit":       "J s"
    }

To print the atomic category as a JSON file, type:

    gencodata atomic --json atomic.json

> or  
> gencodata atomic -j atomic.json
>
------------------------------------------------------------------------

Copyright 2017, Daniel R. Haney
