from pysb import *
from pysb.simulator import ScipyOdeSimulator
import numpy as np
import matplotlib.pyplot as plt

Model()

# Monomers
# Parameters
# Initials
# Rules
# Observables
# simulation commands

Monomer('A', ['b', 'state'], {'state': ['U', 'P'] })
Monomer('B',['a'])

Parameter('A_init', 100)
Initial(A(b=None, state='U'), A_init)
Parameter('B_init', 100)
Initial(B(a=None), B_init)

Parameter('kf_AB', 1)
Parameter('kr_AB', 1)
Rule('A_binds_B', A(b=None, state='U') + B(a=None) | A(b=1, state='U') % B(a=1), kf_AB, kr_AB
Parameter('k_A_U_to_P', 1)
Rule('A_state_change', A(b=1, state='U') % B(a=1) >> A(b=1, state='P') % B(a=1), k_A_U_To_P)

Observable('A_free', A(b=None))
Observable('A_phos', A(state='P'))
#Observable('A_bound, A(b=1') % B(a=1))
Observable('A_bound', A(b=ANY))

tspan = np.linspace(0, 10, 101)
sim = ScipyOdeSimulator(model, tspan, verbose=True)
result = sim.run()

obs =  result.observables

for o in model.observables:
    plt.plot(tspan, obs[o.name] lw=2, label=o.name)
plt.xlabel('time')
plt.ylabel('concentration')
plt.legend(loc=0)

plt.show()

print(model)