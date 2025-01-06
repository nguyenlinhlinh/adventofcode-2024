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
    for nbr in secretNbrs:
        result[nbr] = nbr
    for i in range(times):
        for initialSecretNbr, secretNbr in result.items():
            result[initialSecretNbr] = getNextSecretNbr(secretNbr)
    return result


if __name__ == "__main__":
    file = open("22/input.txt", "r")
    secretNbrs = getInputs(file)
    result = generateSecretNbrs(secretNbrs, 2000)
    print(sum(result.values()))
    
# solution 17965282217
