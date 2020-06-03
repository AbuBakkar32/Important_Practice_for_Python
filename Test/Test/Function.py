
def Namata():
    a = input('what is the range of your Namata: ')
    c = input('how much it will be Iterate: ')
    for i in range(int(a)):
        if i == 0:
            continue
        for j in range(int(c)):
            if j == 0:
                continue
            b = i * j
            print('{} X {} = {}'.format(i, j, b))
        print(' ')


Namata()