while True:
    print('-' * 40)
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0: #se o número for menor que 0
        break
    print('-'*40)
    for c in range(1, 11):
        print('{} x {} = {}'.format(n, c, n * c))
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')