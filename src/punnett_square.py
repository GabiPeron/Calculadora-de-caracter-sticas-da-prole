import pandas as pd
from itertools import groupby, product

def allele(e):
    return [list(v) for _, v in groupby(e, key = str.lower)]

def punnett(a, b):
    return [''.join(e)
        for e in product(*([''.join(e) for e in product(*e)]
                    for e in zip(allele(a), allele(b))))]

dataset = pd.read_csv('dataset.csv')

crossover_samples = dataset.sample(2)

crossover_genotypes = []

for sample in crossover_samples.itertuples():
    crossover_genotypes.append(sample.eyeColor + sample.hairColor)

print(punnett(crossover_genotypes[0], crossover_genotypes[1]))