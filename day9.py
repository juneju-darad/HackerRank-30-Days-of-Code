# efficient solution
# factorial = lambda x : 1 if x<=1 else x*factorial(x-1)
# print(factorial(int(input())))


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == '__main__':
    n = int(input())
    print(factorial(n))
