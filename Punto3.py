#Utilizar una multilista para cargar los votos obtenidos por tres candidatos a una elección de gobernador. 
#Se debe almacenar el nombre del candidato, el municipio (5 municipios en total) y el total de votos. 
#Realizar un programa que realice lo siguiente: 

#1. Solicitar los nombres de los candidatos, el municipio y la cantidad de votos obtenidos.
#2. Imprimir el total de votos de un candidato solicitado.
#3. Imprimir el total de votos en un municipio solicitado.
#4. Imprimir el candidato ganador.


multilista = [[["candidato1", 0] for j in range(5)] for i in range(3)]


for i in range(3):
    candidato = input("Ingrese el nombre del candidato #" + str(i+1) + ": ")
    for j in range(5):
        municipio = input("Ingrese el nombre del municipio #" + str(j+1) + ": ")
        votos = int(input("Ingrese la cantidad de votos obtenidos por " + candidato + " en " + municipio + ": "))
        multilista[i][j] = [candidato, votos]


candidato_solicitado = input("Ingrese el nombre del candidato del que desea conocer el total de votos: ")
total_votos_candidato = 0
for i in range(3):
    for j in range(5):
        if multilista[i][j][0] == candidato_solicitado:
            total_votos_candidato += multilista[i][j][1]
print("El total de votos obtenidos por " + candidato_solicitado + " es: " + str(total_votos_candidato))


municipio_solicitado = input("Ingrese el nombre del municipio del que desea conocer el total de votos: ")
total_votos_municipio = 0
for i in range(3):
    for j in range(5):
        if multilista[i][j][0] != "" and municipio_solicitado == j:
            total_votos_municipio += multilista[i][j][1]
print("El total de votos obtenidos en " + municipio_solicitado + " es: " + str(total_votos_municipio))


votos_candidato = [0, 0, 0]
for i in range(3):
    for j in range(5):
        votos_candidato[i] += multilista[i][j][1]
ganador = votos_candidato.index(max(votos_candidato))
print("El candidato ganador es: " + multilista[ganador][0][0])
