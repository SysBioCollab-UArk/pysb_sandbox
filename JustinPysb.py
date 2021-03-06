from pysb import *
from pysb.simulator import ScipyOdeSimulator
import numpy as np
import matplotlib.pyplot as plt

Model()

print(model)


Monomer("A",["b","state"],{"state":["U","P"]})
Monomer("B",["a"])

Parameter("kf_AB",1)
Parameter("kr_AB",1)


Parameter("A_init",100)
Initial(A(b=None,state="U"), A_init)


Parameter("B_init",100)

Initial(B(a=None),B_init)





Rule("ABindsB",A(b=None, state="U")+B(a=None) | A(b=1, state="U")% B(a=1), kf_AB, kr_AB)

Parameter("k_A_U_to_P", 1)
Rule("AStateChange", A(b=1, state="U") % B(a=1) >>A(b=1, state="P") % B(a=1), k_A_U_to_P)

Observable("AFree", A(b=None))
Observable("APhos", A(state="P"))

tspan = np.linspace(0,10,101)

sim = ScipyOdeSimulator(model, tspan, verbose=True)
result = sim.run()

obs = result.observables

for o in model.observables:
    plt.plot(tspan, obs[o.name], lw=2, lable=o.name)
plt.legend(loc=0)
plt.xlabel("time")
plt.ylabel("count")

plt.show()




print(model)