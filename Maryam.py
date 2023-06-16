from pysb import *
from pysb.simulator import ScipyOdeSimulator
import numpy as np
import matplotlib.pyplot as plt

Model()
Monomer("A")
Parameter("A_0",100)
Initial(A(),A_0)
Parameter("kdeg",1)
Rule("A_degrade",A() >> None,kdeg)
Observable("A_tot",A())

print(model)
print(model.monomers)
print(model.parameters)
print(model.rules)

tspan=np.linspace(0,1,101)
sim=ScipyOdeSimulator(model,tspan,verbose=True)
result=sim.run()

plt.plot(tspan,result.observables["A_tot"],lw=2,label="A_tot")
plt.xlabel("time")
plt.ylabel("concentration")
plt.legend(loc=0)

plt.show()
