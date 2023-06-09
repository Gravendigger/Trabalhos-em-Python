
valor = float(input('Digite o valor da sua prestação'))
print(' ')
dias = int(input('Digite a quantidade de dias em atraso'))
print(' ')

txmulta = float((valor * 2) / 100)
txjuros = float(valor / 100)

multa = float(txmulta * valor)
juros = float(((valor * (0.3*dias))*txjuros))
vlpagar = float(valor+multa+juros)

print('valor da prestação: ',valor)
print(' ')
print('quantidade de dias: ',dias)
print(' ')
print('valor da multa: ',multa)
print(' ')
print('valor dos juros: ',juros)
print(' ')
print('valor final a ser pago: ',vlpagar)
