#!/usr/bin/env python
"""
 codata.py - create codata constants dictionary from the
            CODATA 2014 JSON file.

 EXPORTS:
     Citation()
        return CODATA citation string

     Dictionary ()
        return CODATA constants dictionary

     Value(constantname='')
        return ASCII numeric string for a constant

     Uncertainty(constantname='')
        return ASCII numeric string of a constant

     Units(constantname='')
        return units string of a constant

     Properties(constantname='')
        return properties dictionary of a constant

     Symbol(constantname='')
        return ASCII symbol string of a constant

     Categories()
        return list containing names of all constant categories

     Names()
        return list containing names of all constants

     Constants(category='')
        return dictionary of constants within a category

     WriteJSON (cdict={},outfile='')
        write a constants dictionary as a JSON file

     WriteCSV (cdict={},outfile='')
        write a constants dictionary as a CSV file


 creation: 10/19/2017
 author: drh
"""

VersionString = '0.1'

import os
import sys
import json

# -- global defs

# set NewCodataFile = True to rebuild dictionary at execution
# time
#   else
# default to pre-built CODATA 2014 dictionary.

NewCodataFile = True    # qFalse
_codata2014_file_ = 'srd121_allascii_2014.json'
_symbol_file = 'symbols.json'


if NewCodataFile == True:

    _phys_const_    = {}
    _citation_      = ""

