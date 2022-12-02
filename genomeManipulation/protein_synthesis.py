from .translation import translate

codonTable = {
		'AUA':'I', 'AUC':'I', 'AUU':'I', 'AUG':'M',
		'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACU':'T',
		'AAC':'N', 'AAU':'N', 'AAA':'K', 'AAG':'K',
		'AGC':'S', 'AGU':'S', 'AGA':'R', 'AGG':'R',				
		'CUA':'L', 'CUC':'L', 'CUG':'L', 'CUU':'L',
		'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCU':'P',
		'CAC':'H', 'CAU':'H', 'CAA':'Q', 'CAG':'Q',
		'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGU':'R',
		'GUA':'V', 'GUC':'V', 'GUG':'V', 'GUU':'V',
		'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCU':'A',
		'GAC':'D', 'GAU':'D', 'GAA':'E', 'GAG':'E',
		'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGU':'G',
		'UCA':'S', 'UCC':'S', 'UCG':'S', 'UCU':'S',
		'UUC':'F', 'UUU':'F', 'UUA':'L', 'UUG':'L',
		'UAC':'Y', 'UAU':'Y', 'UGC':'C', 'UGU':'C', 
		'UGG':'W',
	}


start = "AUG"

stops = ['UAA','UGA','UAG']

def computeProteinChain(genome):

	genome = translate(genome)
	
	startIndex = genome.find(start)
	
	stopIndices = [genome.find(stop) for stop in stops]

	stopIndices = [_ for _ in stopIndices if _ >= 0 ]
	
	potentialCodingRegions = [genome[startIndex:stopIndex] for stopIndex in stopIndices]
	
	proteins = []
	
	for potentialCodingRegion in potentialCodingRegions:
		if len(potentialCodingRegion) % 3 == 0:
			protein = ""
			for i in range(0,len(potentialCodingRegion)-3,3):
				protein += codonTable[potentialCodingRegion[i:i+3]]
			proteins.append(protein)
			
	return proteins