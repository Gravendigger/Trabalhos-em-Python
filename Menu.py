cont = int(0)
saldo = int(0)
media = int(0)
valor = int(0)

print('Deseja digitar um valor?')
print(' ')
print('[1] - SIM')
print('[2] - NÃO')
print(' ')
res = int(input('Opção: '))

while res == 1:
        nome = str(input('Digite seu nome: '))
        print(' ')
        valor = int(input('Digite um valor: '))
        print(' ')
        
        cont += 1 
        saldo = saldo + valor
        media = saldo/cont
        
        print('Nome do usuario: ',nome)
        print('Total de valores digitados:',cont)
        print('Saldo total dos valores digitados:',saldo)
        print('Média dos valores digitados:',media)
        print('')
        print('Deseja digitar um novo valor?')
        print(' ')
        print('[1] - SIM')
        print('[2] - NÃO')
        print(' ')
        res = int(input('Opção: '))
        

print('Programa encerrado.')
        
        
        

