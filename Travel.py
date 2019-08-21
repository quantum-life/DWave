from dwave.system.samplers import DWaveSampler
# Set Q for the minor-embedded problem QUBO
qubit_biases = {(0, 0): 0.3333, (1, 1): -0.333, (4, 4): -0.333, (5, 5): 0.333}
coupler_strengths = {(0, 4): 0.667, (0, 5): -1, (1, 4): 0.667, (1, 5): 0.667}
Q = dict(qubit_biases)
Q.update(coupler_strengths)
# Sample once on a D-Wave system and print the returned sample
response = DWaveSampler().sample_qubo(Q, num_reads=10000)
print(next(response.samples()))

for (sample, energy, num) in response.data():
        print(sample, "Energy: ", energy, "Occurrences: ", num)
