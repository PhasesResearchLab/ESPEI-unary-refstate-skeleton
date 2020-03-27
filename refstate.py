"""
The refdata module contains pure-element reference state data.
"""


from sympy import And, Piecewise, Symbol, log, exp
from pycalphad.variables import T
from collections import OrderedDict

# Note these are the same as SGTE91 and just here for an example.
# These functions form GHSER<ELEMENT> names, e.g. GHERAG and GHSERAL, which are used in the lattice stabilities later.
BOCK2015Stable = OrderedDict(
[('AG',
  Piecewise((-3.98587e-7*T**3 - 0.001790585*T**2 - 23.8463314*T*log(T) + 118.202013*T - 7209.512 - 12011/T, And(T < 1234.93, T >= 298.15)), (-33.472*T*log(T) + 190.266404*T - 15095.252 + 1.411773e+29/T**9, And(T < 3000.0, T >= 1234.93)), evaluate=False)),
 ('AL',
  Piecewise((-8.77664e-7*T**3 - 0.001884662*T**2 - 24.3671976*T*log(T) + 137.093038*T - 7976.15 + 74092/T, And(T < 700.0, T >= 298.15)), (-5.764227e-6*T**3 + 0.018531982*T**2 - 38.5844296*T*log(T) + 223.048446*T - 11276.24 + 74092/T, And(T < 933.47, T >= 700.0)), (-31.748192*T*log(T) + 188.684153*T - 11278.378 - 1.230524e+28/T**9, And(T < 2900.0, T >= 933.47)), evaluate=False)),
])

# This is the chemical potential relative to the standard state (reference structure, 1 mol, 298.15 K, 101325 Pa)
# The symbol GHSER[element] refers to an entry in SGTE above
# SGTE91[(element, reference structure)] = SGTE91Stable[element]
# Reference:
# A.T. Dinsdale, SGTE data for pure elements, Calphad, Volume 15, Issue 4, 1991, Pages 317-425, ISSN 0364-5916,
# http://dx.doi.org/10.1016/0364-5916(91)90030-N.
# http://www.sciencedirect.com/science/article/pii/036459169190030N
BOCK2015 = OrderedDict(
[(('AG', 'BCC_A2'), Piecewise((-1.05*T + Symbol('GHSERAG') + 3400, And(T < 3000.0, T >= 298.15)), evaluate=False)),
 (('AG', 'CUB_A13'), Piecewise((-1.8826*T + Symbol('GHSERAG') + 3765.6, And(T < 3000.0, T >= 298.15)), evaluate=False)),
 (('AG', 'FCC_A1'), Piecewise((Symbol('GHSERAG'), And(T < 3000.0, T >= 298.15)), evaluate=False)),
 (('AG', 'HCP_A3'), Piecewise((0.3*T + Symbol('GHSERAG') + 300, And(T < 3000.0, T >= 298.15)), evaluate=False)),
 (('AG', 'LIQUID'), Piecewise((-1.033905e-20*T**7 - 8.89102*T + Symbol('GHSERAG') + 11025.076, And(T < 1234.93, T >= 298.15)),
                              (-33.472*T*log(T) + 180.964656*T - 3587.111, And(T < 3000.0, T >= 1234.93)), evaluate=False)),
 (('AL', 'BCC_A2'), Piecewise((-4.813*T + Symbol('GHSERAL') + 10083, And(T < 2900.0, T >= 298.15)), evaluate=False)),
 (('AL', 'BCT_A5'), Piecewise((-4.813*T + Symbol('GHSERAL') + 10083, And(T < 2900.0, T >= 298.15)), evaluate=False)),
 (('AL', 'CBCC_A12'), Piecewise((-4.813*T + Symbol('GHSERAL') + 10083.4, And(T < 2900.0, T >= 298.15)), evaluate=False)),
 (('AL', 'CUB_A13'), Piecewise((-4.8116*T + Symbol('GHSERAL') + 10920.44, And(T < 2900.0, T >= 298.15)), evaluate=False)),
 (('AL', 'DIAMOND_A4'), Piecewise((30*T + Symbol('GHSERAL'), And(T < 2900.0, T >= 298.15)), evaluate=False)),
 (('AL', 'FCC_A1'), Piecewise((Symbol('GHSERAL'), And(T < 2900.0, T >= 298.15)), evaluate=False)),
 (('AL', 'HCP_A3'), Piecewise((-1.8*T + Symbol('GHSERAL') + 5481, And(T < 2900.0, T >= 298.15)), evaluate=False)),
 (('AL', 'LIQUID'), Piecewise((7.9337e-20*T**7 - 11.841867*T + Symbol('GHSERAL') + 11005.029, And(T < 700.0, T >= 298.15)),
                              (7.9337e-20*T**7 - 11.841867*T + Symbol('GHSERAL') + 11005.03, And(T < 933.47, T >= 700.0)),
                              (-31.748192*T*log(T) + 177.430178*T - 795.996, And(T < 2900.0, T >= 933.47)), evaluate=False)),
])

