complementDictionary = {
    'A':'T',
    'T':'A',
    'C':'G',
    'G':'C'
}


def complement(genome):
    complementGenome = ''
    for base in genome:
        complementGenome += complementDictionary[base]

    return complementGenome(string[::-1])