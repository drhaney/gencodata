THE INCONSTANT HARTREE
======================

The accepted value of the molar Hartree-to-kilocalorie equivalence is

> **627.509 541 kcal/Hartree**

Although deriving from the original 1928 Atomic Units definition by Douglas Hartree
and calculated from CODATA 1986 constants, it would be adequate were it consistently
applied.

A perusal of scientific software shows that Hartree values are usually out
of date, often truncated, sometimes inconsistent, even occasionally
mistranscribed. Calculations from such software have systematic errors
that are larger and more variable than might otherwise be.

Post-CODATA 2006, the molar Hartree-to-kilocalorie equivalence **should** be:

> **627.509 474 kcal/Hartree**

This value has shown only 3e-09 relative variation averaged over two decades.

Searching NWChem source code for "627.5" and its variations reveals the
Hartree-kcal equivalence to be variously stated as:

> | value           | comment                                     |
> |-----------------|---------------------------------------------|
> | 627.5           | truncated                                   |
> | 627.51          | truncated                                   |
> | 627.509 5       | truncated                                   |
> | 627.509 **541** | up to 1986 from Atomic Units (AU)           |
> | 627.509 **451** | **mistranscription of 1986 AU above**       |
> | 627.509 552     | 1986 Rydberg equation, should be 627.509559 |
> | 627.509 331 4   | apocryphal (and wrong)                      |
>
**Low energy thermochemical computations such as those for Zero-point, spin**
**orbital, and hydrogen-bond energies are particularly sensitive to these**
**inconsistencies.**

The Hartree/particle value is usually obtained from one of three equations
which primarily use either the Rydberg constant, or the Fine-structure
constant, or electron mass and elementary charge, the last from Douglas
Hartree's Atomic Units (AU) system.

The antique Atomic Unit formula value persists despite its ~1.0e-6
relative error disagreement with other methods even after the CODATA 1986
adjustments.

The Rydberg-based equation is preferable for its simplicity and low
propagated error. **R** is known to 13 decimals and **c** is exact by decree.
Therefore, the Planck constant **h** inaccuracy &lt;2.0e-10 determines the Hartree
energy inaccuracy:

> **E\_h = 2Rhc**
>
> > = 4.359744650e-18 +/-0.000000054e-18 Joules (0.012 ppm rel. err)
>
> where:
>
> E\_h = Hartree energy R = Rydberg constant h = Planck constant c = Speed of light

The molar Hartree-kilocalorie equivalence is calculated from:

> **Ha\_kcal = E\_h \* N\_A / 4.184 / 1000.0**
>
> where:
>
> E\_h = Hartree energy N\_A = Avogadro constant 4.184 is the decreed Joules-to-kcal equivalence

The Hartree (E\_h) relative uncertainty depends largely on those of the
Planck and Rydberg constants which, since the 1986 CODATA revision, are
always less than 1.0e-8 combined. The Rydberg constant's uncertainty
contribution, at &lt;6.0e-12, is comparatively insignificant. For the molar
Hartree value, the error contribution from Avogadro's constant is large
enough that the molar Rydberg-Hartree's last digit may be gratuitous
(see table).

> |         |                   |             |           |
> |---------|-------------------|-------------|-----------|
> | year    | Rydberg Hartree   | error       | error     |
> |         | (kcal) abso       | lute ppm    |           |
> | ======= | ================= | =========== | ========= |
> | 1986    | 627.50956         | 5.3E-04     | 0.85      |
> | 1998    | 627.509471        | 6.9E-05     | 0.11      |
> | 2002    | 627.50947         | 1.5E-04     | 0.23      |
> | 2006    | 627.509469        | 4.4E-05     | 0.07      |
> | 2010    | 627.509474        | 3.9E-05     | 0.06      |
> | 2014    | 627.509474        | 1.1E-05     | 0.02      |
>
------------------------------------------------------------------------

Copyright 2017, Daniel R. Haney
