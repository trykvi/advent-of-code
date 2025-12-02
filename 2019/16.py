def FFT(listN):
    result = [0]*len(listN)
    baseSequence = [0, 1, 0, -1]
    print(len(listN))
    for i in range(len(result)):
        sequence = []
        j = 0
        while(True):
            sequence += [baseSequence[j%4]]*(i+1)
            
            j += 1
            if(len(sequence) > len(listN)):
                sequence = sequence[1:][:(len(listN))]
                break
            
        for k in range(len(result)):          
            result[i] += listN[k] * sequence[k]
            
    for i in range(len(result)):
        result[i] = abs(result[i])%10

    return result

N = input()
offset = int(N[:7])
N = [int(i) for i in list(N)]

N = N*10000

for i in range(100):
    N = FFT(N)
    
print(N)
desired8 = ""
for i in range(8):
    desired8 += str(N[offset+i])

print(desired8)
