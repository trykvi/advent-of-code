N = input()

for i in range(len(N)):
    if(len(N[:i]) > 13):
        if(len(N[:i][(i-14):]) == len(set(N[:i][(i-14):]))):
            print(i)
            break