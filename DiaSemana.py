print('Digite um número de 1 a 7 para definir o dia.')
d = int(input())

if d == 1:
    print('Hoje é domingo.')
elif d == 2:
    print('Hoje é segunda.')
elif d == 3:
    print ('Hoje é terça.')
elif d == 4:
    print ('Hoje é quarta.')
elif d == 5:
    print ('Hoje é quinta.')
elif d == 6:
    print ('Hoje é sexta.')
elif d == 7:
    print ('Hoje é sábado.')
else:
    print ('ERROR: Número digitado não é valido.')
