print('Deseja verificar sua média bimestral?')
Resp = input()

while Resp == 'sim':
    
    Alg = float(input('Digite a nota da disciplina de Algoritimo: '))
    Mat = float(input('Digite a nota da disciplina de Matemática: '))
    Ard = float(input('Digite a nota da disciplina de Arduino: '))
    Ing = float(input('Digite a nota da disciplina de Inglês: '))

    print('Sua média do seu bimestre é: ',(Alg+Mat+Ard+Ing)//4)

    print('Deseja verificar uma nova média?')
    Resp = input()
    

