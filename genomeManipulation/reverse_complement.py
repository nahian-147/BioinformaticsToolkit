complementDictionary = {
    'A':'T',
    'T':'A',
    'C':'G',
    'G':'C'
}


def reverseComplement(genome):
    reverseComplement = ''
    for base in genome:
        reverseComplement += complementDictionary[base]

    return reverseComplement[::-1]