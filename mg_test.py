from pysb import *
from pysb.simulator import ScipyOdeSimulator
import numpy as np
import matplotlib.pyplot as plt





########## Creat a model ##########
###################################



## model's requirement elements ##
 
# Monomers
# Parameters
# Initials
# Rules ( BioNEtGEn or KAPPA ) 
# Observables
# simulation commands



# Declare a model
Model()

# Declare the monomers 
Monomer('A', ['b', 'state'], { 'state' : ['U', 'P'] })
Monomer('B', ['a'])
Monomer('C', ['X'],{'X' : ['active','inactive']})


# Declare parameters              
Parameter('kf_AB', 1)
Parameter('kr_AB', 1)
Parameter('A_init', 100)                # nunmber of molecules (Concentrations )
Parameter('B_init', 100)                # nunmber of molecules (Concentrations )
Parameter('C_init',150)                 # number of molecules  (Concentrations ) 
Parameter('k_A_U_to_P', 1)
Parameter('k_AP_active_C',0.1)          # C gets activate (e.g, 0.1 , 0.01 ,0.001 )


# Declare inintial conditions 
Initial(A(b=None, state='U'), A_init)
Initial(B(a=None), B_init)
Initial(C(X='inactive'),C_init)


# Declare binding rules  
Rule('A_binds_B', A(b=None, state='U') + B(a=None) | A(b=1, state='U') % B(a=1), kf_AB, kr_AB)
Rule('A_state_change', A(b=1, state='U') % B(a=1) >> A(b=1, state='P') % B(a=1), k_A_U_to_P)
Rule('AP_active_C', A(b=1, state='P') % B(a=1) + C(X = 'inactive') >> A(b=1, state='P') % B(a=1) + C(X = 'active'),k_AP_active_C)


# observe the complex 
Observable('A_free', A(b=None))
Observable('A_phos', A(state='P'))
# Observable('A_bound', A(b=1) % B(a=1))
Observable('A_bound', A(b=ANY))
Observable('C_active',C(X= 'active'))
Observable('C_inactive',C(X= 'inactive'))


# Declare the simulate time 
tStart = 0                          # Start time 
tEnd = 10                           # End time 
tPoints = 1001                      # number of time-points 

#from pylab import linspace
#tspan = linspace(tStart,tEnd, tDivid)

tspan = np.linspace(tStart,tEnd, tPoints)
print ("Simulating.........")


# Simulate the model 
sim = ScipyOdeSimulator(model, tspan, verbose=True)
result = sim.run()
obs = result.observables


# plot the trajectories 

for o in model.observables:
    plt.plot(tspan, obs[o.name], lw=2, label=o.name)
    
plt.xlabel('time (secounds)')
plt.ylabel('Concentration')
plt.legend(loc=1)              # legend location on the plot (1,2,3,4)

print(model)
print(model.monomers)
print(model.parameters)
print(model.rules)
print(model.observables)
for ic in model.initial_conditions:
    print(ic)


plt.show()