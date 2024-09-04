"""
    This module contains thermocouple reference functions for types
    B,E,J,K,N,R,S,T.

    You can access the lookup table objects like so:
        typeK = <this module>.thermocouples['K']

    This module contains the NIST ITS-90 thermocouple reference functions.

    Disclaimers:
    (Author) I make no warranties as to the accuracy of this module, and shall
           not be liable for any damage that may result from errors or omissions.
    (NIST) The National Institute of Standards and Technology (NIST) uses its
           best efforts to produce a Database of high quality and to verify that
           the data contained therein have been selected on the basis of sound
           scientific judgement. However, NIST makes no warranties to that effect,
           and NIST shall not be liable for any damage that may result from errors
           or omissions in the Database.

    (Note: This module is generated code from create_tables_NIST.py.)
"""

__copyright__ = "public domain"

import numpy as np
from .function_types import Thermocouple_Reference, Polynomial_Gaussian_Piecewise_Function

thermocouples = {

'B': Thermocouple_Reference(Polynomial_Gaussian_Piecewise_Function([
  [0.000, 630.615, np.array([
         0.629903470940e-18,
        -0.169445292400e-14,
         0.156682919010e-11,
        -0.132579316360e-08,
         0.590404211710e-05,
        -0.246508183460e-03,
         0.000000000000e+00,
  ]), None],
  [630.615, 1820.000, np.array([
        -0.937913302890e-24,
         0.989756408210e-20,
        -0.445154310330e-16,
         0.111097940130e-12,
        -0.168353448640e-09,
         0.157852801640e-06,
        -0.848851047850e-04,
         0.285717474700e-01,
        -0.389381686210e+01,
  ]), None],
  ],'C','mV',
       calibration='ITS-90',
       source='NIST SRD 60, type B'),
     ttype='Type B',
     composition='70Pt,30Rh - 94Pt,6Rh'),

'E': Thermocouple_Reference(Polynomial_Gaussian_Piecewise_Function([
  [-270.000, 0.000, np.array([
        -0.346578420130e-28,
        -0.558273287210e-25,
        -0.396736195160e-22,
        -0.164147763550e-19,
        -0.439794973910e-17,
        -0.803701236210e-15,
        -0.102876055340e-12,
        -0.932140586670e-11,
        -0.594525830570e-09,
        -0.258001608430e-07,
        -0.779980486860e-06,
         0.454109771240e-04,
         0.586655087080e-01,
         0.000000000000e+00,
  ]), None],
  [0.000, 1000.000, np.array([
         0.359608994810e-27,
        -0.143880417820e-23,
         0.214892175690e-20,
        -0.125366004970e-17,
        -0.191974955040e-15,
         0.650244032700e-12,
        -0.330568966520e-09,
         0.289084072120e-07,
         0.450322755820e-04,
         0.586655087100e-01,
         0.000000000000e+00,
  ]), None],
  ],'C','mV',
       calibration='ITS-90',
       source='NIST SRD 60, type E'),
     ttype='Type E',
     composition='90Ni,10Cr - 55Cu,45Ni'),

'J': Thermocouple_Reference(Polynomial_Gaussian_Piecewise_Function([
  [-210.000, 760.000, np.array([
         0.156317256970e-22,
        -0.125383953360e-18,
         0.209480906970e-15,
        -0.170529583370e-12,
         0.132281952950e-09,
        -0.856810657200e-07,
         0.304758369300e-04,
         0.503811878150e-01,
         0.000000000000e+00,
  ]), None],
  [760.000, 1200.000, np.array([
        -0.306913690560e-12,
         0.157208190040e-08,
        -0.318476867010e-05,
         0.317871039240e-02,
        -0.149761277860e+01,
         0.296456256810e+03,
  ]), None],
  ],'C','mV',
       calibration='ITS-90',
       source='NIST SRD 60, type J'),
     ttype='Type J',
     composition='Fe - 55Cu,45Ni'),

'K': Thermocouple_Reference(Polynomial_Gaussian_Piecewise_Function([
  [-270.000, 0.000, np.array([
        -0.163226974860e-22,
        -0.198892668780e-19,
        -0.104516093650e-16,
        -0.310888728940e-14,
        -0.574103274280e-12,
        -0.675090591730e-10,
        -0.499048287770e-08,
        -0.328589067840e-06,
         0.236223735980e-04,
         0.394501280250e-01,
         0.000000000000e+00,
  ]), None],
  [0.000, 1372.000, np.array([
        -0.121047212750e-25,
         0.971511471520e-22,
        -0.320207200030e-18,
         0.560750590590e-15,
        -0.560728448890e-12,
         0.318409457190e-09,
        -0.994575928740e-07,
         0.185587700320e-04,
         0.389212049750e-01,
        -0.176004136860e-01,
  ]), [0.118597600000e+00,-0.118343200000e-03,0.126968600000e+03]],
  ],'C','mV',
       calibration='ITS-90',
       source='NIST SRD 60, type K'),
     ttype='Type K',
     composition='90Ni,10Cr - 95Ni,2Mg,2Al,1Si'),

'N': Thermocouple_Reference(Polynomial_Gaussian_Piecewise_Function([
  [-270.000, 0.000, np.array([
        -0.934196678350e-19,
        -0.760893007910e-16,
        -0.226534380030e-13,
        -0.263033577160e-11,
        -0.464120397590e-10,
        -0.938411115540e-07,
         0.109574842280e-04,
         0.261591059620e-01,
         0.000000000000e+00,
  ]), None],
  [0., 1300., np.array([
        -0.306821961510e-28,
         0.208492293390e-24,
        -0.608632456070e-21,
         0.997453389920e-18,
        -0.100634715190e-14,
         0.643118193390e-12,
        -0.252611697940e-09,
         0.438256272370e-07,
         0.157101418800e-04,
         0.259293946010e-01,
         0.000000000000e+00,
  ]), None],
  ],'C','mV',
       calibration='ITS-90',
       source='NIST SRD 60, type N'),
     ttype='Type N',
     composition='84.1Ni,14.4Cr,1.4Si,0.1Mg - 95.6Ni,4.4Si'),

'R': Thermocouple_Reference(Polynomial_Gaussian_Piecewise_Function([
  [-50.000, 1064.180, np.array([
        -0.281038625251e-26,
         0.157716482367e-22,
        -0.373105886191e-19,
         0.500777441034e-16,
        -0.462347666298e-13,
         0.356916001063e-10,
        -0.238855693017e-07,
         0.139166589782e-04,
         0.528961729765e-02,
         0.000000000000e+00,
  ]), None],
  [1064.180, 1664.500, np.array([
        -0.293359668173e-15,
         0.205305291024e-11,
        -0.764085947576e-08,
         0.159564501865e-04,
        -0.252061251332e-02,
         0.295157925316e+01,
  ]), None],
  [1664.5, 1768.1, np.array([
        -0.934633971046e-14,
        -0.345895706453e-07,
         0.171280280471e-03,
        -0.268819888545e+00,
         0.152232118209e+03,
  ]), None],
  ],'C','mV',
       calibration='ITS-90',
       source='NIST SRD 60, type R'),
     ttype='Type R',
     composition='87Pt,13Rh - Pt'),

'S': Thermocouple_Reference(Polynomial_Gaussian_Piecewise_Function([
  [-50.000, 1064.180, np.array([
         0.271443176145e-23,
        -0.125068871393e-19,
         0.255744251786e-16,
        -0.331465196389e-13,
         0.322028823036e-10,
        -0.232477968689e-07,
         0.125934289740e-04,
         0.540313308631e-02,
         0.000000000000e+00,
  ]), None],
  [1064.180, 1664.500, np.array([
         0.129989605174e-13,
        -0.164856259209e-08,
         0.654805192818e-05,
         0.334509311344e-02,
         0.132900444085e+01,
  ]), None],
  [1664.5, 1768.1, np.array([
        -0.943223690612e-14,
        -0.330439046987e-07,
         0.163693574641e-03,
        -0.258430516752e+00,
         0.146628232636e+03,
  ]), None],
  ],'C','mV',
       calibration='ITS-90',
       source='NIST SRD 60, type S'),
     ttype='Type S',
     composition='90Pt,10Rh - Pt'),

'T': Thermocouple_Reference(Polynomial_Gaussian_Piecewise_Function([
  [-270.000, 0.000, np.array([
         0.797951539270e-30,
         0.139450270620e-26,
         0.107955392700e-23,
         0.487686622860e-21,
         0.142515947790e-18,
         0.282135219250e-16,
         0.384939398830e-14,
         0.360711542050e-12,
         0.226511565930e-10,
         0.901380195590e-09,
         0.200329735540e-07,
         0.118443231050e-06,
         0.441944343470e-04,
         0.387481063640e-01,
         0.000000000000e+00,
  ]), None],
  [0.000, 400.000, np.array([
        -0.275129016730e-19,
         0.454791352900e-16,
        -0.308157587720e-13,
         0.109968809280e-10,
        -0.218822568460e-08,
         0.206182434040e-06,
         0.332922278800e-04,
         0.387481063640e-01,
         0.000000000000e+00,
  ]), None],
  ],'C','mV',
       calibration='ITS-90',
       source='NIST SRD 60, type T'),
     ttype='Type T',
     composition='Cu - 55Cu,45Ni'),

}

#end of module
