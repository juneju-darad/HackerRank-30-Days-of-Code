# one line:
# print(len(max(str(bin(int(input())))[2:].split('0'))))

if __name__ == '__main__':
    n = list(bin(int(input())))
    count = 1
    list2 = []
    for x in range(len(n)-1):
        current = n[x]
        next = n[x+1]
        if current == next:
            count+=1
            list2.append(count)
        else:
            list2.append(count)
            count = 1
    print(max(list2))
