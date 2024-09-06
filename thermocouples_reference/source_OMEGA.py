"""    
    This module uses thermocouple reference functions for types C,D,G.

    You can access the lookup table objects like so:
        typeC = <this module>.thermocouples['C']

    Thermocouple reference functions are polynomials taken from
        "Tungsten-Rhenium Thermocouples Calibration Equivalents"
        http://www.omega.com/temperature/z/pdf/z202.pdf

    Note on calibration:
        Curves C, G are almost certainly calibrations to IPTS-68,
        as suggested by the source PDF.
        Observe that we can compare the type G curve here to
        the type G from ASTM functions:
            from pylab import *
            from thermocouples_reference import *
            G90 = source_ASTM.thermocouples['G']
            T90 = linspace(0,2310,1001)
            G68 = source_OMEGA.thermocouples['G']
            T68 = [G68.inverse_CmV(e) for e in G90.emf_mVC(T90)]
            figure() ; plot(T90+273.15,T90-T68)
            xlim(0,4000) ; ylim(-2.5,0.5)
            xlabel('$T_{90}$ (K)')
            ylabel('$T_{90} - T_{68}$ (K)')
            show()
        The resulting graph appears very similar to the published
        ITS-90 vs. IPTS-68 difference, see 
        http://www.bipm.org/en/publications/mep_kelvin/its-90_supplementary.html
           Figure 5 of Introduction
        
        The difference between IPTS-68 and ITS-90 scales is at worst
        0.4 deg C over the range 0 to 1400 deg C;
        At 1500 deg C, IPTS-68 reads 0.44 deg C higher
        At 2000 deg C, IPTS-68 reads 0.72 deg C higher
        At 2500 deg C, IPTS-68 reads 1.07 deg C higher
        Anyway at the manufacturing variations in WRe thermocouples
        are somewhere around +/-4 to +/-20 deg C.
        
        Curve D is also very probably IPTS68.

    Disclaimers:
    (Author) I make no warranties as to the accuracy of this module, and shall
           not be liable for any damage that may result from errors or omissions.

    (Note: This module is generated code from create_tables_CDG.py.)
"""

__copyright__ = "public domain"

import numpy as np
from .function_types import Thermocouple_Reference, Polynomial_Gaussian_Piecewise_Function

_source = 'OMEGA Inc. z202.pdf'
_cal = 'IPTS-68'

thermocouples = {
# The coefficients of this polynomial have been converted from
# a Fahrenheit polynomial with 7 significant figures, and have
# been stored here with longer precision to avoid further inaccuracy.
'G':Thermocouple_Reference(Polynomial_Gaussian_Piecewise_Function(
    [[0.,2315.,
np.array([ -2.2222283359680003e-16,   2.2112702944358399e-12,
        -1.0316119658501839e-08,   2.1425207201941232e-05,
         1.2905824431600024e-03,   0.0000000000000000e+00]),
    None]],'C','mV', calibration=_cal, source=_source+', type G'),
    ttype='Type G',
    composition='W - 74W,26Re'),

# The coefficients of this polynomial have been converted from
# a Fahrenheit polynomial with 7 significant figures, and have
# been stored here with longer precision to avoid further inaccuracy.
'C':Thermocouple_Reference(Polynomial_Gaussian_Piecewise_Function(
    [[0.,2315.,
np.array([ -4.9446064258560002e-16,   3.6006582486412798e-12,
        -1.0489145155399067e-08,   1.2252598548103214e-05,
         1.3387722982319094e-02,   0.0000000000000000e+00]),
    None]],'C','mV', calibration=_cal, source=_source+', type C'),
    ttype='Type C',
    composition='95W,5Re - 74W,26Re'),

'D':Thermocouple_Reference(Polynomial_Gaussian_Piecewise_Function(
    [[0.,783., np.array([
        -1.4240735e-15,
         7.9498033e-12,
        -1.8464573e-8,
         2.0592621e-5,
         9.5685256e-3,
         0.,
    ]), None],
    [783.,2320., np.array([
        -7.9026726e-16,
         5.3743821e-12,
        -1.4935266e-8,
         1.8666488e-5,
         9.9109462e-3,
         0.,
    ]), None],
    ],'C','mV', calibration=_cal, source=_source+', type D'),
    ttype='Type D',
    composition='97W,3Re - 75W,25Re'),
}

del _source
del _cal

#end of module

