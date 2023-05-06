#Almacenar en una lista los datos de 5 empleados, cada elemento de la lista es una sub lista con el nombre del 
#empleado junto a sus últimos tres sueldos. El programa debe tener las siguientes funciones:

#1. Carga de los nombres de empleados y sus últimos tres sueldos.
#2. Imprimir el monto total cobrado por cada empleado.

def CargarDatos_Empleados():
    empleados = []
    for i in range(5):
        Nombre = input("Ingrese el nombre del empleado {}: ".format(i+1))
        sueldos = []
        for j in range(3):
            sueldoI = float(input("Ingrese el sueldo {}: ".format(j+1)))
            sueldos.append(sueldoI)
        empleadoI = [Nombre, sueldos]
        empleados.append(empleadoI)
    return empleados

def SaldoTotal(empleados):
    for empleadoI in empleados:
        Nombre = empleadoI[0]
        sueldos = empleadoI[1]
        STotal = sum(sueldos)
        print("{} ha cobrado un total de ${:.2f}".format(Nombre, STotal))


empleados = CargarDatos_Empleados()
SaldoTotal(empleados)

