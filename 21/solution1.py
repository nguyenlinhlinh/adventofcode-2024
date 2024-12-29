from collections import defaultdict
import heapq
import sys
UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)
directions = [UP, DOWN, LEFT, RIGHT]
dirToString = {UP: "^", DOWN: "v", LEFT: "<", RIGHT: ">"}
numericKeypad = [
    ['7','8','9'],
    ['4','5','6'],
    ['1','2','3'],
    [None, '0', 'A']
]
directionalKeypad = [
    [None,'^','A'],
    ['<','v','>'],
]

def getInputs(file):
    return[line.replace("\n", "") for line in file.readlines()]

def isInsideKeypad(pos, rows, cols):
    return pos[0] in range(rows) and pos[1] in range(cols)

def buildKeyPadGraph(keypad):
    rows, cols = len(keypad), len(keypad[0])
    buttons = {}

    for r in range(len(keypad)):
        for c in range(len(keypad[0])):
            button = keypad[r][c]
            if button == None:
                continue
            buttons[button] = {}
            for (dR, dC) in directions:
                nextPos = (r + dR, c + dC)
                if isInsideKeypad(nextPos, rows, cols) and keypad[nextPos[0]][nextPos[1]] != None:
                    nextButton = keypad[nextPos[0]][nextPos[1]]
                    buttons[button][dirToString[(dR, dC)]] = nextButton
    return buttons

def robot(char, buttons, currentButton):
    result = []
    bestLength = sys.maxsize
    queue = [(0, currentButton, None, '')]
    heapq.heapify(queue)
    visited = set()
    while len(queue):
        (step, button, fromButton, seq) = heapq.heappop(queue)
        if button == char and step <= bestLength:
            result.append(seq + 'A') 
            bestLength = step         
        if (button, fromButton) in visited:
            continue
        visited.add((button, fromButton))
        for dir, nextButton in buttons[button].items():
            if (nextButton, button) not in visited:
                heapq.heappush(queue, (step + 1, nextButton, button, seq + dir))
        currentButton = char
    return result

def getStringWithShortestLength(array):
    minLen = sys.maxsize
    string = ''
    for s in array:
        if len(s) < minLen:
            minLen = len(s)
            string = s
    return string

def bestCharSeq(char, currentButton, depth, maxDepth):
    keypad = numericButtons if depth == maxDepth else directionalButtons
    seqs = robot(char, keypad, currentButton)
    if depth == 0:
        return getStringWithShortestLength(seqs)
    bestSequence = ''
    bestSeqLen = sys.maxsize
    for seq in seqs:
        result = ''
        currButton = 'A'
        for c in seq:
            result += bestCharSeq(c, currButton, depth - 1, maxDepth)
            currButton = c
        if len(result) < bestSeqLen:
            bestSeqLen = len(result)
            bestSequence = result
    return bestSequence

def bestSeq(seq, depth, maxDepth):
    currentButton = 'A'
    result = ''

    for char in seq:
        result += bestCharSeq(char, currentButton, depth, maxDepth)
        currentButton = char
    
    return result

if __name__ == "__main__":
    file = open("21/input.txt", "r")
    codes = getInputs(file)
    numericButtons = buildKeyPadGraph(numericKeypad)
    directionalButtons = buildKeyPadGraph(directionalKeypad)
    total = 0
    result = {}
    for seq in codes:
        result = bestSeq(seq, 2, 2)
        total += len(result) * int(seq[:-1])
    print(total)
    
# solution 179444