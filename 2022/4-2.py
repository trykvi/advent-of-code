N = open("input4.txt", "r").read().split("\n")[:-1]

result = 0

for line in N:
    A, B = line.split(",")
    if(int(B.split("-")[0]) <= int(A.split("-")[1]) <= int(B.split("-")[1])): 
        print(line)      
        result += 1
    elif(int(A.split("-")[0]) <= int(B.split("-")[1]) <= int(A.split("-")[1])):
        print(line)
        result += 1

print(result)