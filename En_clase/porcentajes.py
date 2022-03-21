#Elabore un algoritmo que lea las notas de un estudiante para la asignatura de programacion
#la primera nota correspondiente a la evaluacion final que tendra un porcentaje del 50%
#la segunda nota corresponde a los 3 quizes que equivalen a un 20%
#y la tercera nota corresponde al trabajo final que equivale 30%
#al final el programa mostrara el nombre del estudiante y la nota final de la asignatura
estudiante=input("Nombre del estudiante: ")
evaluacion_final=float(input("Digite nota de la evaluacion final: "))
quiz1=float(input("Digite nota del primer quiz: "))
quiz2=float(input("Digite nota del segundo quiz: "))
quiz3=float(input("Digite nota del tercer quiz: "))
trabajo_final=float(input("Digite nota del trabajo final: "))
promedio1=evaluacion_final*0.50
promedio2=((quiz1+quiz2+quiz3)/3)*0.20
promedio3=trabajo_final*0.30
promedio4=promedio1+promedio2+promedio3
print(f'{promedio4}')