#Escriba un programa en Python que acepte una ruta remota de recurso samba, 
# y lo separe en nombre(IP) del equipo y ruta
#Entrada: //1.1.1.1/eoi/python Salida: equipo=1.1.1.1; ruta=/eoi/python
texto="//1.1.1.1/eoi/python"
print("equipo",texto[2:9])
print("ruta:",texto[9:20])
forma2=input("Digite el texto: ")
print(f"equipo",forma2[2:9])
print(f"ruta",forma2[9:20])