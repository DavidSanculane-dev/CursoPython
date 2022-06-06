print('=====Media=====')

nota1 = int(input('Digite a primeira Nota: '))
nota2 = int(input('Digita a segunda Nota: '))
media = (nota1 + nota2)/2

if media >= 10:
    print('Parabens, APROVADO!')
else: print('Infelizmente, REPROVOU!')
print('A sua média entre {} e {} é: {}'.format(nota1, nota2, media))