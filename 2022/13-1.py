def find_zeroth(listU):
    print(listU)
    if(listU == []):
        return -1
    elif(type(listU[0]) == type(1)):
        return listU[0]
    else:
        return find_zeroth(listU[0])

def right_order(list1, list2):
    if(list1 == []):
        return True
    elif(list2 == []):
        return False
    print(list1, list2)
    for j in range(max(len(list1), len(list2))):
        print(j)
        if(j >= len(list1)):
            return True
        elif(j >= len(list2)):
            return False

        elif(type(list1[j]) == type(list2[j]) and type(list1[j]) == type(1)):
            print("test")
            if(list1[j] > list2[j]):
                return False
            elif(list1[j] < list2[j]):
                return True
            print("test2")
        elif(type(list1[j]) == type(list2[j]) and type(list1[j]) == type(["1"])):
            print("test3")
            if(right_order(list1[j], list2[j]) != "end"):
                return right_order(list1[j], list2[j])

        elif(type(list1[j]) == type(["1"])):
            print("test4", list1[j], list2[j])
            if(find_zeroth(list1[j]) > list2[j]):
                return False
            elif(find_zeroth(list1[j]) < list2[j]):
                return True
        elif(type(list2[j]) == type(["1"])):
            print("test5")
            if(list1[j] > find_zeroth(list2[j])):
                return False
            elif(list1[j] < find_zeroth(list2[j])):
                return True
        else:
            return True
    return "End"


N = open("input13.txt", "r").read().split("\n")

pairs = len(N) // 3

rightOrderInxs = []

for i in range(pairs):
    ele1 = eval(N[i*3])
    ele2 = eval(N[i*3 + 1])

    if(right_order(ele1, ele2)):
        rightOrderInxs.append(i + 1)
        print("right", i + 1)

print(rightOrderInxs)
print(sum(rightOrderInxs))

    