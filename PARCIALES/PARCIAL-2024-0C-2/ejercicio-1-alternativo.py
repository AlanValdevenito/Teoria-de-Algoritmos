import numpy as np

def strassen(A, B):
    n = len(A)

    # Caso base: si la matriz es 1x1, simplemente multiplicamos los valores
    if (n == 1):
        return A * B

    mid = n // 2  # Mitad del tamaño de la matriz (para dividir en submatrices)

    # Dividimos la matriz A en cuatro submatrices
    A11, A12 = A[:mid, :mid], A[:mid, mid:] # Esquina superior izquierda y esquina superior derecha
    A21, A22 = A[mid:, :mid], A[mid:, mid:] # Esquina inferior izquierda y esquina inferior derecha

    # Dividimos la matriz B en cuatro submatrices
    B11, B12 = B[:mid, :mid], B[:mid, mid:] # Esquina superior izquierda y esquina superior derecha
    B21, B22 = B[mid:, :mid], B[mid:, mid:] # Esquina inferior izquierda y esquina inferior derecha

    # Calculamos las 7 multiplicaciones de Strassen (M1 a M7)
    M1 = strassen(A11 + A22, B11 + B22)  # (A11 + A22) * (B11 + B22)
    M2 = strassen(A21 + A22, B11)        # (A21 + A22) * B11
    M3 = strassen(A11, B12 - B22)        # A11 * (B12 - B22)
    M4 = strassen(A22, B21 - B11)        # A22 * (B21 - B11)
    M5 = strassen(A11 + A12, B22)        # (A11 + A12) * B22
    M6 = strassen(A21 - A11, B11 + B12)  # (A21 - A11) * (B11 + B12)
    M7 = strassen(A12 - A22, B21 + B22)  # (A12 - A22) * (B21 + B22)

    # Construimos los bloques de la matriz C
    C11 = M1 + M4 - M5 + M7
    C12 = M3 + M5
    C21 = M2 + M4
    C22 = M1 - M2 + M3 + M6

    # Combinamos los bloques C11, C12, C21 y C22 en la matriz C final
    C = np.zeros((n, n))
    C[:mid, :mid] = C11   # Colocamos C11 en la esquina superior izquierda
    C[:mid, mid:] = C12   # Colocamos C12 en la esquina superior derecha
    C[mid:, :mid] = C21   # Colocamos C21 en la esquina inferior izquierda
    C[mid:, mid:] = C22   # Colocamos C22 en la esquina inferior derecha

    return C

# Complejidad

# A: 7 (Hay escritos siete llamados recursivos)
# B: 2 (Se divide al problema en dos)
# C: 0 (Operaciones)

# T(n) = A.T(n/B) + O(n^C) = 7 T(n/2) + O(n^0) = 7 T(n/2) + O(1)

# log (A) = log (7) = 2,8 > C → T(n) = O(n^(log (A))) = O(n^(log (7))) = O(n^2,8)
#    B         2                               B                2

A = np.array([[2, 3], [4, 5]])
B = np.array([[1, 2], [3, 4]])
C = np.array([[11, 16], [19, 28]])

print(strassen(A,B))

A = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
B = np.array([[16, 15, 14, 13], [12, 11, 10, 9], [8, 7, 6, 5], [4, 3, 2, 1]])
C = np.array([[80, 60, 70, 50], [240, 214, 188, 162], [400, 358, 316, 274], [560, 502, 444, 386]])

print(strassen(A,B))