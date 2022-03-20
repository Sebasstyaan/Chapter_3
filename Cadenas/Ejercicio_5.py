#Escriba un programa en Python que acepte una palabra en castellano y calcule una
#métrica que sea el número total de caracteres de la palabra multiplicado por el número
#total de vocales que contiene la palabra
texto=(input("Digite palabra: "))
convercion=len(texto)
a=texto.count('a')
e=texto.count('e')
i=texto.count('i')
o=texto.count('o')
u=texto.count('u')
metrica=convercion*(a+e+i+o+u)
print(f'Resultado: {metrica}')
print(f'{convercion}')