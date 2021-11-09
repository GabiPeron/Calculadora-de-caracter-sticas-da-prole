import csv
import names
import random

genes = {
    'eyeColor': ['O', 'o'],
    'hairColor': ['C', 'c'],
    # 'skinColor': ['P', 'p'],
    # 'dominantHand': ['M', 'm'],
    # 'earLobule': ['R', 'r'],
    # 'noseFormat': ['N', 'n'],
    # 'hairSwirl': ['S', 's'],
    # 'widowBeak': ['V', 'v'],
    # 'dimples': ['A', 'a'],
    # 'ptc': ['T', 't'],
    # 'thumb': ['L', 'l'],
    # 'earTip': ['U', 'u'],
    # 'eyebrow': ['B', 'b'],
    # 'freckles': ['D', 'd'],
    # 'eyelash': ['I', 'i'],
    # 'eyeFormat': ['H', 'h'],
    # 'cerumen': ['E', 'e'],
    # 'wisdowTeeth': ['Z', 'z']
}

index = 1

with open('dataset.csv', 'w', newline='') as dataset:
    header = ['index', 'name']
    header += genes.keys()

    writer = csv.DictWriter(dataset, fieldnames=header)
    writer.writeheader()

    while (index <= 2):
        row = {
            'index' : index,
            'name': names.get_first_name()
        }

        for gene in genes:
            row[gene] = (genes[gene][random.randint(0, 1)] + genes[gene][random.randint(0, 1)])

        writer.writerow(row)

        index += 1