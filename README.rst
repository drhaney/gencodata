
GENCODATA
=========


**gencodata generates physical constant header files in C, Fortran, and Python syntaxes.**

| Scientific software can suffer from using expressions of physical 
| constants which are dated or imprecise (i.e., wrong).

**gencodata**'s physical constant values are current and authoritative \ 
since they are extracted from the \ 
`NIST CODATA 2014 document SRD121 \ 
<https://catalog.data.gov/dataset/nist-codata-fundamental-physical-constants-srd-121>`_
, a machine-parsable summary of the primary reference::

    CODATA recommended values of the fundamental physical constants: 2014
    Peter J. Mohr, David B. Newell,and Barry N. Taylor
    REVIEWS OF MODERN PHYSICS, VOLUME 88, JULY-SEPTEMBER 2016 (73 pages)
    DOI: 10.1103/RevModPhys.88.035009

The reference article is linked from \ `NIST Reference on Constants,Units,and Uncertainty \ 
<https://physics.nist.gov/cuu/Constants/article2014.html>`_ 


----------


USAGE
----------

| This example writes the Universal constants (speed of light, Planck, etc)
| definitions in Fortran 77 syntax to an output file named "universal.Fh".

::

    gencodata universal --syntax fortran --output universal.Fh

The short form is::

    gencodata universal -s f -o universal.Fh



Without arguments, the **gencodata** command prints::

    gencodata generates CODATA physical constants
    header files in C, Fortan, or Python(default) syntax.

    usage: gencodata [-h] [-l] [-i INPUT] [-o OUTPUT] [-c CSV] [-j JSON]
		[-s SYNTAX]
		[category [category ...]]


For more information, type::

    gencodata --help

----------

Copyright 2017, Daniel R. Haney