else:

    '''This dictionary was created from the CODATA 2014 json
    file and amended by the "symbols.json" file.

    The codata 2014 JSON file provided by the CODATA Group
    is authoritative and is used here without change.

    The symbol file was created by the author and contains
    provisional variable names for CODATA constants and the
    categories to which they belong.
    '''

    _citation_ ='CODATA recommended values of the fundamental physical constants: 2014\n\
    Peter J. Mohr, David B. Newell,and Barry N. Taylor\n\
    REVIEWS OF MODERN PHYSICS, VOLUME 88, JULY-SEPTEMBER 2016 (73 pages)\n\
    DOI: 10.1103/RevModPhys.88.035009\n'

    _phys_const_ = \
    {
      "bohr radius": {
        "Category": "atomic",
        "Symbol": "a0",
        "Uncertainty": "0.00000000012e-10",
        "Quantity ": "Bohr radius",
        "Value": "0.52917721067e-10",
        "Unit": "m"
      },
      "quantum of circulation times 2": {
        "Category": "universal",
        "Symbol": "h_over_2m_e",
        "Uncertainty": "0.0000000033e-4",
        "Quantity ": "quantum of circulation times 2",
        "Value": "7.2738950972e-4",
        "Unit": "m^2 s^{-1}"
      },
      "hertz-inverse meter relationship": {
        "Category": "equivalents",
        "Symbol": "Hz_to_inv_m",
        "Uncertainty": "0.0",
        "Quantity ": "hertz-inverse meter relationship",
        "Value": "3.335640951e-9",
        "Unit": "m^{-1}"
      },
      "unified atomic mass unit": {
        "Category": "equivalents",
        "Symbol": "u",
        "Uncertainty": "0.000000020e-27",
        "Quantity ": "unified atomic mass unit",
        "Value": "1.660539040e-27",
        "Unit": "kg"
      },
      "atomic mass unit-kelvin relationship": {
        "Category": "equivalents",
        "Symbol": "AMU_to_K",
        "Uncertainty": "0.00000062e13",
        "Quantity ": "atomic mass unit-kelvin relationship",
        "Value": "1.08095438e13",
        "Unit": "K"
      },
      "boltzmann constant in inverse meters per kelvin": {
        "Category": "physicochemical",
        "Symbol": "k_B_over_hc",
        "Uncertainty": "0.000040",
        "Quantity ": "Boltzmann constant in inverse meters per kelvin",
        "Value": "69.503457",
        "Unit": "m^{-1} K^{-1}"
      },
      "deuteron molar mass": {
        "Category": "deuteron",
        "Symbol": "M_d",
        "Uncertainty": "0.000000000040e-3",
        "Quantity ": "deuteron molar mass",
        "Value": "2.013553212745e-3",
        "Unit": "kg mol^{-1}"
      },
      "shielded helion to shielded proton mag mom ratio": {
        "Category": "helion",
        "Symbol": "mu_prime_h_over_mu_prime_p",
        "Uncertainty": "0.0000000033",
        "Quantity ": "shielded helion to shielded proton mag. mom. ratio",
        "Value": "-0.7617861313",
        "Unit": ""
      },
      "hertz-kelvin relationship": {
        "Category": "equivalents",
        "Symbol": "Hz_to_K",
        "Uncertainty": "0.0000028e-11",
        "Quantity ": "hertz-kelvin relationship",
        "Value": "4.7992447e-11",
        "Unit": "K"
      },
      "neutron gyromag ratio": {
        "Category": "neutron",
        "Symbol": "gamma_n",
        "Uncertainty": "0.00000043e8",
        "Quantity ": "neutron gyromag. ratio",
        "Value": "1.83247172e8",
        "Unit": "s^{-1} T^{-1}"
      },
      "mag flux quantum": {
        "Category": "electromagnetic",
        "Symbol": "Phi0",
        "Uncertainty": "0.000000013e-15",
        "Quantity ": "mag. flux quantum",
        "Value": "2.067833831e-15",
        "Unit": "Wb"
      },
      "joule-electron volt relationship": {
        "Category": "equivalents",
        "Symbol": "J_to_eV",
        "Uncertainty": "0.000000038e18",
        "Quantity ": "joule-electron volt relationship",
        "Value": "6.241509126e18",
        "Unit": "eV"
      },
      "neutron-electron mag mom ratio": {
        "Category": "neutron",
        "Symbol": "mu_n_over_mu_e",
        "Uncertainty": "0.00000025e-3",
        "Quantity ": "neutron-electron mag. mom. ratio",
        "Value": "1.04066882e-3",
        "Unit": ""
      },
      "planck constant over 2 pi": {
        "Category": "universal",
        "Symbol": "hbar",
        "Uncertainty": "0.000000013e-34",
        "Quantity ": "Planck constant over 2 pi",
        "Value": "1.054571800e-34",
        "Unit": "J s"
      },
      "stefan-boltzmann constant": {
        "Category": "physicochemical",
        "Symbol": "sigma",
        "Uncertainty": "0.000013e-8",
        "Quantity ": "Stefan-Boltzmann constant",
        "Value": "5.670367e-8",
        "Unit": "W m^{-2} K^{-4}"
      },
      "joule-kilogram relationship": {
        "Category": "equivalents",
        "Symbol": "J_to_kg",
        "Uncertainty": "0.0",
        "Quantity ": "joule-kilogram relationship",
        "Value": "1.112650056e-17",
        "Unit": "kg"
      },
      "atomic unit of mag flux density": {
        "Category": "atomic units",
        "Symbol": "AU_mag_flux_density",
        "Uncertainty": "0.000000014e5",
        "Quantity ": "atomic unit of mag. flux density",
        "Value": "2.350517550e5",
        "Unit": "T"
      },
      "electron-deuteron mass ratio": {
        "Category": "electron",
        "Symbol": "m_e_over_m_d",
        "Uncertainty": "0.000000000096e-4",
        "Quantity ": "electron-deuteron mass ratio",
        "Value": "2.724437107484e-4",
        "Unit": ""
      },
      "deuteron mag mom to nuclear magneton ratio": {
        "Category": "deuteron",
        "Symbol": "mu_d_over_mu_N",
        "Uncertainty": "0.0000000048",
        "Quantity ": "deuteron mag. mom. to nuclear magneton ratio",
        "Value": "0.8574382311",
        "Unit": ""
      },
      "electron to shielded proton mag mom ratio": {
        "Category": "electron",
        "Symbol": "mu_e_over_mu_prime_P",
        "Uncertainty": "0.0000072",
        "Quantity ": "electron to shielded proton mag. mom. ratio",
        "Value": "-658.2275971",
        "Unit": ""
      },
      "muon mass in u": {
        "Category": "muon",
        "Symbol": "m_mu_in_u",
        "Uncertainty": "0.0000000025",
        "Quantity ": "muon mass in u",
        "Value": "0.1134289257",
        "Unit": "u"
      },
      "natural unit of time": {
        "Category": "natural",
        "Symbol": "nu_time",
        "Uncertainty": "0.00000000058e-21",
        "Quantity ": "natural unit of time",
        "Value": "1.28808866712e-21",
        "Unit": "s"
      },
      "neutron-proton mag mom ratio": {
        "Category": "neutron",
        "Symbol": "mu_n_over_mu_P",
        "Uncertainty": "0.00000016",
        "Quantity ": "neutron-proton mag. mom. ratio",
        "Value": "-0.68497934",
        "Unit": ""
      },
      "proton mag mom ": {
        "Category": "proton",
        "Symbol": "mu_P",
        "Uncertainty": "0.0000000097e-26",
        "Quantity ": "proton mag. mom.",
        "Value": "1.4106067873e-26",
        "Unit": "J T^{-1}"
      },
      "conductance quantum": {
        "Category": "electromagnetic",
        "Symbol": "G0",
        "Uncertainty": "0.0000000018e-5",
        "Quantity ": "conductance quantum",
        "Value": "7.7480917310e-5",
        "Unit": "S"
      },
      "natural unit of velocity": {
        "Category": "natural",
        "Symbol": "nu_velocity",
        "Uncertainty": "0.0",
        "Quantity ": "natural unit of velocity",
        "Value": "299792458",
        "Unit": "m s^{-1}"
      },
      "electron mag mom to nuclear magneton ratio": {
        "Category": "electron",
        "Symbol": "mu_e_over_mu_N",
        "Uncertainty": "0.00000017",
        "Quantity ": "electron mag. mom. to nuclear magneton ratio",
        "Value": "-1838.28197234",
        "Unit": ""
      },
      "tau-neutron mass ratio": {
        "Category": "tau",
        "Symbol": "m_tau_over_m_n",
        "Uncertainty": "0.00017",
        "Quantity ": "tau-neutron mass ratio",
        "Value": "1.89111",
        "Unit": ""
      },
      "standard acceleration of gravity": {
        "Category": "equivalents",
        "Symbol": "g_n",
        "Uncertainty": "0.0",
        "Quantity ": "standard acceleration of gravity",
        "Value": "9.80665",
        "Unit": "m s^{-2}"
      },
      "electron mag mom anomaly": {
        "Category": "electron",
        "Symbol": "a_e",
        "Uncertainty": "0.00000000026e-3",
        "Quantity ": "electron mag. mom. anomaly",
        "Value": "1.15965218091e-3",
        "Unit": ""
      },
      "deuteron-proton mass ratio": {
        "Category": "deuteron",
        "Symbol": "m_d_over_m_P",
        "Uncertainty": "0.00000000019",
        "Quantity ": "deuteron-proton mass ratio",
        "Value": "1.99900750087",
        "Unit": ""
      },
      "faraday constant": {
        "Category": "physicochemical",
        "Symbol": "F",
        "Uncertainty": "0.00059",
        "Quantity ": "Faraday constant",
        "Value": "96485.33289",
        "Unit": "C mol^{-1}"
      },
      "electron-neutron mass ratio": {
        "Category": "electron",
        "Symbol": "m_e_over_m_n",
        "Uncertainty": "0.0000000027e-4",
        "Quantity ": "electron-neutron mass ratio",
        "Value": "5.4386734428e-4",
        "Unit": ""
      },
      "planck mass energy equivalent in gev": {
        "Category": "universal",
        "Symbol": "m_P_c2",
        "Uncertainty": "0.000029e19",
        "Quantity ": "Planck mass energy equivalent in GeV",
        "Value": "1.220910e19",
        "Unit": "GeV"
      },
      "neutron-proton mass difference in u": {
        "Category": "neutron",
        "Symbol": "m_n_diff_m_P_in_u",
        "Uncertainty": "0.00000000051",
        "Quantity ": "neutron-proton mass difference in u",
        "Value": "0.00138844900",
        "Unit": ""
      },
      "electron volt-hertz relationship": {
        "Category": "equivalents",
        "Symbol": "eV_to_Hz",
        "Uncertainty": "0.000000015e14",
        "Quantity ": "electron volt-hertz relationship",
        "Value": "2.417989262e14",
        "Unit": "Hz"
      },
      "conventional value of josephson constant": {
        "Category": "electromagnetic",
        "Symbol": "K_J_old",
        "Uncertainty": "0.0",
        "Quantity ": "conventional value of Josephson constant",
        "Value": "483597.9e9",
        "Unit": "Hz V^{-1}"
      },
      "muon compton wavelength": {
        "Category": "muon",
        "Symbol": "lambda_C",
        "Uncertainty": "0.00000026e-15",
        "Quantity ": "muon Compton wavelength",
        "Value": "11.73444111e-15",
        "Unit": "m"
      },
      "lattice parameter of silicon": {
        "Category": "X-ray",
        "Symbol": "a",
        "Uncertainty": "0.0000089e-12",
        "Quantity ": "lattice parameter of silicon",
        "Value": "543.1020504e-12",
        "Unit": "m"
      },
      "proton gyromag ratio over 2 pi": {
        "Category": "proton",
        "Symbol": "lambda_P_over_2pi",
        "Uncertainty": "0.00000029",
        "Quantity ": "proton gyromag. ratio over 2 pi",
        "Value": "42.57747892",
        "Unit": "MHz T^{-1}"
      },
      "loschmidt constant (273 15 k, 100 kpa)": {
        "Category": "physicochemical",
        "Symbol": "n_0",
        "Uncertainty": "0.0000015e25",
        "Quantity ": "Loschmidt constant (273.15 K, 100 kPa)",
        "Value": "2.6516467e25",
        "Unit": "m^{-3}"
      },
      "deuteron mass in u": {
        "Category": "deuteron",
        "Symbol": "m_d_in_u",
        "Uncertainty": "0.000000000040",
        "Quantity ": "deuteron mass in u",
        "Value": "2.013553212745",
        "Unit": "u"
      },
      "rydberg constant times hc in j": {
        "Category": "atomic",
        "Symbol": "Rinf_J",
        "Uncertainty": "0.000000027e-18",
        "Quantity ": "Rydberg constant times hc in J",
        "Value": "2.179872325e-18",
        "Unit": "J"
      },
      "triton-electron mass ratio": {
        "Category": "triton",
        "Symbol": "m_t_over_m_e",
        "Uncertainty": "0.00000026",
        "Quantity ": "triton-electron mass ratio",
        "Value": "5496.92153588",
        "Unit": ""
      },
      "electric constant": {
        "Category": "universal",
        "Symbol": "mu_0",
        "Uncertainty": "0.0",
        "Quantity ": "electric constant",
        "Value": "8.854187817e-12",
        "Unit": "F m^{-1}"
      },
      "helion mass in u": {
        "Category": "helion",
        "Symbol": "m_h_in_u",
        "Uncertainty": "0.00000000012",
        "Quantity ": "helion mass in u",
        "Value": "3.01493224673",
        "Unit": "u"
      },
      "atomic unit of mom um": {
        "Category": "atomic units",
        "Symbol": "AU_momum",
        "Uncertainty": "0.000000024e-24",
        "Quantity ": "atomic unit of mom.um",
        "Value": "1.992851882e-24",
        "Unit": "kg m s^{-1}"
      },
      "hartree-electron volt relationship": {
        "Category": "equivalents",
        "Symbol": "Ha_to_eV",
        "Uncertainty": "0.00000017",
        "Quantity ": "hartree-electron volt relationship",
        "Value": "27.21138602",
        "Unit": "eV"
      },
      "characteristic impedance of vacuum": {
        "Category": "universal",
        "Symbol": "Z_0",
        "Uncertainty": "0.0",
        "Quantity ": "characteristic impedance of vacuum",
        "Value": "376.730313461",
        "Unit": "ohm"
      },
      "newtonian constant of gravitation": {
        "Category": "universal",
        "Symbol": "G",
        "Uncertainty": "0.00031e-11",
        "Quantity ": "Newtonian constant of gravitation",
        "Value": "6.67408e-11",
        "Unit": "m^3 kg^{-1} s^{-2}"
      },
      "helion mass energy equivalent": {
        "Category": "helion",
        "Symbol": "m_h_c2",
        "Uncertainty": "0.000000055e-10",
        "Quantity ": "helion mass energy equivalent",
        "Value": "4.499539341e-10",
        "Unit": "J"
      },
      "thomson cross section": {
        "Category": "electron",
        "Symbol": "sigma_e",
        "Uncertainty": "0.00000000091e-28",
        "Quantity ": "Thomson cross section",
        "Value": "0.66524587158e-28",
        "Unit": "m^2"
      },
      "shielded helion gyromag ratio over 2 pi": {
        "Category": "helion",
        "Symbol": "gamma_prime_h_over_2pi",
        "Uncertainty": "0.00000043",
        "Quantity ": "shielded helion gyromag. ratio over 2 pi",
        "Value": "32.43409966",
        "Unit": "MHz T^{-1}"
      },
      "josephson constant": {
        "Category": "electromagnetic",
        "Symbol": "K_J",
        "Uncertainty": "0.0030e9",
        "Quantity ": "Josephson constant",
        "Value": "483597.8525e9",
        "Unit": "Hz V^{-1}"
      },
      "atomic unit of force": {
        "Category": "atomic units",
        "Symbol": "AU_force",
        "Uncertainty": "0.00000010e-8",
        "Quantity ": "atomic unit of force",
        "Value": "8.23872336e-8",
        "Unit": "N"
      },
      "standard atmosphere": {
        "Category": "equivalents",
        "Symbol": "atm",
        "Uncertainty": "0.0",
        "Quantity ": "standard atmosphere",
        "Value": "101325",
        "Unit": "Pa"
      },
      "hertz-joule relationship": {
        "Category": "equivalents",
        "Symbol": "Hz_to_J",
        "Uncertainty": "0.000000081e-34",
        "Quantity ": "hertz-joule relationship",
        "Value": "6.626070040e-34",
        "Unit": "J"
      },
      "alpha particle mass": {
        "Category": "alpha",
        "Symbol": "m_alpha",
        "Uncertainty": "0.000000082e-27",
        "Quantity ": "alpha particle mass",
        "Value": "6.644657230e-27",
        "Unit": "kg"
      },
      "wien wavelength displacement law constant": {
        "Category": "physicochemical",
        "Symbol": "b_wein_prime",
        "Uncertainty": "0.0000017e-3",
        "Quantity ": "Wien wavelength displacement law constant",
        "Value": "2.8977729e-3",
        "Unit": "m K"
      },
      "atomic unit of mag dipole mom ": {
        "Category": "atomic units",
        "Symbol": "AU_mag_dipole_mom",
        "Uncertainty": "0.000000011e-23",
        "Quantity ": "atomic unit of mag. dipole mom.",
        "Value": "1.854801999e-23",
        "Unit": "J T^{-1}"
      },
      "standard-state pressure": {
        "Category": "equivalents",
        "Symbol": "ssp",
        "Uncertainty": "0.0",
        "Quantity ": "standard-state pressure",
        "Value": "100000",
        "Unit": "Pa"
      },
      "helion mass energy equivalent in mev": {
        "Category": "helion",
        "Symbol": "m_h_c2_in_MeV",
        "Uncertainty": "0.000017",
        "Quantity ": "helion mass energy equivalent in MeV",
        "Value": "2808.391586",
        "Unit": "MeV"
      },
      "atomic mass constant": {
        "Category": "physicochemical",
        "Symbol": "m_u",
        "Uncertainty": "0.000000020e-27",
        "Quantity ": "atomic mass constant",
        "Value": "1.660539040e-27",
        "Unit": "kg"
      },
      "rydberg constant times hc in ev": {
        "Category": "atomic",
        "Symbol": "Rinf_eV",
        "Uncertainty": "0.000000084",
        "Quantity ": "Rydberg constant times hc in eV",
        "Value": "13.605693009",
        "Unit": "eV"
      },
      "elementary charge": {
        "Category": "electromagnetic",
        "Symbol": "e",
        "Uncertainty": "0.0000000098e-19",
        "Quantity ": "elementary charge",
        "Value": "1.6021766208e-19",
        "Unit": "C"
      },
      "inverse meter-hartree relationship": {
        "Category": "equivalents",
        "Symbol": "inv_m_to_Ha",
        "Uncertainty": "0.000000000027e-8",
        "Quantity ": "inverse meter-hartree relationship",
        "Value": "4.556335252767e-8",
        "Unit": "E_h"
      },
      "fermi coupling constant": {
        "Category": "electroweak",
        "Symbol": "G_F_over_hbarc3",
        "Uncertainty": "0.0000006e-5",
        "Quantity ": "Fermi coupling constant",
        "Value": "1.1663787e-5",
        "Unit": "GeV^{-2}"
      },
      "atomic unit of electric field": {
        "Category": "atomic units",
        "Symbol": "AU_electric_field",
        "Uncertainty": "0.000000032e11",
        "Quantity ": "atomic unit of electric field",
        "Value": "5.142206707e11",
        "Unit": "V m^{-1}"
      },
      "muon-tau mass ratio": {
        "Category": "muon",
        "Symbol": "m_mu_over_m_tau",
        "Uncertainty": "0.00054e-2",
        "Quantity ": "muon-tau mass ratio",
        "Value": "5.94649e-2",
        "Unit": ""
      },
      "tau mass in u": {
        "Category": "tau",
        "Symbol": "m_tau_in_u",
        "Uncertainty": "0.00017",
        "Quantity ": "tau mass in u",
        "Value": "1.90749",
        "Unit": "u"
      },
      "electron-proton mass ratio": {
        "Category": "electron",
        "Symbol": "m_e_over_m_P",
        "Uncertainty": "0.00000000052e-4",
        "Quantity ": "electron-proton mass ratio",
        "Value": "5.44617021352e-4",
        "Unit": ""
      },
      "natural unit of mass": {
        "Category": "natural",
        "Symbol": "nu_mass",
        "Uncertainty": "0.00000011e-31",
        "Quantity ": "natural unit of mass",
        "Value": "9.10938356e-31",
        "Unit": "kg"
      },
      "calorie-joule relationship": {
        "Category": "equivalents",
        "Symbol": "cal_to_J",
        "Uncertainty": "0.0",
        "Quantity ": "calorie-Joule relationship",
        "Value": "2.3900573613766729e-01",
        "Unit": "cal/J"
      },
      "electron mass energy equivalent": {
        "Category": "electron",
        "Symbol": "m_e_c2",
        "Uncertainty": "0.00000010e-14",
        "Quantity ": "electron mass energy equivalent",
        "Value": "8.18710565e-14",
        "Unit": "J"
      },
      "atomic unit of permittivity": {
        "Category": "atomic units",
        "Symbol": "AU_permittivity",
        "Uncertainty": "0.0",
        "Quantity ": "atomic unit of permittivity",
        "Value": "1.112650056e-10",
        "Unit": "F m^{-1}"
      },
      "atomic mass unit-inverse meter relationship": {
        "Category": "equivalents",
        "Symbol": "AMU_to_inv_m",
        "Uncertainty": "0.0000000034e14",
        "Quantity ": "atomic mass unit-inverse meter relationship",
        "Value": "7.5130066166e14",
        "Unit": "m^{-1}"
      },
      "atomic unit of magnetizability": {
        "Category": "atomic units",
        "Symbol": "AU_magnetizability",
        "Uncertainty": "0.0000000090e-29",
        "Quantity ": "atomic unit of magnetizability",
        "Value": "7.8910365886e-29",
        "Unit": "J T^{-2}"
      },
      "molar gas constant": {
        "Category": "physicochemical",
        "Symbol": "Rgas",
        "Uncertainty": "0.0000048",
        "Quantity ": "molar gas constant",
        "Value": "8.3144598",
        "Unit": "J mol^{-1} K^{-1}"
      },
      "{220} lattice spacing of silicon": {
        "Category": "X-ray",
        "Symbol": "d_220",
        "Uncertainty": "0.0000032e-12",
        "Quantity ": "{220} lattice spacing of silicon",
        "Value": "192.0155714e-12",
        "Unit": "m"
      },
      "atomic unit of time": {
        "Category": "atomic units",
        "Symbol": "AU_time",
        "Uncertainty": "0.000000000014e-17",
        "Quantity ": "atomic unit of time",
        "Value": "2.418884326509e-17",
        "Unit": "s"
      },
      "mo x unit": {
        "Category": "X-ray",
        "Symbol": "Mo_K_alpha",
        "Uncertainty": "0.00000053e-13",
        "Quantity ": "Mo x unit",
        "Value": "1.00209952e-13",
        "Unit": "m"
      },
      "planck length": {
        "Category": "universal",
        "Symbol": "l_P",
        "Uncertainty": "0.000038e-35",
        "Quantity ": "Planck length",
        "Value": "1.616229e-35",
        "Unit": "m"
      },
      "speed of light in vacuum": {
        "Category": "universal",
        "Symbol": "c",
        "Uncertainty": "0.0",
        "Quantity ": "speed of light in vacuum",
        "Value": "299792458",
        "Unit": "m s^{-1}"
      },
      "shielded proton mag mom to nuclear magneton ratio": {
        "Category": "proton",
        "Symbol": "mu_prime_P_over_mu_N",
        "Uncertainty": "0.000000030",
        "Quantity ": "shielded proton mag. mom. to nuclear magneton ratio",
        "Value": "2.792775600",
        "Unit": ""
      },
      "cu x unit": {
        "Category": "X-ray",
        "Symbol": "Co_K_alpha",
        "Uncertainty": "0.00000028e-13",
        "Quantity ": "Cu x unit",
        "Value": "1.00207697e-13",
        "Unit": "m"
      },
      "neutron gyromag ratio over 2 pi": {
        "Category": "neutron",
        "Symbol": "gamma_n_over_2pi",
        "Uncertainty": "0.0000069",
        "Quantity ": "neutron gyromag. ratio over 2 pi",
        "Value": "29.1646933",
        "Unit": "MHz T^{-1}"
      },
      "proton mass energy equivalent": {
        "Category": "proton",
        "Symbol": "m_P_c2",
        "Uncertainty": "0.000000018e-10",
        "Quantity ": "proton mass energy equivalent",
        "Value": "1.503277593e-10",
        "Unit": "J"
      },
      "compton wavelength over 2 pi": {
        "Category": "electron",
        "Symbol": "lambdabar_c",
        "Uncertainty": "0.00000018e-15",
        "Quantity ": "Compton wavelength over 2 pi",
        "Value": "386.15926764e-15",
        "Unit": "m"
      },
      "boltzmann constant in ev/k": {
        "Category": "physicochemical",
        "Symbol": "k_B_in_eV",
        "Uncertainty": "0.0000050e-5",
        "Quantity ": "Boltzmann constant in eV/K",
        "Value": "8.6173303e-5",
        "Unit": "eV K^{-1}"
      },
      "inverse meter-atomic mass unit relationship": {
        "Category": "equivalents",
        "Symbol": "inv_m_to_AMU",
        "Uncertainty": "0.00000000061e-15",
        "Quantity ": "inverse meter-atomic mass unit relationship",
        "Value": "1.33102504900e-15",
        "Unit": "u"
      },
      "weak mixing angle": {
        "Category": "electroweak",
        "Symbol": "sin2omega_W",
        "Uncertainty": "0.0021",
        "Quantity ": "weak mixing angle",
        "Value": "0.2223",
        "Unit": ""
      },
      "helion-proton mass ratio": {
        "Category": "helion",
        "Symbol": "m_h_over_m_p",
        "Uncertainty": "0.00000000029",
        "Quantity ": "helion-proton mass ratio",
        "Value": "2.99315267046",
        "Unit": ""
      },
      "triton mass energy equivalent": {
        "Category": "triton",
        "Symbol": "m_t_c2",
        "Uncertainty": "0.000000055e-10",
        "Quantity ": "triton mass energy equivalent",
        "Value": "4.500387735e-10",
        "Unit": "J"
      },
      "shielded helion gyromag ratio": {
        "Category": "helion",
        "Symbol": "gamma_prime_h",
        "Uncertainty": "0.000000027e8",
        "Quantity ": "shielded helion gyromag. ratio",
        "Value": "2.037894585e8",
        "Unit": "s^{-1} T^{-1}"
      },
      "inverse of conductance quantum": {
        "Category": "electromagnetic",
        "Symbol": "G0_inv",
        "Uncertainty": "0.0000029",
        "Quantity ": "inverse of conductance quantum",
        "Value": "12906.4037278",
        "Unit": "ohm"
      },
      "electron mass in u": {
        "Category": "electron",
        "Symbol": "m_e_in_u",
        "Uncertainty": "0.00000000016e-4",
        "Quantity ": "electron mass in u",
        "Value": "5.48579909070e-4",
        "Unit": "u"
      },
      "kilogram-atomic mass unit relationship": {
        "Category": "equivalents",
        "Symbol": "kg_to_AMU",
        "Uncertainty": "0.000000074e26",
        "Quantity ": "kilogram-atomic mass unit relationship",
        "Value": "6.022140857e26",
        "Unit": "u"
      },
      "atomic mass unit-hertz relationship": {
        "Category": "equivalents",
        "Symbol": "AMU_to_Hz",
        "Uncertainty": "0.0000000010e23",
        "Quantity ": "atomic mass unit-hertz relationship",
        "Value": "2.2523427206e23",
        "Unit": "Hz"
      },
      "atomic unit of length": {
        "Category": "atomic units",
        "Symbol": "AU_length",
        "Uncertainty": "0.00000000012e-10",
        "Quantity ": "atomic unit of length",
        "Value": "0.52917721067e-10",
        "Unit": "m"
      },
      "natural unit of length": {
        "Category": "natural",
        "Symbol": "nu_length",
        "Uncertainty": "0.00000018e-15",
        "Quantity ": "natural unit of length",
        "Value": "386.15926764e-15",
        "Unit": "m"
      },
      "neutron compton wavelength": {
        "Category": "neutron",
        "Symbol": "lambda_C_n",
        "Uncertainty": "0.00000000088e-15",
        "Quantity ": "neutron Compton wavelength",
        "Value": "1.31959090481e-15",
        "Unit": "m"
      },
      "electron volt-kilogram relationship": {
        "Category": "equivalents",
        "Symbol": "eV_to_kg",
        "Uncertainty": "0.000000011e-36",
        "Quantity ": "electron volt-kilogram relationship",
        "Value": "1.782661907e-36",
        "Unit": "kg"
      },
      "electron-deuteron mag mom ratio": {
        "Category": "electron",
        "Symbol": "mu_e_over_mu_prime_d",
        "Uncertainty": "0.000012",
        "Quantity ": "electron-deuteron mag. mom. ratio",
        "Value": "-2143.923499",
        "Unit": ""
      },
      "electron charge to mass quotient": {
        "Category": "electron",
        "Symbol": "e_over_m_e",
        "Uncertainty": "0.000000011e11",
        "Quantity ": "electron charge to mass quotient",
        "Value": "-1.758820024e11",
        "Unit": "C kg^{-1}"
      },
      "proton mag mom to nuclear magneton ratio": {
        "Category": "proton",
        "Symbol": "mu_P_over_mu_N",
        "Uncertainty": "0.0000000085",
        "Quantity ": "proton mag. mom. to nuclear magneton ratio",
        "Value": "2.7928473508",
        "Unit": ""
      },
      "kelvin-hartree relationship": {
        "Category": "equivalents",
        "Symbol": "K_to_Ha",
        "Uncertainty": "0.0000018e-6",
        "Quantity ": "kelvin-hartree relationship",
        "Value": "3.1668105e-6",
        "Unit": "E_h"
      },
      "inverse fine-structure constant": {
        "Category": "atomic",
        "Symbol": "alpha_inv",
        "Uncertainty": "0.000000031",
        "Quantity ": "inverse fine-structure constant",
        "Value": "137.035999139",
        "Unit": ""
      },
      "triton molar mass": {
        "Category": "triton",
        "Symbol": "M_t",
        "Uncertainty": "0.00000000011e-3",
        "Quantity ": "triton molar mass",
        "Value": "3.01550071632e-3",
        "Unit": "kg mol^{-1}"
      },
      "deuteron-electron mag mom ratio": {
        "Category": "deuteron",
        "Symbol": "mu_d_over_m_e",
        "Uncertainty": "0.000000026e-4",
        "Quantity ": "deuteron-electron mag. mom. ratio",
        "Value": "-4.664345535e-4",
        "Unit": ""
      },
      "classical electron radius": {
        "Category": "electron",
        "Symbol": "r_e",
        "Uncertainty": "0.0000000019e-15",
        "Quantity ": "classical electron radius",
        "Value": "2.8179403227e-15",
        "Unit": "m"
      },
      "helion-electron mass ratio": {
        "Category": "helion",
        "Symbol": "m_h_over_m_e",
        "Uncertainty": "0.00000027",
        "Quantity ": "helion-electron mass ratio",
        "Value": "5495.88527922",
        "Unit": ""
      },
      "atomic mass unit-joule relationship": {
        "Category": "equivalents",
        "Symbol": "AMU_to_J",
        "Uncertainty": "0.000000018e-10",
        "Quantity ": "atomic mass unit-joule relationship",
        "Value": "1.492418062e-10",
        "Unit": "J"
      },
      "proton mag shielding correction": {
        "Category": "proton",
        "Symbol": "sigma_prime_P",
        "Uncertainty": "0.011e-6",
        "Quantity ": "proton mag. shielding correction",
        "Value": "25.691e-6",
        "Unit": ""
      },
      "tau compton wavelength over 2 pi": {
        "Category": "tau",
        "Symbol": "lambda_C_over_2pi",
        "Uncertainty": "0.000010e-15",
        "Quantity ": "tau Compton wavelength over 2 pi",
        "Value": "0.111056e-15",
        "Unit": "m"
      },
      "neutron mass energy equivalent in mev": {
        "Category": "neutron",
        "Symbol": "m_n_c2_in_MeV",
        "Uncertainty": "0.0000058",
        "Quantity ": "neutron mass energy equivalent in MeV",
        "Value": "939.5654133",
        "Unit": "MeV"
      },
      "neutron-proton mass difference energy equivalent in mev": {
        "Category": "neutron",
        "Symbol": "m_n_diff_m_P_c2_in_MeV",
        "Uncertainty": "0.00000048",
        "Quantity ": "neutron-proton mass difference energy equivalent in MeV",
        "Value": "1.29333205",
        "Unit": ""
      },
      "fine-structure constant": {
        "Category": "atomic",
        "Symbol": "alpha",
        "Uncertainty": "0.0000000017e-3",
        "Quantity ": "fine-structure constant",
        "Value": "7.2973525664e-3",
        "Unit": ""
      },
      "hertz-electron volt relationship": {
        "Category": "equivalents",
        "Symbol": "Hz_to_eV",
        "Uncertainty": "0.000000025e-15",
        "Quantity ": "hertz-electron volt relationship",
        "Value": "4.135667662e-15",
        "Unit": "eV"
      },
      "deuteron mass energy equivalent in mev": {
        "Category": "deuteron",
        "Symbol": "m_d_c2_in_MeV",
        "Uncertainty": "0.000012",
        "Quantity ": "deuteron mass energy equivalent in MeV",
        "Value": "1875.612928",
        "Unit": "MeV"
      },
      "compton wavelength": {
        "Category": "electron",
        "Symbol": "lambda_c",
        "Uncertainty": "0.0000000011e-12",
        "Quantity ": "Compton wavelength",
        "Value": "2.4263102367e-12",
        "Unit": "m"
      },
      "kelvin-joule relationship": {
        "Category": "equivalents",
        "Symbol": "K_to_J",
        "Uncertainty": "0.00000079e-23",
        "Quantity ": "kelvin-joule relationship",
        "Value": "1.38064852e-23",
        "Unit": "J"
      },
      "alpha particle molar mass": {
        "Category": "alpha",
        "Symbol": "M_alpha",
        "Uncertainty": "0.000000000063e-3",
        "Quantity ": "alpha particle molar mass",
        "Value": "4.001506179127e-3",
        "Unit": "kg mol^{-1}"
      },
      "deuteron mag mom ": {
        "Category": "deuteron",
        "Symbol": "mu_d",
        "Uncertainty": "0.0000000036e-26",
        "Quantity ": "deuteron mag. mom.",
        "Value": "0.4330735040e-26",
        "Unit": "J T^{-1}"
      },
      "inverse meter-joule relationship": {
        "Category": "equivalents",
        "Symbol": "inv_m_to_J",
        "Uncertainty": "0.000000024e-25",
        "Quantity ": "inverse meter-joule relationship",
        "Value": "1.986445824e-25",
        "Unit": "J"
      },
      "proton compton wavelength over 2 pi": {
        "Category": "proton",
        "Symbol": "lambda_C_P_over_2pi",
        "Uncertainty": "0.000000000097e-15",
        "Quantity ": "proton Compton wavelength over 2 pi",
        "Value": "0.210308910109e-15",
        "Unit": "m"
      },
      "muon mag mom to bohr magneton ratio": {
        "Category": "muon",
        "Symbol": "mu_mu_over_mu_B",
        "Uncertainty": "0.00000011e-3",
        "Quantity ": "muon mag. mom. to Bohr magneton ratio",
        "Value": "-4.84197048e-3",
        "Unit": ""
      },
      "deuteron rms charge radius": {
        "Category": "deuteron",
        "Symbol": "r_d",
        "Uncertainty": "0.0025e-15",
        "Quantity ": "deuteron rms charge radius",
        "Value": "2.1413e-15",
        "Unit": "m"
      },
      "faraday constant for conventional electric current": {
        "Category": "physicochemical",
        "Symbol": "F_star",
        "Uncertainty": "0.0012",
        "Quantity ": "Faraday constant for conventional electric current",
        "Value": "96485.3251",
        "Unit": "C_{90} mol^{-1}"
      },
      "proton mass in u": {
        "Category": "proton",
        "Symbol": "m_P_in_u",
        "Uncertainty": "0.000000000091",
        "Quantity ": "proton mass in u",
        "Value": "1.007276466879",
        "Unit": "u"
      },
      "neutron-electron mass ratio": {
        "Category": "neutron",
        "Symbol": "m_n_over_m_e",
        "Uncertainty": "0.00000090",
        "Quantity ": "neutron-electron mass ratio",
        "Value": "1838.68366158",
        "Unit": ""
      },
      "electron-proton mag mom ratio": {
        "Category": "electron",
        "Symbol": "mu_e_over_mu_P",
        "Uncertainty": "0.0000020",
        "Quantity ": "electron-proton mag. mom. ratio",
        "Value": "-658.2106866",
        "Unit": ""
      },
      "deuteron-electron mass ratio": {
        "Category": "deuteron",
        "Symbol": "m_d_over_m_e",
        "Uncertainty": "0.00000013",
        "Quantity ": "deuteron-electron mass ratio",
        "Value": "3670.48296785",
        "Unit": ""
      },
      "proton mag mom to bohr magneton ratio": {
        "Category": "proton",
        "Symbol": "mu_P_over_mu_B",
        "Uncertainty": "0.0000000046e-3",
        "Quantity ": "proton mag. mom. to Bohr magneton ratio",
        "Value": "1.5210322053e-3",
        "Unit": ""
      },
      "helion g factor": {
        "Category": "helion",
        "Symbol": "g_h",
        "Uncertainty": "0.000000050",
        "Quantity ": "helion g factor",
        "Value": "-4.255250616",
        "Unit": ""
      },
      "shielded proton mag mom to bohr magneton ratio": {
        "Category": "proton",
        "Symbol": "mu_prime_P_over_mu_B",
        "Uncertainty": "0.000000017e-3",
        "Quantity ": "shielded proton mag. mom. to Bohr magneton ratio",
        "Value": "1.520993128e-3",
        "Unit": ""
      },
      "bohr magneton": {
        "Category": "electromagnetic",
        "Symbol": "mu_B",
        "Uncertainty": "0.0000057e-26",
        "Quantity ": "Bohr magneton",
        "Value": "927.4009994e-26",
        "Unit": "J T^{-1}"
      },
      "kelvin-inverse meter relationship": {
        "Category": "equivalents",
        "Symbol": "K_to_inv_m",
        "Uncertainty": "0.000040",
        "Quantity ": "kelvin-inverse meter relationship",
        "Value": "69.503457",
        "Unit": "m^{-1}"
      },
      "shielded helion mag mom ": {
        "Category": "helion",
        "Symbol": "mu_prime_h",
        "Uncertainty": "0.000000014e-26",
        "Quantity ": "shielded helion mag. mom.",
        "Value": "-1.074553080e-26",
        "Unit": "J T^{-1}"
      },
      "hartree-joule relationship": {
        "Category": "equivalents",
        "Symbol": "Ha_to_J",
        "Uncertainty": "0.000000054e-18",
        "Quantity ": "hartree-joule relationship",
        "Value": "4.359744650e-18",
        "Unit": "J"
      },
      "neutron mag mom ": {
        "Category": "neutron",
        "Symbol": "mu_n",
        "Uncertainty": "0.00000023e-26",
        "Quantity ": "neutron mag. mom.",
        "Value": "-0.96623650e-26",
        "Unit": "J T^{-1}"
      },
      "hartree-kilogram relationship": {
        "Category": "equivalents",
        "Symbol": "Ha_to_kg",
        "Uncertainty": "0.000000060e-35",
        "Quantity ": "hartree-kilogram relationship",
        "Value": "4.850870129e-35",
        "Unit": "kg"
      },
      "quantum of circulation": {
        "Category": "universal",
        "Symbol": "h_over_m_e",
        "Uncertainty": "0.0000000017e-4",
        "Quantity ": "quantum of circulation",
        "Value": "3.6369475486e-4",
        "Unit": "m^2 s^{-1}"
      },
      "helion mag mom ": {
        "Category": "helion",
        "Symbol": "mu_h",
        "Uncertainty": "0.000000014e-26",
        "Quantity ": "helion mag. mom.",
        "Value": "-1.074617522e-26",
        "Unit": "J T^{-1}"
      },
      "electron-neutron mag mom ratio": {
        "Category": "electron",
        "Symbol": "mu_e_over_mu_n",
        "Uncertainty": "0.00023",
        "Quantity ": "electron-neutron mag. mom. ratio",
        "Value": "960.92050",
        "Unit": ""
      },
      "shielded proton gyromag ratio over 2 pi": {
        "Category": "proton",
        "Symbol": "lambda_prime_over_2pi",
        "Uncertainty": "0.00000053",
        "Quantity ": "shielded proton gyromag. ratio over 2 pi",
        "Value": "42.57638507",
        "Unit": "MHz T^{-1}"
      },
      "kilogram-joule relationship": {
        "Category": "equivalents",
        "Symbol": "kg_to_J",
        "Uncertainty": "0.0",
        "Quantity ": "kilogram-joule relationship",
        "Value": "8.987551787e16",
        "Unit": "J"
      },
      "neutron-proton mass difference": {
        "Category": "neutron",
        "Symbol": "m_n_diff_m_P",
        "Uncertainty": "0.00000085e-30",
        "Quantity ": "neutron-proton mass difference",
        "Value": "2.30557377e-30",
        "Unit": ""
      },
      "bohr magneton in k/t": {
        "Category": "electromagnetic",
        "Symbol": "mu_B_over_k",
        "Uncertainty": "0.00000039",
        "Quantity ": "Bohr magneton in K/T",
        "Value": "0.67171405",
        "Unit": "K T^{-1}"
      },
      "molar volume of silicon": {
        "Category": "equivalents",
        "Symbol": "V_m_Si",
        "Uncertainty": "0.00000061e-6",
        "Quantity ": "molar volume of silicon",
        "Value": "12.05883214e-6",
        "Unit": "m^3 mol^{-1}"
      },
      "helion molar mass": {
        "Category": "helion",
        "Symbol": "M_h",
        "Uncertainty": "0.00000000012e-3",
        "Quantity ": "helion molar mass",
        "Value": "3.01493224673e-3",
        "Unit": "kg mol^{-1}"
      },
      "proton g factor": {
        "Category": "proton",
        "Symbol": "g_P",
        "Uncertainty": "0.000000017",
        "Quantity ": "proton g factor",
        "Value": "5.585694702",
        "Unit": ""
      },
      "hertz-atomic mass unit relationship": {
        "Category": "equivalents",
        "Symbol": "Hz_to_AMU",
        "Uncertainty": "0.0000000020e-24",
        "Quantity ": "hertz-atomic mass unit relationship",
        "Value": "4.4398216616e-24",
        "Unit": "u"
      },
      "joule-hertz relationship": {
        "Category": "equivalents",
        "Symbol": "J_to_Hz",
        "Uncertainty": "0.000000019e33",
        "Quantity ": "joule-hertz relationship",
        "Value": "1.509190205e33",
        "Unit": "Hz"
      },
      "tau molar mass": {
        "Category": "tau",
        "Symbol": "M_tau",
        "Uncertainty": "0.00017e-3",
        "Quantity ": "tau molar mass",
        "Value": "1.90749e-3",
        "Unit": "kg mol^{-1}"
      },
      "deuteron-neutron mag mom ratio": {
        "Category": "deuteron",
        "Symbol": "mu_d_over_m_n",
        "Uncertainty": "0.00000011",
        "Quantity ": "deuteron-neutron mag. mom. ratio",
        "Value": "-0.44820652",
        "Unit": ""
      },
      "joule-atomic mass unit relationship": {
        "Category": "equivalents",
        "Symbol": "J_to_AMU",
        "Uncertainty": "0.000000082e9",
        "Quantity ": "joule-atomic mass unit relationship",
        "Value": "6.700535363e9",
        "Unit": "u"
      },
      "shielded helion mag mom to nuclear magneton ratio": {
        "Category": "helion",
        "Symbol": "mu_prime_h_over_mu_N",
        "Uncertainty": "0.000000025",
        "Quantity ": "shielded helion mag. mom. to nuclear magneton ratio",
        "Value": "-2.127497720",
        "Unit": ""
      },
      "neutron-proton mass difference energy equivalent": {
        "Category": "neutron",
        "Symbol": "m_n_diff_m_P_c2",
        "Uncertainty": "0.00000076e-13",
        "Quantity ": "neutron-proton mass difference energy equivalent",
        "Value": "2.07214637e-13",
        "Unit": ""
      },
      "electron gyromag ratio over 2 pi": {
        "Category": "electron",
        "Symbol": "gammabar_e",
        "Uncertainty": "0.00017",
        "Quantity ": "electron gyromag. ratio over 2 pi",
        "Value": "28024.95164",
        "Unit": "MHz T^{-1}"
      },
      "muon mag mom ": {
        "Category": "muon",
        "Symbol": "mu_mu",
        "Uncertainty": "0.00000010e-26",
        "Quantity ": "muon mag. mom.",
        "Value": "-4.49044826e-26",
        "Unit": "J T^{-1}"
      },
      "planck constant in ev s": {
        "Category": "universal",
        "Symbol": "h_eV",
        "Uncertainty": "0.000000025e-15",
        "Quantity ": "Planck constant in eV s",
        "Value": "4.135667662e-15",
        "Unit": "eV s"
      },
      "planck mass": {
        "Category": "universal",
        "Symbol": "m_P",
        "Uncertainty": "0.000051e-8",
        "Quantity ": "Planck mass",
        "Value": "2.176470e-8",
        "Unit": "kg"
      },
      "conventional value of von klitzing constant": {
        "Category": "electromagnetic",
        "Symbol": "R_K_old",
        "Uncertainty": "0.0",
        "Quantity ": "conventional value of von Klitzing constant",
        "Value": "25812.807",
        "Unit": "ohm"
      },
      "electron volt-joule relationship": {
        "Category": "equivalents",
        "Symbol": "eV_to_J",
        "Uncertainty": "0.0000000098e-19",
        "Quantity ": "electron volt-joule relationship",
        "Value": "1.6021766208e-19",
        "Unit": "J"
      },
      "electron-triton mass ratio": {
        "Category": "electron",
        "Symbol": "m_e_over_m_t",
        "Uncertainty": "0.000000000084e-4",
        "Quantity ": "electron-triton mass ratio",
        "Value": "1.819200062203e-4",
        "Unit": ""
      },
      "muon mass energy equivalent in mev": {
        "Category": "muon",
        "Symbol": "m_mu_c2_in_MeV",
        "Uncertainty": "0.0000024",
        "Quantity ": "muon mass energy equivalent in MeV",
        "Value": "105.6583745",
        "Unit": "MeV"
      },
      "electron mag mom ": {
        "Category": "electron",
        "Symbol": "mu_e",
        "Uncertainty": "0.0000057e-26",
        "Quantity ": "electron mag. mom.",
        "Value": "-928.4764620e-26",
        "Unit": "J T^{-1}"
      },
      "natural unit of energy": {
        "Category": "natural",
        "Symbol": "nu_energy",
        "Uncertainty": "0.00000010e-14",
        "Quantity ": "natural unit of energy",
        "Value": "8.18710565e-14",
        "Unit": "J"
      },
      "joule-calorie relationship": {
        "Category": "equivalents",
        "Symbol": "J_to_cal",
        "Uncertainty": "0.0",
        "Quantity ": "Joule-calorie relationship",
        "Value": "4.184",
        "Unit": "J/cal"
      },
      "muon-proton mag mom ratio": {
        "Category": "muon",
        "Symbol": "mu_mu_over_mu_P",
        "Uncertainty": "0.000000071",
        "Quantity ": "muon-proton mag. mom. ratio",
        "Value": "-3.183345142",
        "Unit": ""
      },
      "deuteron mass energy equivalent": {
        "Category": "deuteron",
        "Symbol": "m_d_c2",
        "Uncertainty": "0.000000037e-10",
        "Quantity ": "deuteron mass energy equivalent",
        "Value": "3.005063183e-10",
        "Unit": "J"
      },
      "neutron g factor": {
        "Category": "neutron",
        "Symbol": "g_n",
        "Uncertainty": "0.00000090",
        "Quantity ": "neutron g factor",
        "Value": "-3.82608545",
        "Unit": ""
      },
      "kilogram-kelvin relationship": {
        "Category": "equivalents",
        "Symbol": "kg_to_K",
        "Uncertainty": "0.0000037e39",
        "Quantity ": "kilogram-kelvin relationship",
        "Value": "6.5096595e39",
        "Unit": "K"
      },
      "muon mag mom anomaly": {
        "Category": "muon",
        "Symbol": "a_mu",
        "Uncertainty": "0.00000063e-3",
        "Quantity ": "muon mag. mom. anomaly",
        "Value": "1.16592089e-3",
        "Unit": ""
      },
      "electron volt-atomic mass unit relationship": {
        "Category": "equivalents",
        "Symbol": "eV_to_AMU",
        "Uncertainty": "0.0000000066e-9",
        "Quantity ": "electron volt-atomic mass unit relationship",
        "Value": "1.0735441105e-9",
        "Unit": "u"
      },
      "neutron-muon mass ratio": {
        "Category": "neutron",
        "Symbol": "m_n_over_m_mu",
        "Uncertainty": "0.00000020",
        "Quantity ": "neutron-muon mass ratio",
        "Value": "8.89248408",
        "Unit": ""
      },
      "joule-hartree relationship": {
        "Category": "equivalents",
        "Symbol": "J_to_Ha",
        "Uncertainty": "0.000000028e17",
        "Quantity ": "joule-hartree relationship",
        "Value": "2.293712317e17",
        "Unit": "E_h"
      },
      "deuteron mass": {
        "Category": "deuteron",
        "Symbol": "m_d",
        "Uncertainty": "0.000000041e-27",
        "Quantity ": "deuteron mass",
        "Value": "3.343583719e-27",
        "Unit": "kg"
      },
      "helion mag mom to bohr magneton ratio": {
        "Category": "helion",
        "Symbol": "mu_h_over_mu_B",
        "Uncertainty": "0.000000014e-3",
        "Quantity ": "helion mag. mom. to Bohr magneton ratio",
        "Value": "-1.158740958e-3",
        "Unit": ""
      },
      "newtonian constant of gravitation over h-bar c": {
        "Category": "universal",
        "Symbol": "G_hbar_over_c",
        "Uncertainty": "0.00031e-39",
        "Quantity ": "Newtonian constant of gravitation over h-bar c",
        "Value": "6.70861e-39",
        "Unit": "(GeV/c^2)^-2"
      },
      "triton mag mom to nuclear magneton ratio": {
        "Category": "triton",
        "Symbol": "mu_t_over_mu_N",
        "Uncertainty": "0.000000014",
        "Quantity ": "triton mag. mom. to nuclear magneton ratio",
        "Value": "2.978962460",
        "Unit": ""
      },
      "muon-proton mass ratio": {
        "Category": "muon",
        "Symbol": "m_mu_over_m_P",
        "Uncertainty": "0.0000000025",
        "Quantity ": "muon-proton mass ratio",
        "Value": "0.1126095262",
        "Unit": ""
      },
      "electron volt-hartree relationship": {
        "Category": "equivalents",
        "Symbol": "eV_to_Ha",
        "Uncertainty": "0.000000023e-2",
        "Quantity ": "electron volt-hartree relationship",
        "Value": "3.674932248e-2",
        "Unit": "E_h"
      },
      "von klitzing constant": {
        "Category": "electromagnetic",
        "Symbol": "R_K",
        "Uncertainty": "0.0000059",
        "Quantity ": "von Klitzing constant",
        "Value": "25812.8074555",
        "Unit": "ohm"
      },
      "shielded helion mag mom to bohr magneton ratio": {
        "Category": "helion",
        "Symbol": "mu_prime_h_over_mu_B",
        "Uncertainty": "0.000000014e-3",
        "Quantity ": "shielded helion mag. mom. to Bohr magneton ratio",
        "Value": "-1.158671471e-3",
        "Unit": ""
      },
      "kilogram-electron volt relationship": {
        "Category": "equivalents",
        "Symbol": "kg_to_eV",
        "Uncertainty": "0.000000034e35",
        "Quantity ": "kilogram-electron volt relationship",
        "Value": "5.609588650e35",
        "Unit": "eV"
      },
      "electron to alpha particle mass ratio": {
        "Category": "electron",
        "Symbol": "mu_e_over_mu_a",
        "Uncertainty": "0.000000000045e-4",
        "Quantity ": "electron to alpha particle mass ratio",
        "Value": "1.370933554798e-4",
        "Unit": ""
      },
      "alpha particle-electron mass ratio": {
        "Category": "alpha",
        "Symbol": "m_alpha_over_m_e",
        "Uncertainty": "0.00000024",
        "Quantity ": "alpha particle-electron mass ratio",
        "Value": "7294.29954136",
        "Unit": ""
      },
      "shielded proton mag mom ": {
        "Category": "proton",
        "Symbol": "mu_prime_P",
        "Uncertainty": "0.000000018e-26",
        "Quantity ": "shielded proton mag. mom.",
        "Value": "1.410570547e-26",
        "Unit": "J T^{-1}"
      },
      "kelvin-electron volt relationship": {
        "Category": "equivalents",
        "Symbol": "K_to_eV",
        "Uncertainty": "0.0000050e-5",
        "Quantity ": "kelvin-electron volt relationship",
        "Value": "8.6173303e-5",
        "Unit": "eV"
      },
      "atomic unit of 1st hyperpolarizability": {
        "Category": "atomic units",
        "Symbol": "AU_1st_hyperpolarizability",
        "Uncertainty": "0.000000020e-53",
        "Quantity ": "atomic unit of 1st hyperpolarizability",
        "Value": "3.206361329e-53",
        "Unit": "C^3 m^3 J^{-2}"
      },
      "atomic unit of velocity": {
        "Category": "atomic units",
        "Symbol": "AU_velocity",
        "Uncertainty": "0.00000000050e6",
        "Quantity ": "atomic unit of velocity",
        "Value": "2.18769126277e6",
        "Unit": "m s^{-1}"
      },
      "atomic mass constant energy equivalent": {
        "Category": "physicochemical",
        "Symbol": "m_u_c2",
        "Uncertainty": "0.000000018e-10",
        "Quantity ": "atomic mass constant energy equivalent",
        "Value": "1.492418062e-10",
        "Unit": "J"
      },
      "natural unit of action": {
        "Category": "natural",
        "Symbol": "nu_action",
        "Uncertainty": "0.000000013e-34",
        "Quantity ": "natural unit of action",
        "Value": "1.054571800e-34",
        "Unit": "J s"
      },
      "kilogram-hartree relationship": {
        "Category": "equivalents",
        "Symbol": "kg_to_Ha",
        "Uncertainty": "0.000000025e34",
        "Quantity ": "kilogram-hartree relationship",
        "Value": "2.061485823e34",
        "Unit": "E_h"
      },
      "kilogram-hertz relationship": {
        "Category": "equivalents",
        "Symbol": "kg_to_Hz",
        "Uncertainty": "0.000000017e50",
        "Quantity ": "kilogram-hertz relationship",
        "Value": "1.356392512e50",
        "Unit": "Hz"
      },
      "muon mass energy equivalent": {
        "Category": "muon",
        "Symbol": "m_mu_c2",
        "Uncertainty": "0.000000043e-11",
        "Quantity ": "muon mass energy equivalent",
        "Value": "1.692833774e-11",
        "Unit": "J"
      },
      "muon mass": {
        "Category": "muon",
        "Symbol": "m_mu",
        "Uncertainty": "0.000000048e-28",
        "Quantity ": "muon mass",
        "Value": "1.883531594e-28",
        "Unit": "kg"
      },
      "electron-muon mass ratio": {
        "Category": "electron",
        "Symbol": "m_e_over_m_u",
        "Uncertainty": "0.00000011e-3",
        "Quantity ": "electron-muon mass ratio",
        "Value": "4.83633170e-3",
        "Unit": ""
      },
      "proton mass energy equivalent in mev": {
        "Category": "proton",
        "Symbol": "m_P_c2_in_MeV",
        "Uncertainty": "0.0000058",
        "Quantity ": "proton mass energy equivalent in MeV",
        "Value": "938.2720813",
        "Unit": "MeV"
      },
      "tau mass": {
        "Category": "tau",
        "Symbol": "m_tau",
        "Uncertainty": "0.00029e-27",
        "Quantity ": "tau mass",
        "Value": "3.16747e-27",
        "Unit": "kg"
      },
      "atomic unit of electric quadrupole mom ": {
        "Category": "atomic units",
        "Symbol": "AU_electric_quadrupole_mom",
        "Uncertainty": "0.000000028e-40",
        "Quantity ": "atomic unit of electric quadrupole mom.",
        "Value": "4.486551484e-40",
        "Unit": "C m^2"
      },
      "helion mag mom to nuclear magneton ratio": {
        "Category": "helion",
        "Symbol": "mu_h_over_mu_N",
        "Uncertainty": "0.000000025",
        "Quantity ": "helion mag. mom. to nuclear magneton ratio",
        "Value": "-2.127625308",
        "Unit": ""
      },
      "inverse meter-hertz relationship": {
        "Category": "equivalents",
        "Symbol": "inv_m_to_Hz",
        "Uncertainty": "0.0",
        "Quantity ": "inverse meter-hertz relationship",
        "Value": "299792458",
        "Unit": "Hz"
      },
      "electron g factor": {
        "Category": "electron",
        "Symbol": "e_g",
        "Uncertainty": "0.00000000000052",
        "Quantity ": "electron g factor",
        "Value": "-2.00231930436182",
        "Unit": ""
      },
      "alpha particle-proton mass ratio": {
        "Category": "alpha",
        "Symbol": "m_alpha_over_m_P",
        "Uncertainty": "0.00000000036",
        "Quantity ": "alpha particle-proton mass ratio",
        "Value": "3.97259968907",
        "Unit": ""
      },
      "electron mass energy equivalent in mev": {
        "Category": "electron",
        "Symbol": "m_e_c2_in_MeV",
        "Uncertainty": "0.0000000031",
        "Quantity ": "electron mass energy equivalent in MeV",
        "Value": "0.5109989461",
        "Unit": "MeV"
      },
      "atomic unit of electric polarizability": {
        "Category": "atomic units",
        "Symbol": "AU_electric_polarizability",
        "Uncertainty": "0.0000000011e-41",
        "Quantity ": "atomic unit of electric polarizability",
        "Value": "1.6487772731e-41",
        "Unit": "C^2 m^2 J^{-1}"
      },
      "hartree-inverse meter relationship": {
        "Category": "equivalents",
        "Symbol": "Ha_to_inv_m",
        "Uncertainty": "0.000000000013e7",
        "Quantity ": "hartree-inverse meter relationship",
        "Value": "2.194746313702e7",
        "Unit": "m^{-1}"
      },
      "proton rms charge radius": {
        "Category": "proton",
        "Symbol": "r_P",
        "Uncertainty": "0.0061e-15",
        "Quantity ": "proton rms charge radius",
        "Value": "0.8751e-15",
        "Unit": "m"
      },
      "deuteron-proton mag mom ratio": {
        "Category": "deuteron",
        "Symbol": "mu_d_over_m_P",
        "Uncertainty": "0.0000000015",
        "Quantity ": "deuteron-proton mag. mom. ratio",
        "Value": "0.3070122077",
        "Unit": ""
      },
      "first radiation constant for spectral radiance": {
        "Category": "physicochemical",
        "Symbol": "c_1L",
        "Uncertainty": "0.000000015e-16",
        "Quantity ": "first radiation constant for spectral radiance",
        "Value": "1.191042953e-16",
        "Unit": "W m^2 sr^{-1}"
      },
      "triton mass": {
        "Category": "triton",
        "Symbol": "m_t",
        "Uncertainty": "0.000000062e-27",
        "Quantity ": "triton mass",
        "Value": "5.007356665e-27",
        "Unit": "kg"
      },
      "proton charge to mass quotient": {
        "Category": "proton",
        "Symbol": "e_over_m_P",
        "Uncertainty": "0.000000059e7",
        "Quantity ": "proton charge to mass quotient",
        "Value": "9.578833226e7",
        "Unit": "C kg^{-1}"
      },
      "molar volume of ideal gas (273 15 k, 101 325 kpa)": {
        "Category": "physicochemical",
        "Symbol": "V_m_101kPa",
        "Uncertainty": "0.000013e-3",
        "Quantity ": "molar volume of ideal gas (273.15 K, 101.325 kPa)",
        "Value": "22.413962e-3",
        "Unit": "m^3 mol^{-1}"
      },
      "elementary charge over h": {
        "Category": "electromagnetic",
        "Symbol": "e_over_h",
        "Uncertainty": "0.000000015e14",
        "Quantity ": "elementary charge over h",
        "Value": "2.417989262e14",
        "Unit": "A J^{-1}"
      },
      "deuteron mag mom to bohr magneton ratio": {
        "Category": "deuteron",
        "Symbol": "mu_d_over_mu_B",
        "Uncertainty": "0.0000000026e-3",
        "Quantity ": "deuteron mag. mom. to Bohr magneton ratio",
        "Value": "0.4669754554e-3",
        "Unit": ""
      },
      "electron-helion mass ratio": {
        "Category": "electron",
        "Symbol": "m_e_over_m_h",
        "Uncertainty": "0.000000000088e-4",
        "Quantity ": "electron-helion mass ratio",
        "Value": "1.819543074854e-4",
        "Unit": ""
      },
      "triton-proton mass ratio": {
        "Category": "triton",
        "Symbol": "m_t_over_m_P",
        "Uncertainty": "0.00000000022",
        "Quantity ": "triton-proton mass ratio",
        "Value": "2.99371703348",
        "Unit": ""
      },
      "wien frequency displacement law constant": {
        "Category": "physicochemical",
        "Symbol": "b_wein",
        "Uncertainty": "0.0000034e10",
        "Quantity ": "Wien frequency displacement law constant",
        "Value": "5.8789238e10",
        "Unit": "Hz K^{-1}"
      },
      "neutron mag mom to bohr magneton ratio": {
        "Category": "neutron",
        "Symbol": "mu_n_over_mu_B",
        "Uncertainty": "0.00000025e-3",
        "Quantity ": "neutron mag. mom. to Bohr magneton ratio",
        "Value": "-1.04187563e-3",
        "Unit": ""
      },
      "natural unit of mom um in mev/c": {
        "Category": "natural",
        "Symbol": "nu_mom_um_in_MeV_c",
        "Uncertainty": "0.0000000031",
        "Quantity ": "natural unit of mom.um in MeV/c",
        "Value": "0.5109989461",
        "Unit": "MeV/c"
      },
      "electron volt": {
        "Category": "electromagnetic",
        "Symbol": "eV",
        "Uncertainty": "0.0000000098e-19",
        "Quantity ": "electron volt",
        "Value": "1.6021766208e-19",
        "Unit": "J"
      },
      "planck constant over 2 pi in ev s": {
        "Category": "universal",
        "Symbol": "hbar_eV",
        "Uncertainty": "0.000000040e-16",
        "Quantity ": "Planck constant over 2 pi in eV s",
        "Value": "6.582119514e-16",
        "Unit": "eV s"
      },
      "muon g factor": {
        "Category": "muon",
        "Symbol": "g_mu",
        "Uncertainty": "0.0000000013",
        "Quantity ": "muon g factor",
        "Value": "-2.0023318418",
        "Unit": ""
      },
      "atomic unit of charge": {
        "Category": "electromagnetic",
        "Symbol": "e",
        "Uncertainty": "0.0000000098e-19",
        "Quantity ": "atomic unit of charge",
        "Value": "1.6021766208e-19",
        "Unit": "C"
      },
      "atomic unit of mass": {
        "Category": "atomic units",
        "Symbol": "AU_mass",
        "Uncertainty": "0.00000011e-31",
        "Quantity ": "atomic unit of mass",
        "Value": "9.10938356e-31",
        "Unit": "kg"
      },
      "natural unit of energy in mev": {
        "Category": "natural",
        "Symbol": "nu_energy_in_MeV",
        "Uncertainty": "0.0000000031",
        "Quantity ": "natural unit of energy in MeV",
        "Value": "0.5109989461",
        "Unit": "MeV"
      },
      "sackur-tetrode constant (1 k, 100 kpa)": {
        "Category": "physicochemical",
        "Symbol": "S_0_over_R",
        "Uncertainty": "0.0000014",
        "Quantity ": "Sackur-Tetrode constant (1 K, 100 kPa)",
        "Value": "-1.1517084",
        "Unit": ""
      },
      "second radiation constant": {
        "Category": "physicochemical",
        "Symbol": "c_2",
        "Uncertainty": "0.00000083e-2",
        "Quantity ": "second radiation constant",
        "Value": "1.43877736e-2",
        "Unit": "m K"
      },
      "atomic unit of electric field gradient": {
        "Category": "atomic units",
        "Symbol": "AU_electric_field_gradient",
        "Uncertainty": "0.000000060e21",
        "Quantity ": "atomic unit of electric field gradient",
        "Value": "9.717362356e21",
        "Unit": "V m^{-2}"
      },
      "nuclear magneton": {
        "Category": "electromagnetic",
        "Symbol": "mu_N",
        "Uncertainty": "0.000000031e-27",
        "Quantity ": "nuclear magneton",
        "Value": "5.050783699e-27",
        "Unit": "J T^{-1}"
      },
      "kelvin-atomic mass unit relationship": {
        "Category": "equivalents",
        "Symbol": "K_to_AMU",
        "Uncertainty": "0.0000053e-14",
        "Quantity ": "kelvin-atomic mass unit relationship",
        "Value": "9.2510842e-14",
        "Unit": "u"
      },
      "helion mass": {
        "Category": "helion",
        "Symbol": "m_h",
        "Uncertainty": "0.000000062e-27",
        "Quantity ": "helion mass",
        "Value": "5.006412700e-27",
        "Unit": "kg"
      },
      "electron mag mom to bohr magneton ratio": {
        "Category": "electron",
        "Symbol": "mu_e_over_mu_B",
        "Uncertainty": "0.00000000000026",
        "Quantity ": "electron mag. mom. to Bohr magneton ratio",
        "Value": "-1.00115965218091",
        "Unit": ""
      },
      "bohr magneton in inverse meters per tesla": {
        "Category": "electromagnetic",
        "Symbol": "mu_B_over_hc",
        "Uncertainty": "0.00000029",
        "Quantity ": "Bohr magneton in inverse meters per tesla",
        "Value": "46.68644814",
        "Unit": "m^{-1} T^{-1}"
      },
      "hertz-kilogram relationship": {
        "Category": "equivalents",
        "Symbol": "Hz_to_kg",
        "Uncertainty": "0.000000091e-51",
        "Quantity ": "hertz-kilogram relationship",
        "Value": "7.372497201e-51",
        "Unit": "kg"
      },
      "atomic mass unit-hartree relationship": {
        "Category": "equivalents",
        "Symbol": "AMU_to_Ha",
        "Uncertainty": "0.0000000016e7",
        "Quantity ": "atomic mass unit-hartree relationship",
        "Value": "3.4231776902e7",
        "Unit": "E_h"
      },
      "proton-neutron mass ratio": {
        "Category": "proton",
        "Symbol": "m_P_over_m_n",
        "Uncertainty": "0.00000000051",
        "Quantity ": "proton-neutron mass ratio",
        "Value": "0.99862347844",
        "Unit": ""
      },
      "avogadro constant": {
        "Category": "physicochemical",
        "Symbol": "N_A",
        "Uncertainty": "0.000000074e23",
        "Quantity ": "Avogadro constant",
        "Value": "6.022140857e23",
        "Unit": "mol^{-1}"
      },
      "first radiation constant": {
        "Category": "physicochemical",
        "Symbol": "c_1",
        "Uncertainty": "0.000000046e-16",
        "Quantity ": "first radiation constant",
        "Value": "3.741771790e-16",
        "Unit": "W m^2"
      },
      "inverse meter-kilogram relationship": {
        "Category": "equivalents",
        "Symbol": "inv_m_to_kg",
        "Uncertainty": "0.000000027e-42",
        "Quantity ": "inverse meter-kilogram relationship",
        "Value": "2.210219057e-42",
        "Unit": "kg"
      },
      "triton mass energy equivalent in mev": {
        "Category": "triton",
        "Symbol": "m_t_c2_in_MeV",
        "Uncertainty": "0.000017",
        "Quantity ": "triton mass energy equivalent in MeV",
        "Value": "2808.921112",
        "Unit": "MeV"
      },
      "alpha particle mass energy equivalent": {
        "Category": "alpha",
        "Symbol": "m_alpha_c2",
        "Uncertainty": "0.000000073e-10",
        "Quantity ": "alpha particle mass energy equivalent",
        "Value": "5.971920097e-10",
        "Unit": "J"
      },
      "rydberg constant": {
        "Category": "atomic",
        "Symbol": "Rinf",
        "Uncertainty": "0.000065",
        "Quantity ": "Rydberg constant",
        "Value": "10973731.568508",
        "Unit": "m^{-1}"
      },
      "neutron molar mass": {
        "Category": "neutron",
        "Symbol": "M_n",
        "Uncertainty": "0.00000000049e-3",
        "Quantity ": "neutron molar mass",
        "Value": "1.00866491588e-3",
        "Unit": "kg mol^{-1}"
      },
      "proton-neutron mag mom ratio": {
        "Category": "proton",
        "Symbol": "mu_P_over_mu_n",
        "Uncertainty": "0.00000034",
        "Quantity ": "proton-neutron mag. mom. ratio",
        "Value": "-1.45989805",
        "Unit": ""
      },
      "neutron compton wavelength over 2 pi": {
        "Category": "neutron",
        "Symbol": "lambda_C_n_over_2pi",
        "Uncertainty": "0.00000000014e-15",
        "Quantity ": "neutron Compton wavelength over 2 pi",
        "Value": "0.21001941536e-15",
        "Unit": "m"
      },
      "hartree-kelvin relationship": {
        "Category": "equivalents",
        "Symbol": "Ha_to_K",
        "Uncertainty": "0.0000018e5",
        "Quantity ": "hartree-kelvin relationship",
        "Value": "3.1577513e5",
        "Unit": "K"
      },
      "triton mag mom ": {
        "Category": "triton",
        "Symbol": "mu_t",
        "Uncertainty": "0.000000012e-26",
        "Quantity ": "triton mag. mom.",
        "Value": "1.504609503e-26",
        "Unit": "J T^{-1}"
      },
      "sackur-tetrode constant (1 k, 101 325 kpa)": {
        "Category": "physicochemical",
        "Symbol": "S_0_over_R_101kPa",
        "Uncertainty": "0.0000014",
        "Quantity ": "Sackur-Tetrode constant (1 K, 101.325 kPa)",
        "Value": "-1.1648714",
        "Unit": ""
      },
      "hertz-hartree relationship": {
        "Category": "equivalents",
        "Symbol": "Hz_to_Ha",
        "Uncertainty": "0.0000000000090e-16",
        "Quantity ": "hertz-hartree relationship",
        "Value": "1.5198298460088e-16",
        "Unit": "E_h"
      },
      "neutron to shielded proton mag mom ratio": {
        "Category": "neutron",
        "Symbol": "mu_n_over_mu_prime_P",
        "Uncertainty": "0.00000016",
        "Quantity ": "neutron to shielded proton mag. mom. ratio",
        "Value": "-0.68499694",
        "Unit": ""
      },
      "electron volt-kelvin relationship": {
        "Category": "equivalents",
        "Symbol": "eV_to_K",
        "Uncertainty": "0.00000067e4",
        "Quantity ": "electron volt-kelvin relationship",
        "Value": "1.16045221e4",
        "Unit": "K"
      },
      "triton mass in u": {
        "Category": "triton",
        "Symbol": "m_t_in_u",
        "Uncertainty": "0.00000000011",
        "Quantity ": "triton mass in u",
        "Value": "3.01550071632",
        "Unit": "u"
      },
      "tau-muon mass ratio": {
        "Category": "tau",
        "Symbol": "m_tau_over_m_mu",
        "Uncertainty": "0.0015",
        "Quantity ": "tau-muon mass ratio",
        "Value": "16.8167",
        "Unit": ""
      },
      "angstrom star": {
        "Category": "X-ray",
        "Symbol": "W_K_alpha",
        "Uncertainty": "0.00000090e-10",
        "Quantity ": "Angstrom star",
        "Value": "1.00001495e-10",
        "Unit": "m"
      },
      "shielded proton gyromag ratio": {
        "Category": "proton",
        "Symbol": "lambda_prime_P",
        "Uncertainty": "0.000000033e8",
        "Quantity ": "shielded proton gyromag. ratio",
        "Value": "2.675153171e8",
        "Unit": "s^{-1} T^{-1}"
      },
      "atomic unit of current": {
        "Category": "atomic units",
        "Symbol": "AU_current",
        "Uncertainty": "0.000000041e-3",
        "Quantity ": "atomic unit of current",
        "Value": "6.623618183e-3",
        "Unit": "A"
      },
      "nuclear magneton in mhz/t": {
        "Category": "electromagnetic",
        "Symbol": "mu_N_over_k",
        "Uncertainty": "0.000000047",
        "Quantity ": "nuclear magneton in MHz/T",
        "Value": "7.622593285",
        "Unit": "MHz T^{-1}"
      },
      "hartree energy in ev": {
        "Category": "atomic",
        "Symbol": "E_h_eV",
        "Uncertainty": "0.00000017",
        "Quantity ": "Hartree energy in eV",
        "Value": "27.21138602",
        "Unit": "eV"
      },
      "proton molar mass": {
        "Category": "proton",
        "Symbol": "M_P",
        "Uncertainty": "0.000000000091e-3",
        "Quantity ": "proton molar mass",
        "Value": "1.007276466879e-3",
        "Unit": "kg mol^{-1}"
      },
      "electron-tau mass ratio": {
        "Category": "electron",
        "Symbol": "m_e_over_m_tau",
        "Uncertainty": "0.00026e-4",
        "Quantity ": "electron-tau mass ratio",
        "Value": "2.87592e-4",
        "Unit": ""
      },
      "tau-proton mass ratio": {
        "Category": "tau",
        "Symbol": "m_tau_over_m_P",
        "Uncertainty": "0.00017",
        "Quantity ": "tau-proton mass ratio",
        "Value": "1.89372",
        "Unit": ""
      },
      "proton-electron mass ratio": {
        "Category": "proton",
        "Symbol": "m_P_over_m_e",
        "Uncertainty": "0.00000017",
        "Quantity ": "proton-electron mass ratio",
        "Value": "1836.15267389",
        "Unit": ""
      },
      "joule-inverse meter relationship": {
        "Category": "equivalents",
        "Symbol": "J_to_inv_m",
        "Uncertainty": "0.000000062e24",
        "Quantity ": "joule-inverse meter relationship",
        "Value": "5.034116651e24",
        "Unit": "m^{-1}"
      },
      "proton gyromag ratio": {
        "Category": "proton",
        "Symbol": "lambda_P",
        "Uncertainty": "0.000000018e8",
        "Quantity ": "proton gyromag. ratio",
        "Value": "2.675221900e8",
        "Unit": "s^{-1} T^{-1}"
      },
      "tau compton wavelength": {
        "Category": "tau",
        "Symbol": "lambda_C",
        "Uncertainty": "0.000063e-15",
        "Quantity ": "tau Compton wavelength",
        "Value": "0.697787e-15",
        "Unit": "m"
      },
      "proton-tau mass ratio": {
        "Category": "proton",
        "Symbol": "m_P_over_m_tau",
        "Uncertainty": "0.000048",
        "Quantity ": "proton-tau mass ratio",
        "Value": "0.528063",
        "Unit": ""
      },
      "atomic mass constant energy equivalent in mev": {
        "Category": "physicochemical",
        "Symbol": "m_u_c2_in_MeV",
        "Uncertainty": "0.0000057",
        "Quantity ": "atomic mass constant energy equivalent in MeV",
        "Value": "931.4940954",
        "Unit": "MeV"
      },
      "atomic unit of electric dipole mom ": {
        "Category": "atomic units",
        "Symbol": "ea_0",
        "Uncertainty": "0.000000052e-30",
        "Quantity ": "atomic unit of electric dipole mom.",
        "Value": "8.478353552e-30",
        "Unit": "C m"
      },
      "electron-muon mag mom ratio": {
        "Category": "electron",
        "Symbol": "mu_e_over_mu_u",
        "Uncertainty": "0.0000046",
        "Quantity ": "electron-muon mag. mom. ratio",
        "Value": "206.7669880",
        "Unit": ""
      },
      "tau mass energy equivalent": {
        "Category": "tau",
        "Symbol": "m_tau_c2",
        "Uncertainty": "0.00026e-10",
        "Quantity ": "tau mass energy equivalent",
        "Value": "2.84678e-10",
        "Unit": "J"
      },
      "rydberg constant times c in hz": {
        "Category": "atomic",
        "Symbol": "Rinf_Hz",
        "Uncertainty": "0.000000000019e15",
        "Quantity ": "Rydberg constant times c in Hz",
        "Value": "3.289841960355e15",
        "Unit": "Hz"
      },
      "hartree-hertz relationship": {
        "Category": "equivalents",
        "Symbol": "Ha_to_Hz",
        "Uncertainty": "0.000000000039e15",
        "Quantity ": "hartree-hertz relationship",
        "Value": "6.579683920711e15",
        "Unit": "Hz"
      },
      "kilogram-inverse meter relationship": {
        "Category": "equivalents",
        "Symbol": "kg_to_inv_m",
        "Uncertainty": "0.000000056e41",
        "Quantity ": "kilogram-inverse meter relationship",
        "Value": "4.524438411e41",
        "Unit": "m^{-1}"
      },
      "muon-electron mass ratio": {
        "Category": "muon",
        "Symbol": "m_mu_over_m_e",
        "Uncertainty": "0.0000046",
        "Quantity ": "muon-electron mass ratio",
        "Value": "206.7682826",
        "Unit": ""
      },
      "bohr magneton in ev/t": {
        "Category": "electromagnetic",
        "Symbol": "mu_B_eV",
        "Uncertainty": "0.0000000026e-5",
        "Quantity ": "Bohr magneton in eV/T",
        "Value": "5.7883818012e-5",
        "Unit": "eV T^{-1}"
      },
      "planck time": {
        "Category": "universal",
        "Symbol": "tP",
        "Uncertainty": "0.00013e-44",
        "Quantity ": "Planck time",
        "Value": "5.39116e-44",
        "Unit": "s"
      },
      "molar planck constant": {
        "Category": "universal",
        "Symbol": "h_N",
        "Uncertainty": "0.0000000018e-10",
        "Quantity ": "molar Planck constant",
        "Value": "3.9903127110e-10",
        "Unit": "J s mol^{-1}"
      },
      "triton mag mom to bohr magneton ratio": {
        "Category": "triton",
        "Symbol": "mu_t_over_mu_B",
        "Uncertainty": "0.0000000076e-3",
        "Quantity ": "triton mag. mom. to Bohr magneton ratio",
        "Value": "1.6223936616e-3",
        "Unit": ""
      },
      "electron to shielded helion mag mom ratio": {
        "Category": "electron",
        "Symbol": "mu_e_over_mu_prime_h",
        "Uncertainty": "0.000010",
        "Quantity ": "electron to shielded helion mag. mom. ratio",
        "Value": "864.058257",
        "Unit": ""
      },
      "electron volt-inverse meter relationship": {
        "Category": "equivalents",
        "Symbol": "eV_to_inv_m",
        "Uncertainty": "0.000000050e5",
        "Quantity ": "electron volt-inverse meter relationship",
        "Value": "8.065544005e5",
        "Unit": "m^{-1}"
      },
      "proton mass": {
        "Category": "proton",
        "Symbol": "m_P",
        "Uncertainty": "0.000000021e-27",
        "Quantity ": "proton mass",
        "Value": "1.672621898e-27",
        "Unit": "kg"
      },
      "triton g factor": {
        "Category": "triton",
        "Symbol": "g_t",
        "Uncertainty": "0.000000028",
        "Quantity ": "triton g factor",
        "Value": "5.957924920",
        "Unit": ""
      },
      "molar mass constant": {
        "Category": "equivalents",
        "Symbol": "M_u",
        "Uncertainty": "0.0",
        "Quantity ": "molar mass constant",
        "Value": "1e-3",
        "Unit": "kg mol^{-1}"
      },
      "muon-neutron mass ratio": {
        "Category": "muon",
        "Symbol": "m_mu_over_m_n",
        "Uncertainty": "0.0000000025",
        "Quantity ": "muon-neutron mass ratio",
        "Value": "0.1124545167",
        "Unit": ""
      },
      "neutron mass in u": {
        "Category": "neutron",
        "Symbol": "m_n_in_u",
        "Uncertainty": "0.00000000049",
        "Quantity ": "neutron mass in u",
        "Value": "1.00866491588",
        "Unit": "u"
      },
      "tau mass energy equivalent in mev": {
        "Category": "tau",
        "Symbol": "m_tau_c2_in_MeV",
        "Uncertainty": "0.16",
        "Quantity ": "tau mass energy equivalent in MeV",
        "Value": "1776.82",
        "Unit": "MeV"
      },
      "mag constant": {
        "Category": "universal",
        "Symbol": "epsilon_0",
        "Uncertainty": "0.0",
        "Quantity ": "mag. constant",
        "Value": "12.566370614e-7",
        "Unit": "N A^{-2}"
      },
      "atomic mass unit-kilogram relationship": {
        "Category": "equivalents",
        "Symbol": "AMU_to_kg",
        "Uncertainty": "0.000000020e-27",
        "Quantity ": "atomic mass unit-kilogram relationship",
        "Value": "1.660539040e-27",
        "Unit": "kg"
      },
      "neutron mag mom to nuclear magneton ratio": {
        "Category": "neutron",
        "Symbol": "mu_n_over_mu_N",
        "Uncertainty": "0.00000045",
        "Quantity ": "neutron mag. mom. to nuclear magneton ratio",
        "Value": "-1.91304273",
        "Unit": ""
      },
      "nuclear magneton in k/t": {
        "Category": "electromagnetic",
        "Symbol": "mu_N_over_hc",
        "Uncertainty": "0.0000021e-4",
        "Quantity ": "nuclear magneton in K/T",
        "Value": "3.6582690e-4",
        "Unit": "K T^{-1}"
      },
      "natural unit of action in ev s": {
        "Category": "natural",
        "Symbol": "nu_action_in_eV_s",
        "Uncertainty": "0.000000040e-16",
        "Quantity ": "natural unit of action in eV s",
        "Value": "6.582119514e-16",
        "Unit": "eV s"
      },
      "atomic unit of action": {
        "Category": "atomic units",
        "Symbol": "hbar",
        "Uncertainty": "0.000000013e-34",
        "Quantity ": "atomic unit of action",
        "Value": "1.054571800e-34",
        "Unit": "J s"
      },
      "planck constant over 2 pi times c in mev fm": {
        "Category": "universal",
        "Symbol": "hbar_c",
        "Uncertainty": "0.0000012",
        "Quantity ": "Planck constant over 2 pi times c in MeV fm",
        "Value": "197.3269788",
        "Unit": "MeV fm"
      },
      "atomic unit of 2nd hyperpolarizability": {
        "Category": "atomic units",
        "Symbol": "AU_2nd_hyperpolarizability",
        "Uncertainty": "0.000000077e-65",
        "Quantity ": "atomic unit of 2nd hyperpolarizability",
        "Value": "6.235380085e-65",
        "Unit": "C^4 m^4 J^{-3}"
      },
      "deuteron g factor": {
        "Category": "deuteron",
        "Symbol": "g_d",
        "Uncertainty": "0.0000000048",
        "Quantity ": "deuteron g factor",
        "Value": "0.8574382311",
        "Unit": ""
      },
      "muon molar mass": {
        "Category": "muon",
        "Symbol": "M_mu",
        "Uncertainty": "0.0000000025e-3",
        "Quantity ": "muon molar mass",
        "Value": "0.1134289257e-3",
        "Unit": "kg mol^{-1}"
      },
      "boltzmann constant": {
        "Category": "physicochemical",
        "Symbol": "k_B",
        "Uncertainty": "0.00000079e-23",
        "Quantity ": "Boltzmann constant",
        "Value": "1.38064852e-23",
        "Unit": "J K^{-1}"
      },
      "kelvin-kilogram relationship": {
        "Category": "equivalents",
        "Symbol": "K_to_kg",
        "Uncertainty": "0.00000088e-40",
        "Quantity ": "kelvin-kilogram relationship",
        "Value": "1.53617865e-40",
        "Unit": "kg"
      },
      "bohr magneton in hz/t": {
        "Category": "electromagnetic",
        "Symbol": "mu_B_over_h",
        "Uncertainty": "0.000000086e9",
        "Quantity ": "Bohr magneton in Hz/T",
        "Value": "13.996245042e9",
        "Unit": "Hz T^{-1}"
      },
      "electron molar mass": {
        "Category": "electron",
        "Symbol": "M_e",
        "Uncertainty": "0.00000000016e-7",
        "Quantity ": "electron molar mass",
        "Value": "5.48579909070e-7",
        "Unit": "kg mol^{-1}"
      },
      "neutron-tau mass ratio": {
        "Category": "neutron",
        "Symbol": "m_n_over_m_tau",
        "Uncertainty": "0.000048",
        "Quantity ": "neutron-tau mass ratio",
        "Value": "0.528790",
        "Unit": ""
      },
      "muon mag mom to nuclear magneton ratio": {
        "Category": "muon",
        "Symbol": "mu_mu_over_mu_N",
        "Uncertainty": "0.00000020",
        "Quantity ": "muon mag. mom. to nuclear magneton ratio",
        "Value": "-8.89059705",
        "Unit": ""
      },
      "hartree-atomic mass unit relationship": {
        "Category": "equivalents",
        "Symbol": "Ha_to_AMU",
        "Uncertainty": "0.0000000013e-8",
        "Quantity ": "hartree-atomic mass unit relationship",
        "Value": "2.9212623197e-8",
        "Unit": "u"
      },
      "planck temperature": {
        "Category": "universal",
        "Symbol": "T_P",
        "Uncertainty": "0.000033e32",
        "Quantity ": "Planck temperature",
        "Value": "1.416808e32",
        "Unit": "K"
      },
      "neutron mass": {
        "Category": "neutron",
        "Symbol": "m_n",
        "Uncertainty": "0.000000021e-27",
        "Quantity ": "neutron mass",
        "Value": "1.674927471e-27",
        "Unit": "kg"
      },
      "kelvin-hertz relationship": {
        "Category": "equivalents",
        "Symbol": "K_to_Hz",
        "Uncertainty": "0.0000012e10",
        "Quantity ": "kelvin-hertz relationship",
        "Value": "2.0836612e10",
        "Unit": "Hz"
      },
      "neutron mass energy equivalent": {
        "Category": "neutron",
        "Symbol": "m_n_c2",
        "Uncertainty": "0.000000019e-10",
        "Quantity ": "neutron mass energy equivalent",
        "Value": "1.505349739e-10",
        "Unit": "J"
      },
      "molar planck constant times c": {
        "Category": "universal",
        "Symbol": "h_N_c",
        "Uncertainty": "0.000000000054",
        "Quantity ": "molar Planck constant times c",
        "Value": "0.119626565582",
        "Unit": "J m mol^{-1}"
      },
      "proton-muon mass ratio": {
        "Category": "proton",
        "Symbol": "m_P_over_m_mu",
        "Uncertainty": "0.00000020",
        "Quantity ": "proton-muon mass ratio",
        "Value": "8.88024338",
        "Unit": ""
      },
      "electron mass": {
        "Category": "electron",
        "Symbol": "m_e",
        "Uncertainty": "0.00000011e-31",
        "Quantity ": "electron mass",
        "Value": "9.10938356e-31",
        "Unit": "kg"
      },
      "inverse meter-kelvin relationship": {
        "Category": "equivalents",
        "Symbol": "inv_m_to_K",
        "Uncertainty": "0.00000083e-2",
        "Quantity ": "inverse meter-kelvin relationship",
        "Value": "1.43877736e-2",
        "Unit": "K"
      },
      "proton compton wavelength": {
        "Category": "proton",
        "Symbol": "lambda_C_P",
        "Uncertainty": "0.00000000061e-15",
        "Quantity ": "proton Compton wavelength",
        "Value": "1.32140985396e-15",
        "Unit": "m"
      },
      "natural unit of mom um": {
        "Category": "natural",
        "Symbol": "nu_mom_um",
        "Uncertainty": "0.000000034e-22",
        "Quantity ": "natural unit of mom.um",
        "Value": "2.730924488e-22",
        "Unit": "kg m s^{-1}"
      },
      "nuclear magneton in ev/t": {
        "Category": "electromagnetic",
        "Symbol": "mu_N_eV",
        "Uncertainty": "0.0000000015e-8",
        "Quantity ": "nuclear magneton in eV/T",
        "Value": "3.1524512550e-8",
        "Unit": "eV T^{-1}"
      },
      "inverse meter-electron volt relationship": {
        "Category": "equivalents",
        "Symbol": "inv_m_to_eV",
        "Uncertainty": "0.0000000076e-6",
        "Quantity ": "inverse meter-electron volt relationship",
        "Value": "1.2398419739e-6",
        "Unit": "eV"
      },
      "molar volume of ideal gas (273 15 k, 100 kpa)": {
        "Category": "physicochemical",
        "Symbol": "V_m",
        "Uncertainty": "0.000013e-3",
        "Quantity ": "molar volume of ideal gas (273.15 K, 100 kPa)",
        "Value": "22.710947e-3",
        "Unit": "m^3 mol^{-1}"
      },
      "joule-kelvin relationship": {
        "Category": "equivalents",
        "Symbol": "J_to_K",
        "Uncertainty": "0.0000042e22",
        "Quantity ": "joule-kelvin relationship",
        "Value": "7.2429731e22",
        "Unit": "K"
      },
      "boltzmann constant in hz/k": {
        "Category": "physicochemical",
        "Symbol": "k_B_over_h",
        "Uncertainty": "0.0000012e10",
        "Quantity ": "Boltzmann constant in Hz/K",
        "Value": "2.0836612e10",
        "Unit": "Hz K^{-1}"
      },
      "shielded helion to proton mag mom ratio": {
        "Category": "helion",
        "Symbol": "mu_prime_h_over_mu_p",
        "Uncertainty": "0.0000000092",
        "Quantity ": "shielded helion to proton mag. mom. ratio",
        "Value": "-0.7617665603",
        "Unit": ""
      },
      "nuclear magneton in inverse meters per tesla": {
        "Category": "electromagnetic",
        "Symbol": "mu_N_over_h",
        "Uncertainty": "0.000000016e-2",
        "Quantity ": "nuclear magneton in inverse meters per tesla",
        "Value": "2.542623432e-2",
        "Unit": "m^{-1} T^{-1}"
      },
      "atomic unit of charge density": {
        "Category": "atomic units",
        "Symbol": "e_over_a_0_3",
        "Uncertainty": "0.0000000067e12",
        "Quantity ": "atomic unit of charge density",
        "Value": "1.0812023770e12",
        "Unit": "C m^{-3}"
      },
      "atomic unit of electric potential": {
        "Category": "atomic units",
        "Symbol": "AU_electric_potential",
        "Uncertainty": "0.00000017",
        "Quantity ": "atomic unit of electric potential",
        "Value": "27.21138602",
        "Unit": "V"
      },
      "molar mass of carbon-12": {
        "Category": "equivalents",
        "Symbol": "M(12_C)",
        "Uncertainty": "0.0",
        "Quantity ": "molar mass of carbon-12",
        "Value": "12e-3",
        "Unit": "kg mol^{-1}"
      },
      "neutron-proton mass ratio": {
        "Category": "neutron",
        "Symbol": "m_n_over_m_P",
        "Uncertainty": "0.00000000051",
        "Quantity ": "neutron-proton mass ratio",
        "Value": "1.00137841898",
        "Unit": ""
      },
      "electron gyromag ratio": {
        "Category": "electron",
        "Symbol": "gamma_e",
        "Uncertainty": "0.000000011e11",
        "Quantity ": "electron gyromag. ratio",
        "Value": "1.760859644e11",
        "Unit": "s^{-1} T^{-1}"
      },
      "alpha particle mass in u": {
        "Category": "alpha",
        "Symbol": "m_alpha_u",
        "Uncertainty": "0.000000000063",
        "Quantity ": "alpha particle mass in u",
        "Value": "4.001506179127",
        "Unit": "u"
      },
      "alpha particle mass energy equivalent in mev": {
        "Category": "alpha",
        "Symbol": "m_alpha_c2_MeV",
        "Uncertainty": "0.000023",
        "Quantity ": "alpha particle mass energy equivalent in MeV",
        "Value": "3727.379378",
        "Unit": "MeV"
      },
      "muon compton wavelength over 2 pi": {
        "Category": "muon",
        "Symbol": "lambda_C_over_2pi",
        "Uncertainty": "0.000000042e-15",
        "Quantity ": "muon Compton wavelength over 2 pi",
        "Value": "1.867594308e-15",
        "Unit": "m"
      },
      "loschmidt constant (273 15 k, 101 325 kpa)": {
        "Category": "physicochemical",
        "Symbol": "n_0_101kPa",
        "Uncertainty": "0.0000015e25",
        "Quantity ": "Loschmidt constant (273.15 K, 101.325 kPa)",
        "Value": "2.6867811e25",
        "Unit": "m^{-3}"
      },
      "planck constant": {
        "Category": "universal",
        "Symbol": "h",
        "Uncertainty": "0.000000081e-34",
        "Quantity ": "Planck constant",
        "Value": "6.626070040e-34",
        "Unit": "J s"
      },
      "hartree energy": {
        "Category": "atomic",
        "Symbol": "E_h",
        "Uncertainty": "0.000000054e-18",
        "Quantity ": "Hartree energy",
        "Value": "4.359744650e-18",
        "Unit": "J"
      },
      "atomic unit of energy": {
        "Category": "atomic units",
        "Symbol": "AU_energy",
        "Uncertainty": "0.000000054e-18",
        "Quantity ": "atomic unit of energy",
        "Value": "4.359744650e-18",
        "Unit": "J"
      },
      "tau-electron mass ratio": {
        "Category": "tau",
        "Symbol": "m_tau_over_m_e",
        "Uncertainty": "0.31",
        "Quantity ": "tau-electron mass ratio",
        "Value": "3477.15",
        "Unit": ""
      },
      "atomic mass unit-electron volt relationship": {
        "Category": "equivalents",
        "Symbol": "AMU_to_eV",
        "Uncertainty": "0.0000057e6",
        "Quantity ": "atomic mass unit-electron volt relationship",
        "Value": "931.4940954e6",
        "Unit": "eV"
      }
    }



