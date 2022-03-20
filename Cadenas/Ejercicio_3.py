#Escriba un programa en Python que acepte un «string» con los 8 dígitos de un NIF,
#y calcule su dígito de control
letra=('TRWAGMYFPDXBNJZSQVHLCKE')
identificacion=int(input("Digite su numero de identificacion: "))
identificacion_completa=letra[int(identificacion) % 23]
print(f"su identificacion completa es: {identificacion}{identificacion_completa}")