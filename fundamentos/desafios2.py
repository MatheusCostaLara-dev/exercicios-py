# Desafio 004: Faça um programa que 
# leia algo pleo teclado e 
# mostre na tela o seu tipo primitivo
# e todas as informações possiveis sobre ela
print('========== DESAFIO 004 ==========')
caractere = input('Digite algo')
print(type(caractere))
print('É um numero?: ',caractere.isnumeric())
print('É alfabético?: ',caractere.isalpha())
print('É um alfanumérico?: ',caractere.isalnum())