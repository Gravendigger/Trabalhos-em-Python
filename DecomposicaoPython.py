print('Por favor, digite um número: ')
n = int(input())
n1 = n
if n < 800:
    unidade = n % 10
    n = (n - unidade)//10
    dezena = n % 10
    n = (n - dezena)//10
    centena = n
    print('O número ',n1,' possui: ',unidade,' unidades, ',dezena,' dezenas e ',centena,' centenas.')
else:
    print('Este número não é valido.')
