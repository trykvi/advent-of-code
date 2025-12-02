N = open("input2.txt", "r").read().split("\n")[:-1]

score = 0


loseMoves = {"A":3, "B":1, "C":2}
drawMoves = {"A":1, "B":2, "C":3}
winMoves = {"A":2, "B":3, "C":1}

for line in N:
    them, outcome = line.split()
    if(outcome == "X"):
        score += loseMoves[them]
    elif(outcome == "Y"):
        score += drawMoves[them] + 3
    elif(outcome == "Z"):
        score += winMoves[them] + 6
print(score)
