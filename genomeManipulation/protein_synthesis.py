from .translation import translate

codonTable = {

}

start = ""

stops = []

def computeProteinChain(genome):

    startIndex = genome.find(start)

    stopIndices = [genome.find(stop) for stop in stops]

    potentialCodingRegions = [genome[startIndex:stopIndex] for stopIndex in stopIndices]

    proteins = []

    for potentialCodingRegion in potentialCodingRegions and len(potentialCodingRegion)%3 == 0:
        protein = ""
        for i in range(0,len(potentialCodingRegion)-3,3):
            protein += codonTable[potentialCodingRegion[i:i+3]]
        proteins.append(protein)

    return proteins