
arr = [7, 5, 4, 2]


def selection_sort(A):
    for i in range(len(A)-1, 0, -1):
        position_of_largest = 0
        for j in range(1, i+1):
            if A[j] > A[position_of_largest]:
                position_of_largest = j

        A[i], A[position_of_largest] = A[position_of_largest], A[i]


print(arr)
selection_sort(arr)
print(arr)
