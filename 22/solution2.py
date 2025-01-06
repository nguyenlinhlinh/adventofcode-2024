from collections import defaultdict
def getInputs(file):
    return[int(line.replace("\n", "")) for line in file.readlines()]

def mix(nbr, value):
    return nbr^value

def prune(nbr):
    return nbr % 16777216

def mul(nbr):
    return nbr * 64

def getNextSecretNbr(secretNbr):
    bigNbr = 16777216
    x = ((secretNbr * 64)^secretNbr) % bigNbr
    y = ((x // 32) ^ x) % bigNbr 
    z = ((y * 2048) ^ y) % bigNbr
    return z

def generateSecretNbrs(secretNbrs, times):
    result = {}
    sequences = {}
    for nbr in secretNbrs:
        result[nbr] = nbr
        sequences[nbr] = ([int(str(nbr)[-1])], [None])

    for i in range(times):
        for initialSecretNbr, nbr in result.items():
            next = getNextSecretNbr(nbr)
            result[initialSecretNbr] = next
            price = int(str(next)[-1])
            prevPrice = sequences[initialSecretNbr][0][-1]
            sequences[initialSecretNbr][0].append(price)
            sequences[initialSecretNbr][1].append(price - prevPrice)

    return sequences

def findBestPrice(sequences):
    lookupTable = defaultdict(int)
    for secretNbr, (prices, priceChanges) in sequences.items():
        sequenceSet = set()
        for i in range(1, len(priceChanges) - 3):
            seq = tuple(priceChanges[i: i + 4])
            p = prices[i + 3]
            if seq not in sequenceSet:
                sequenceSet.add(seq)
                lookupTable[seq] += p
    bestPrice = 0
    for seq, price in lookupTable.items():
        if price > bestPrice:
            bestPrice = price
    return bestPrice    

if __name__ == "__main__":
    file = open("22/input.txt", "r")
    secretNbrs = getInputs(file)
    result = generateSecretNbrs(secretNbrs, 2000)
    bestPrice = findBestPrice(result)
    print("Best price", bestPrice)

# solution 2152
