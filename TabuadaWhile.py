x = 0
n = int(input('Digite qual tabuada você quer ver: '))
while x <= 10:
    result = x * n
    print('{} x {} = {}'.format(n, x, result))
    x = x + 1