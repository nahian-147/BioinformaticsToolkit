translatorDictionary = {
    'A':'U',
    'T':'A',
    'C':'G',
    'G':'C'
}


def translate(genome):
    translatedGenome = ''
    for base in genome:
        translatedGenome += translatorDictionary[base]

    return translatedGenome