#Escriba un programa en Python que calcule la distancia euclΓ­dea entre dos puntos (π₯1, π¦1) y (π₯2, π¦2)
#Entrada: (π₯1 = 3, π¦1 = 5); (π₯2 = β7, π¦2 = β4) Salida: 13.45362404707371
x1=int(input("Digite vector x1: "))
y1=int(input("Digite vector y1: "))
x2=int(input("Digite vector x2: "))
y2=int(input("Digite vector y1: "))
d=((x2-x1)**2+(y2-y1)**2)**(1/2)
print("la distancia euclidia entre los puntos es: ", d)