# cache for convenience
_categories_ = []
_phys_const_keys_ = []


#_______________________________________________________
def _strip_name (name=''):
    ''' cvt to lower case, remove periods, double spaces'''
    name = name.lower().replace('.',' ')
    name = name.replace('  ',' ')
    return name


#_______________________________________________________

def _build_CODATA_dict (codata_file, symbol_file):
    """
        CODATA JSON elements are like dictionary entries
        without an external key.

        {
          "Quantity ": "Planck constant",
          "Value": "6.626 070 040 e-34",
          "Uncertainty": "0.000 000 081 e-34",
          "Unit": "J s"
        },

    """

    global _phys_const_          # = {}
    global _categories_          # = []
    global _phys_const_keys_     # = []

    # if dictionary is already instantiated,
    #   gather categories and keys

    if len(_phys_const_) > 1:
        _phys_const_keys_ = _phys_const_.keys()
        for k in _phys_const_keys_:
            if _phys_const_[k]['Category'] not in _categories_:
                _categories_.append(_phys_const_[k]['Category'])

    # ELSE Build the CODATA dictionary from scratch
    else:

        jdict = {}
        with open(codata_file,'ra') as codatafp :
            jdict = json.load(codatafp)
        codatafp.close()

        ''' The CODATA JSON file is a dictionary with one key
            that references a list of dictionary entries:
            {'constants' : [{},{},...] }
        '''

        # extract the list from the JSON dictionary
        codata_list = []
        codata_list = jdict[jdict.keys()[0]]

        for i in range(len(codata_list)):
            # get one constant dictionary and extract the constant name
            member = codata_list[i]

            # note 'Quantity ' key has trailing space
            # retain the Quantity field but
            # use lower case form as key for case-insensitive searching.

            # name = member.pop('Quantity ', None)

            name = _strip_name (member['Quantity '])

            # reformat numeric strings
            numerics = member['Value'].replace(' ', '').replace('...', '')
            member['Value'] = numerics

            numerics = member['Uncertainty'].replace(' ', '').replace('(exact)', '0.0')
            member['Uncertainty'] = numerics
            #add placeholder keys
            member['Category'] = ''
            member['Symbol'] = ''

            _phys_const_[name] = member

        """
            Note the trailing space in the 'Quantity ' key.
            Dictionary object now has a key and usably formatted
            numeric fields.

            "planck constant" : {
              "Category": "",
              "Quantity ": "Planck constant",
              "Symbol": "",
              "Value": "6.626070040e-34",
              "Uncertainty": "0.000000081e-34",
              "Unit": "J s"
            },
        """



        '''
         read in symbol & category addenda.
         Update constant defs accordingly.

         symbol JSON items look like:

            {
              "Quantity ": "Planck constant",
              "Category": "universal",
              "Symbol": "h"
            },

         This updates the existing CODATA entry to:

          "planck constant": {
            "Category": "universal",
            "Symbol": "h",
            "Uncertainty": "0.000000081e-34",
            "Quantity ": "Planck constant",
            "Value": "6.626070040e-34",
            "Unit": "J s"
          },

         Build a category list in the process.
        '''

        with open(symbol_file,'ra') as symfp:
            symdict = json.load(symfp)

            symlist = []
            symlist = symdict[symdict.keys()[0]]

            for i in range(len(symlist)):
                symdict = symlist[i]

                # remove constant name from dictionary for immediate use
                name = _strip_name(symdict['Quantity '])

                if name in _phys_const_.keys():
                    _phys_const_[name].update(symdict)

                    # build the category list for later
                    if symdict['Category'] not in _categories_:
                        _categories_.append(symdict['Category'])

        symfp.close()

    # addenda

    _phys_const_['joule-calorie relationship'] = {
          'Quantity ': 'Joule-calorie relationship',
          'Value': '4.184',
          'Uncertainty': '0.0',
          'Unit': 'J/cal',
          'Category': 'equivalents',
          'Symbol': 'J_to_cal'
        }

    calPerJoule = ('%1.16e' % (1.0/4.184))

    _phys_const_['calorie-joule relationship'] = {
          'Quantity ': 'calorie-Joule relationship',
          'Value': calPerJoule,
          'Uncertainty': '0.0',
          'Unit': 'cal/J',
          'Category': 'equivalents',
          'Symbol': 'cal_to_J'
        }

    _phys_const_keys_ = _phys_const_.keys()

    #return _phys_const_

