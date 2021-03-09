
def selected_sort(A):
    for i in range(len(A) - 1): # 0 (0,1,2,3,4)
        print("Index i: ", i)
        min_position = i # 0
        print("min_pos: ", min_position) # 0
        for j in range(i, len(A)): # 0 in (0,6)...0,1,2,3,4,5
            print("Index j: ", j)
            if A[j] < A[min_position]: # A[0] < A[0] 5 < 5 false
                min_position = j # false
                print("min_pos after comparision: ", min_position)
        # temp = A[i] # temp = A[0] = 5
        # A[i] = A[min_position] # A[5] = 2
        # A[min_position] = temp # 5
        print("For Index: ", i)
        print("Before Swap: ", A[i], A[min_position])
        A[i], A[min_position] = A[min_position], A[i]
        print(A) # 5


arr = [6, 3, 8, 5, 7, 2, 9]
selected_sort(arr)