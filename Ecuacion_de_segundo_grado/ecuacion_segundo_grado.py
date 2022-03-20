#𝑥1 =−𝑏 +√𝑏2 − 4𝑎𝑐/2a
#x2 =−𝑏 −√𝑏2 − 4𝑎𝑐/2𝑎
#Dados los coeficientes a=4, b=-6 y c=2 calcule sus dos soluciones.
a=float(input("Digite el valor para a : "))
b=float(input("Digite el valor para b : "))
c=float(input("Digite el valor para c : "))
if a!=0:
    x1=(-b+(((b**2)-(4*a*c))**0.5))/(2*a)
    x2=(-b-(((b**2)-(4*a*c))**0.5))/(2*a)
    print("Valor de x 1 es: ")
    print(x1)
    print("Valor de x 2 es: ")
    print(x2)
if a==0:
    print("El valor de a no puede ser 0")