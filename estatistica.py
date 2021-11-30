import math

quantidade_de_medias = int(input('Digite o número de média que serão calculadas - '))

medias = []

for i in range(0, quantidade_de_medias):
    medias.append(float(input(f'Digite o {i + 1}º valor: ')))

media_aritmetica = sum(medias) / quantidade_de_medias

print(f'A média aritmética é igual a {media_aritmetica}')

acumulador = 0

for i in range(0, quantidade_de_medias):
    acumulador += pow(medias[i] - media_aritmetica, 2)

acumulador = acumulador / (quantidade_de_medias - 1)
desvio_padrao = math.sqrt(acumulador)

print('Desvio padrão: {:.2f}'.format(desvio_padrao))

coeficiente_variacao = (desvio_padrao / media_aritmetica) * 100

print('Coeficiente_variacao: {:.2f}%'.format(coeficiente_variacao))
