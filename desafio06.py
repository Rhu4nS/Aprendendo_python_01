# crie um algoritimo que crie um numero e mostre o seu dobro, triplo e raiz quadrada:
'''
n1 = int(input(' Digite um numero: '))
d = n1*2
t = n1*3
r = n1**(1/2)

print(' O número é:\n {}\n O dobro é:\n {}\n O triplo é:\n {}\n A raiz quadrada é:\n {}'.format(n1, d, t, r))
'''
#outro jeito de escrever

n1 = int(input(' Digite um numero: '))
print(' O numero escolido é: {}\n O dobro de {} é {}\n O triplo de {} é {}\n A raiz quadrada de {} é {:.2f}'.format(n1, n1, (n1*2), n1, (n1*3), n1,(n1**(1/2))))