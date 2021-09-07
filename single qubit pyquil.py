import numpy as np
from pyquil import Program, get_qc
from pyquil.api import WavefunctionSimulator
from pyquil.gates import*

wavefunction_simulator = WavefunctionSimulator()
qc = get_qc('9q-generic-qvm')

p = Program(X(0))
wavefunction = wavefunction_simulator.wavefunction(p)
print("X|0> = ", wavefunction)
print("The outcome probabilities are", wavefunction.get_outcome_probs())
print("This looks like a bit flip.\n")

p = Program(Y(0))
wavefunction = wavefunction_simulator.wavefunction(p)
print("Y|0> = ", wavefunction)
print("The outcome probabilities are", wavefunction.get_outcome_probs())
print("This also looks like a bit flip.\n")

p = Program(Z(0))
wavefunction = wavefunction_simulator.wavefunction(p)
print("Z|0> = ", wavefunction)
print("The outcome probabilities are", wavefunction.get_outcome_probs())
print("This state looks unchanged.")


"""
-------------------------------------------------------------------
Composing qubit operations is the same as multiplying matrices sequentially
"""

p = Program(X(0), Y(0), Z(0))
wavefunction = wavefunction_simulator.wavefunction(p)

print("ZYX|0> = ", wavefunction)
print("With outcome probabilities\n", wavefunction.get_outcome_probs())






"""
--------------------------------------------------------------------
The Hadamard gate
"""
had_program = Program(H(0))
wavefunction = wavefunction_simulator.wavefunction(had_program)

print("H|0> = ", wavefunction)
print("With outcome probabilities\n", wavefunction.get_outcome_probs())
























