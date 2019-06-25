import numpy as np

statevector=np.array([0.2,0.8])

transition=np.array([[0.6,0.4],[0.3,0.7]])

states = [statevector]

for i in range(3):
    statevector=np.dot(statevector,transition)
states.append(statevector)

print(states)
