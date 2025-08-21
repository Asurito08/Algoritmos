import time
import random

# --- Generación (no se cronometra) ---
def generar_tres_arreglos():
    return (
        [random.randint(1, 1000) for _ in range(10)],
        [random.randint(1, 1000) for _ in range(100)],
        [random.randint(1, 1000) for _ in range(1000)],
    )

def bubble_sort(a, reverse=False):
    copia = a[:]
    n = len(copia)
    while n > 1:
        last_swap = 0
        for i in range(1, n):
            if (not reverse and copia[i-1] > copia[i]) or (reverse and copia[i-1] < copia[i]):
                copia[i-1], copia[i] = copia[i], copia[i-1]
                last_swap = i
        if last_swap == 0:
            break
        n = last_swap
    return copia

def medir_tiempo_ordenamiento(arr, sorter):
    t0 = time.perf_counter()
    _ = sorter(arr)   # NO imprime, NO modifica el original
    t1 = time.perf_counter()
    return t1 - t0

# --- Ejemplo de uso ---
a10, a100, a1000 = generar_tres_arreglos()

t10   = medir_tiempo_ordenamiento(a10, bubble_sort)
t100  = medir_tiempo_ordenamiento(a100, bubble_sort)
t1000 = medir_tiempo_ordenamiento(a1000, bubble_sort)

# Salida (esto sí imprime pero NO afecta las mediciones)
print(f"Tiempo arreglo 10  : {t10*1000:.3f} ms")
print(f"Tiempo arreglo 100 : {t100*1000:.3f} ms")
print(f"Tiempo arreglo 1000: {t1000*1000:.3f} ms")
