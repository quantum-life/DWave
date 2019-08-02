# It Works!
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite

DWAVE_SAPI_URL = 'https://cloud.dwavesys.com/sapi'
DWAVE_TOKEN = 'DEV-7c86da7d5e80b59ef47d1a76f9a99a4a924654bf'
DWAVE_SOLVER = 'DW_2000Q_2_1'

linear = {('me', 'me'): -1, ('you', 'you'): -1, ('them', 'them'): -1}
quadratic = {('me', 'you'): 2, ('me', 'you'): 2, ('me', 'you'): 2}
Q = dict(linear)
Q.update(quadratic)
response = EmbeddingComposite(DWaveSampler()).sample_qubo(Q, num_reads=10000)
for sample in response.data():
    print(sample)