#_______________________________________________________

def __init__():
    """pyLint"""

    #________________________________________________
    def _fileExists (fname):
        """Test file existence"""
        if os.path.exists(fname):
            return True
        else:
            print(("Error: " + fname + " not found"))
            return False
    #________________________________________________

    if len(_phys_const_) < 330:

        if not _fileExists(_codata2014_file_):
            return False

        if not _fileExists(_symbol_file):
            return False

    # convert CODATA JSON input file to python dictionary

    _build_CODATA_dict(_codata2014_file_,_symbol_file)

#_______________________________________________________
def Citation():
    '''Unambiguous statement of source'''
    return _citation_

#_______________________________________________________

def Dictionary ():
    ''' return the ENTIRE pythonic CODATA dictionary '''
    return _phys_const_

#_______________________________________________________

def Value(constantname=''):
    '''
    return value as numerical ASCII and leave
    binary translation to the application language.
    '''
    key = _strip_name (constantname)

    if key in _phys_const_.keys():
        return _phys_const_[key]['Value']
    else:
        return '0.0'

#_______________________________________________________

def Uncertainty(constantname=''):
    ''' return absolute uncertainty as numerical ASCII string '''

    key = _strip_name (constantname)
    if key in _phys_const_.keys():
        return _phys_const_[key]['Uncertainty']

    else:
        return '0.0'

