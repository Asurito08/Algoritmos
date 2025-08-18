def bubbleSort(A, n):
    for i in range(0, (n-1)):
        for j in range(0, (n-i-1)):
            if A[j] > A[j+1]:
                temp = A[j]
                A[j] = A[j+1]
                A[j+1] = temp
    return A


