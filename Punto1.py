#Realizar un programa que realice la multiplicación de dos matrices. Tener en cuenta las validaciones que deben 
#hacerse para realizar la operación.

matA = [[2, 7, 2], 
        [4, 5, 6],
        [7, 2, 9]]

matB = [[9, 2, 7], 
        [1, 5, 2],
        [3, 2, 1]]

def MulMatriz(matA, matB):

    # Validación para comprobar que el número de columnas de matA es igual al número de filas de matB
    if len(matA[0]) != len(matB):
        return "No es posible multiplicar las matrices"
    
    #MatC con el mismo número de filas que A y el mismo número de columnas que B
    matC = [[0 for i in range(len(matB[0]))] for j in range(len(matA))]
    
    #Multiplicación de matrices
    for i in range(len(matA)):
        for j in range(len(matB[0])):
            for m in range(len(matB)):
                matC[i][j] += matA[i][m] * matB[m][j]
    return matC



matC = MulMatriz(matA, matB)
print(matC)