#_______________________________________________________

def Units(constantname=''):
    '''
    Return units of constant.
    Dimensionless constants are denoted by a null string ''
    '''

    key = _strip_name (constantname)
    if key in _phys_const_.keys():
        return _phys_const_[key]['Unit']
    else:
        return ''

#_______________________________________________________

def Properties(constantname=''):
    '''
    return the single dictionary entry for a constant

    constantname = 'planck constant' returns:

    { "Quantity ": "Planck constant",
      "Category": "universal",
      "Symbol": "h"
      "Uncertainty": "0.000000081e-34",
      "Unit": "J s"
      "Value": "6.626070040e-34",
    }

    '''

    key = _strip_name (constantname)
    if key in _phys_const_.keys():
        return _phys_const_[key]
    else:
        return {}

#_______________________________________________________

def Symbol (constantname=''):

    key = _strip_name (constantname)
    if key in _phys_const_.keys():
        return _phys_const_[key]['Symbol']
    else:
        return ''

#_______________________________________________________

def Categories():
    ''' return list of all constant categories '''
    return _categories_

#_______________________________________________________

def Names():
    ''' return list of all constant names '''
    return _phys_const_keys_

#_______________________________________________________

def Constants(category=''):
    '''
    Return a dictionary of constants within a category,
    e.g., all 'universal' constants or 'physicochemical' ones
    '''

    if  category == '' or \
        category not in _categories_ or \
        category is None:

        return {}

    _keys = Names()

    catdict = {}

    for k in _keys:
        if _phys_const_[k]['Category'] == category:
            catdict[k] = _phys_const_[k]

        #prop = _phys_const_[k]
        #if prop['Category'] == category:
        #    catdict[k] = prop

    return catdict

