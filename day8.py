if __name__ == '__main__':
    n = int(input())
    phoneBook = dict(input().split() for _ in range(n))
    while True:
        try:
            name = input()
            if name in phoneBook:
                # print('{}={}'.format(name, phoneBook[name]))
                print(f'{name}={phoneBook[name]}')
            else:
                print('Not found')
        except:
            break
