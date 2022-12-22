from pysb import *
from pysb.simulator import ScipyOdeSimulator
import numpy as np
import matplotlib.pyplot as plt

Model()
Monomer('A', ['b', 'c'])
Monomer('B', ['a', 's'], {'s': ['u', 'p']})
Monomer('C', ['a'])
Parameter('kf_AB' , 1)
Parameter('kr_AB' , 10)
Rule('A_binds_B', A(b=None) + B(a=None, s='u') | A(b=1) % B(a=1, s='u'), kf_AB, kr_AB)
print(model)
print(model.monomers)