#_______________________________________________________


def WriteJSON (cdict={},outfile=''):

    if len(cdict) < 1 or outfile == '':
        return

    with open(outfile,'wa') as ofp:
        json.dump(cdict,ofp, indent=2)
        ofp.write('\n')

    ofp.close()

#_______________________________________________________

def WriteCSV (cdict={},outfile=''):

    if len(cdict) < 1 or outfile == '':
        return

    constants = sorted(cdict.keys())
    fields = sorted(cdict[constants[0]].keys())
    fields.reverse()

    ''' CSV header format:
       "Quantity ","Value","Unit","Uncertainty","Symbol","Category"
    '''
    csv_header = '\"Quantity \",' + \
                ','.join([('\"%s\"' % f) for f in fields]) + '\n'

    ''' row format is:
    "Planck constant","6.626070040e-34","J s","0.000000081e-34","h","universal"
    '''

    with open(outfile,'wa') as ofp:
        ofp.write(csv_header)

        for name in constants:
            const = cdict[name]
            row = ('\"%s\",' % name) + \
                    ','.join([('\"%s\"' % const[f]) for f in fields]) + \
                    '\n'

            ofp.write(row)
    # done
    ofp.close()

#_______________________________________________________

# Explicitly initialize since module isn't a class yet


__init__()


