import time
import random

# --- Generación (no se cronometra) ---
def generar_tres_arreglos():
    return (
        [random.randint(1, 1000) for _ in range(10)],
        [random.randint(1, 1000) for _ in range(100)],
        [random.randint(1, 1000) for _ in range(1000)],
    )

def bubbleSort(A):
    n = len(A)
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                swapped = True
        if not swapped:
            break
    return A

def medir_tiempo_ordenamiento(arr, sorter):
    t0 = time.perf_counter()
    _ = sorter(arr)   # NO imprime, NO modifica el original
    t1 = time.perf_counter()
    return t1 - t0

# --- Ejemplo de uso ---
a10, a100, a1000 = generar_tres_arreglos()

t10   = medir_tiempo_ordenamiento(a10, bubbleSort)
t100  = medir_tiempo_ordenamiento(a100, bubbleSort)
t1000 = medir_tiempo_ordenamiento(a1000, bubbleSort)

# Salida (esto sí imprime pero NO afecta las mediciones)
print(f"Tiempo arreglo 10  : {t10*1000:.3f} ms")
print(f"Tiempo arreglo 100 : {t100*1000:.3f} ms")
print(f"Tiempo arreglo 1000: {t1000*1000:.3f} ms")
