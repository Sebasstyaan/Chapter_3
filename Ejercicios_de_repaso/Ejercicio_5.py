#Escriba un programa en Python que calcule la distancia euclídea entre dos puntos (𝑥1, 𝑦1) y (𝑥2, 𝑦2)
#Entrada: (𝑥1 = 3, 𝑦1 = 5); (𝑥2 = −7, 𝑦2 = −4) Salida: 13.45362404707371
x1=int(input("Digite vector x1: "))
y1=int(input("Digite vector y1: "))
x2=int(input("Digite vector x2: "))
y2=int(input("Digite vector y1: "))
d=((x2-x1)**2+(y2-y1)**2)**(1/2)
print("la distancia euclidia entre los puntos es: ", d)