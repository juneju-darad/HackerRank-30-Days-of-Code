# best solution:
# for i in range(int(input())):
#     s = input()
#     print(s[::2], s[1::2])


def evenOdd(s):
    even = ''
    odd = ''
    for i in range(0, len(s)):
        if i % 2 == 0:
            even = even + s[i]
        else:
            odd = odd + s[i]
    print('{} {}'.format(even, odd))


if __name__ == '__main__':
    str = []
    T = int(input())
    if 1 <= T <= 10:
        for i in range(0, T):
            str.append(input())

        if 2 <= len(str) <= 10000:
            for j in range(0, T):
                evenOdd(str[j])