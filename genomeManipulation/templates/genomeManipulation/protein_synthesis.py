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

table = {
		'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
		'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
		'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
		'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',				
		'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
		'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
		'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
		'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
		'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
		'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
		'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
		'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
		'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
		'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
		'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
		'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
	}

def findPotentialCodingSegments(sequence,stopList):
    potentialCodingSegments = []
    i,j = 0,0
    for _ in range(len(stopList)-1):
        i,j = stopList[_],stopList[_+1]
        start = sequence[i:j].find('ATG') + i
        if start > i and (j+3-start)%3==0 and j+3-start >= 50:
            seq = sequence[start:j]
            potentialCodingSegments.append(tuple([(i,j),seq]))
    return potentialCodingSegments

    stopList = [i for i in range(len(sq))
    if (sq.startswith('TGA',i) or 
        sq.startswith('TAG',i) or 
        sq.startswith('TAA',i))]
    orfs = findPotentialCodingSegments(sq,stopList)




