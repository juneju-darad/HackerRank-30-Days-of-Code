def arrayRev(arr):
    i = len(arr) - 1
    while i >= 0:
        print(arr[i], end=' ')
        i -= 1

if __name__ == '__main__':
    N = int(input())
    if 1 <= N <= 1000:
        arr = [int(x) for x in input().split()]

    arrayRev(arr)