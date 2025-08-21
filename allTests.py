import random
import subprocess
import threading
import time

def gen_array(arr_size):
    arr = []
    for i in range(arr_size):
        arr.append(random.randint(0, 1000))
    return arr

def bubble_sort(arr):
    arr_size = len(arr)
    for i in range(0, (arr_size-1)):
        for j in range(0, (arr_size-i-1)):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr

def bubble_sort_ChatGPT(arr, reverse=False):
    arr_size = len(arr)
    while arr_size > 1:
        last_swap = 0
        for i in range(1, arr_size):
            if (not reverse and arr[i-1] > arr[i]) or (reverse and arr[i-1] < arr[i]):
                arr[i-1], arr[i] = arr[i], arr[i-1]
                last_swap = i
        if last_swap == 0:
            break
        arr_size = last_swap
    return arr

def bubble_sort_Gemini(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def bubble_sort_Deepseek(arr):
    n = len(arr)
    left = 0
    right = n - 1
    while left < right:
        swapped = False
        # Forward pass (left to right)
        for i in range(left, right):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
                last_swap = i
        if not swapped:
            break
        right = last_swap
        # Backward pass (right to left)
        swapped = False
        for i in range(right, left, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swapped = True
                last_swap = i
        if not swapped:
            break
        left = last_swap
    return arr

def bubble_sort_Meta(arr):
    n = len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def test_sort(arr_size, sorter, iterations):
    times = []
    for i in range(iterations):
        arr = gen_array(arr_size)
        start_time = time.time()
        temp = sorter(arr)
        if temp != sorted(arr):
            print(f"Error: Sorting failed for array size {arr_size} on iteration {i+1} for sorter {sorter}")
        times.append(time.time() - start_time)
    return times

def average(times):
    return (sum(times) / len(times)) * 1000

def print_wait_message():
    subprocess.run("clear")
    while processing.is_set():
        print("running tests")
        time.sleep(1)
        subprocess.run("clear")
        print("running tests.")
        time.sleep(1)
        subprocess.run("clear")
        print("running tests..")
        time.sleep(1)
        subprocess.run("clear")
        print("running tests...")
        time.sleep(1)
        subprocess.run("clear")

if __name__ == "__main__":
    iterations = int(input("Input the number of iterations for testing: "))

    processing = threading.Event()
    processing.set()

    thread = threading.Thread(target=print_wait_message)
    thread.start()

    times10bubble = test_sort(10, bubble_sort, iterations)
    times100bubble = test_sort(100, bubble_sort, iterations)
    times1000bubble = test_sort(1000, bubble_sort, iterations)
    
    times10ChatGPT = test_sort(10, bubble_sort_ChatGPT, iterations)
    times100ChatGPT = test_sort(100, bubble_sort_ChatGPT, iterations)
    times1000ChatGPT = test_sort(1000, bubble_sort_ChatGPT, iterations)

    times10Gemini = test_sort(10, bubble_sort_Gemini, iterations)
    times100Gemini = test_sort(100, bubble_sort_Gemini, iterations)
    times1000Gemini = test_sort(1000, bubble_sort_Gemini, iterations)

    times10Deepseek = test_sort(10, bubble_sort_Deepseek, iterations)
    times100Deepseek = test_sort(100, bubble_sort_Deepseek, iterations)
    times1000Deepseek = test_sort(1000, bubble_sort_Deepseek, iterations)

    times10Meta = test_sort(10, bubble_sort_Meta, iterations)
    times100Meta = test_sort(100, bubble_sort_Meta, iterations)
    times1000Meta = test_sort(1000, bubble_sort_Meta, iterations)

    processing.clear()
    thread.join()

    average10 = {'Standard Bubble': average(times10bubble),
                 'ChatGPT': average(times10ChatGPT),
                 'Gemini': average(times10Gemini),
                 'Deepseek': average(times10Deepseek),
                 'Meta': average(times10Meta)}
    
    average10AI = {'ChatGPT': average(times10ChatGPT),
                   'Gemini': average(times10Gemini),
                   'Deepseek': average(times10Deepseek),
                   'Meta': average(times10Meta)}
    
    average100 = {'Standard Bubble': average(times100bubble),
                  'ChatGPT': average(times100ChatGPT),
                  'Gemini': average(times100Gemini),
                  'Deepseek': average(times100Deepseek),
                  'Meta': average(times100Meta)}
    
    average100AI = {'ChatGPT': average(times100ChatGPT),
                    'Gemini': average(times100Gemini),
                    'Deepseek': average(times100Deepseek),
                    'Meta': average(times100Meta)}
    
    average1000 = {'Standard Bubble': average(times1000bubble),
                   'ChatGPT': average(times1000ChatGPT),
                   'Gemini': average(times1000Gemini),
                   'Deepseek': average(times1000Deepseek),
                   'Meta': average(times1000Meta)}
    
    average1000AI = {'ChatGPT': average(times1000ChatGPT),
                     'Gemini': average(times1000Gemini),
                     'Deepseek': average(times1000Deepseek),
                     'Meta': average(times1000Meta)}
    
    print("Results:\n")
    print(f"{'Algorithm':<20} | {'Time on array 10':>20} | {'Time on array 100':>20} | {'Time on array 1000':>20}")
    print("-" * 21 + "|" + f"{'-' * 22}|" * 2 + "-" * 21)
    print(f"{'Standard Bubble':<20} | {average10['Standard Bubble']:>17.6} ms | {average100['Standard Bubble']:>17.6} ms | {average1000['Standard Bubble']:>17.6} ms")
    print(f"{'ChatGPT':<20} | {average10['ChatGPT']:>17.6} ms | {average100['ChatGPT']:>17.6} ms | {average1000['ChatGPT']:>17.6} ms")
    print(f"{'Gemini':<20} | {average10['Gemini']:>17.6} ms | {average100['Gemini']:>17.6} ms | {average1000['Gemini']:>17.6} ms")
    print(f"{'Deepseek':<20} | {average10['Deepseek']:>17.6} ms | {average100['Deepseek']:>17.6} ms | {average1000['Deepseek']:>17.6} ms")
    print(f"{'Meta':<20} | {average10['Meta']:>17.6} ms | {average100['Meta']:>17.6} ms | {average1000['Meta']:>17.6} ms")
    print(" " * 21 + "|" + f"{' ' * 22}|" * 2 + " " * 21)
    print(f"{'Slowest Algorithm':<20} | {max(average10, key=average10.get):>20} | {max(average100, key=average100.get):>20} | {max(average1000, key=average1000.get):>20}")
    print(f"{'Slowest AI':<20} | {max(average10AI, key=average10AI.get):>20} | {max(average100AI, key=average100AI.get):>20} | {max(average1000AI, key=average1000AI.get):>20}")
    print(f"{'Fastest Algorithm':<20} | {min(average10, key=average10.get):>20} | {min(average100, key=average100.get):>20} | {min(average1000, key=average1000.get):>20}")
