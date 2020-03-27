"""
The refdata module contains pure-element reference state data.
"""


from sympy import And, Piecewise, Symbol, log, exp
from pycalphad.variables import T
from collections import OrderedDict

# These are truncated versions of SGTE91. They are not correct and just here for an example.
# These functions form GHSER<ELEMENT> names, e.g. GHERAG and GHSERAL, which are used in the lattice stabilities later.
CustomRefstate2020Stable = OrderedDict(
[('AG',
  Piecewise((-7209.512 + 118.202013*T, And(T < 1234.93, T >= 298.15)), (-15095.252 + 190.266404*T, And(T < 3000.0, T >= 1234.93)), evaluate=False)),
 ('AL',
  Piecewise((-7976.15 + 137.093038*T, And(T < 700.0, T >= 298.15)), (-11276.24 + 223.048446*T, And(T < 933.47, T >= 700.0)), (-11278.378 + 188.684153*T, And(T < 2900.0, T >= 933.47)), evaluate=False)),
])

# This is the chemical potential relative to the standard state (reference structure, 1 mol, 298.15 K, 101325 Pa)
# The symbol GHSER[element] refers to an entry in SGTE above
# SGTE91[(element, reference structure)] = SGTE91Stable[element]
# Reference:
# A.T. Dinsdale, SGTE data for pure elements, Calphad, Volume 15, Issue 4, 1991, Pages 317-425, ISSN 0364-5916,
# http://dx.doi.org/10.1016/0364-5916(91)90030-N.
# http://www.sciencedirect.com/science/article/pii/036459169190030N
CustomRefstate2020 = OrderedDict(
[(('AG', 'BCC_A2'), Piecewise((3400 - 1.05*T + Symbol('GHSERAG'), And(T < 3000.0, T >= 298.15)), evaluate=False)),
 (('AG', 'CUB_A13'), Piecewise((3765.6 - 1.8826*T + Symbol('GHSERAG'), And(T < 3000.0, T >= 298.15)), evaluate=False)),
 (('AG', 'FCC_A1'), Piecewise((Symbol('GHSERAG'), And(T < 3000.0, T >= 298.15)), evaluate=False)),
 (('AG', 'HCP_A3'), Piecewise((300 + 0.3*T + Symbol('GHSERAG'), And(T < 3000.0, T >= 298.15)), evaluate=False)),
 (('AG', 'LIQUID'), Piecewise((11025.076 - 8.89102*T - 1.033905e-20*T**7 + Symbol('GHSERAG'), And(T < 1234.93, T >= 298.15)),
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

