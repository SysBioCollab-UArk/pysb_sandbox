from pysb import *
from pysb.simulator import ScipyOdeSimulator
import numpy as np
import matplotlib.pyplot as plt

Model()

Monomer('Drug')
Monomer('Cell')

Parameter('Cell_0', 10000)
Initial(Cell(), Cell_0)

Parameter('Drug_0', 0)
Initial(Drug(), Drug_0)

# Parameter('k_release', 1)
# Rule('drug_release', None >> Drug(), k_release)

Parameter('k_drug', 0.001)
Rule('Cell_death', Cell() + Drug() >> Drug(), k_drug)

Observable('Drug_total', Drug())
Observable('Cell_total', Cell())

sim = ScipyOdeSimulator(model)

# First dose
tspan1 = np.linspace(0, 12, 121)
result = sim.run(tspan=tspan1, initials={model.species[1]: 0.5})

plt.figure('drug')
plt.plot(tspan1, result.observables['Drug_total'], lw=2, label='Drug')
plt.figure('cell')
plt.plot(tspan1, result.observables['Cell_total'], lw=2, label='Cell')

# Second dose
initials = result.species[-1]
initials[1] = 1
tspan2 = np.linspace(0, 12, 121)
result = sim.run(tspan=tspan2, initials=initials)

plt.figure('drug')
plt.plot(tspan1[-1] + tspan2, result.observables['Drug_total'], lw=2, label='Drug')
plt.figure('cell')
plt.plot(tspan1[-1] + tspan2, result.observables['Cell_total'], lw=2, label='Cell')

plt.figure('drug')
plt.xlabel('time')
plt.ylabel('amount')
plt.legend(loc=0)

plt.figure('cell')
plt.xlabel('time')
plt.ylabel('amount')
plt.legend(loc=0)

plt.show()