#_______________________________________________________

#
# Low-rent unit testing follows.

def _test_codata():

    print('\n#### BEGIN %s test\n' % __file__.upper())
    print('CITATION:')
    print(Citation())

    # scan property dictionaries for oddness
    cdict  = Dictionary()
    keys = cdict.keys()
    len_names = len(Names())
    len_dict = len(cdict)
    len_keys = len(keys)

    print('CODATA dictionary has %d members' % len_dict)
    print("NOTE: entries: %d  keys: %d" %(len_dict, len_keys))
    print("NOTE: names() list len %d" %(len_names))

    dict_err = 0
    for name in keys:
        mem = cdict[name]
        if len(mem) == 0:
            print('%s property dict is empty' % name)

        elif len(mem)!=6:
            print('%s property dict has len %d, should be 5' % (name,len(mem)))
            dict_err+=1
        else:
            fields = ['Quantity ','Value','Category','Uncertainty','Symbol']
            for fld in fields:
                try:
                    if mem[fld] == '':
                        print('%s \'%s\' field is empty' % (name,fld))
                        dict_err+=1
                except:
                    print('%s has no %s field' % (name,fld))
                    dict_err+=1

    print('%d structural errors in dictionary\n' % dict_err)

    print('testing property retrieval for Planck constant...')

    constantname = 'Planck constant'
    value        = Value(constantname)
    uncertainty  = Uncertainty(constantname)
    unit         = Units(constantname)
    symbol       = Symbol(constantname)

    p = Properties(constantname)
    print(p)
    if value != p['Value']:
        print('bad value, got %s, not %s' %(value,p['Value']))
    if uncertainty != p['Uncertainty']:
        print('bad uncertainty')
    if unit != p['Unit']:
        print('bad unit')
    if symbol != p['Symbol']:
        print('bad symbol')
    print('...Done.\n')

    # fetch categories list
    catlist = Categories()
    catlistlen = len(catlist)
    print('%d CATEGORIES: %s\n' %
        (catlistlen,', '.join([c for c in catlist])))

    # tally category sizes, compare to dictionary size
    cat_total = 0
    print('%-16s: SIZE' % 'CATEGORY')
    for cat in catlist:
        catlen = len(Constants(cat))
        print('%-16s: %d' % (cat,catlen))
        cat_total += catlen
    print('\ncategory total: %d, dictionary size: %d' % (cat_total, len_dict))

    #WriteJSON (cdict={},outfile='')
    #WriteCSV (cdict={},outfile='')

    print('\n#### END %s test\n' % __file__.upper())

    return

#________________________________________

if __name__ == "__main__":

    _test_codata()
    sys.exit(0)

