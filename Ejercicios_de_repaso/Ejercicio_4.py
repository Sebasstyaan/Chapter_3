#Escriba un programa en Python que compute el futuro valor de una cantidad de dinero,
#a partir del capital inicial, el tipo de interés y el número de años
#Entrada: capital=10000; interés=3.5; años=7 Salida: 12722.792627665729
#capital=int(input("Digite el valor del capital solicitado:  "))
#interes=3.5
#print("La taza de interes para su credito es de 3.5")
#años=int(input("Digite la cantidad de años para pagar el credito:  "))
#formula=capital*(1+interes)**años
#print(formula)
c=int(input("Digite capital"))
i=float(input("Digite taza de interes"))
a=int(input("Digite años de plazo"))
n=c*(1+i)**7
print(n)