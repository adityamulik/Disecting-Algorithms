
arr = [10, 4, 43, 5, 57, 91, 45, 9, 7]

# for i in range(8, 0, -1):
#     print(i)

def selection_sort(A):
    for i in range(len(A)-1, 0, -1):
        position_of_largest = 0
        print("Post of i: ", i)
        print("Og Pos: ", position_of_largest)
        for j in range(1, i+1):
            print("Post of j: ", j)
            if A[j] > A[position_of_largest]:
                position_of_largest = j
                print('New Pos: ', position_of_largest)

        print("Before Swap Index Loc: ", i, position_of_largest)
        print("Before Swap: ", A[i], A[position_of_largest])        
        A[i], A[position_of_largest] = A[position_of_largest], A[i]
        print("After Swap Index Loc: ", position_of_largest, i)
        print("After Swap: ", A[i], A[position_of_largest])      
        print("Final Array: ", A)  


print(arr)
selection_sort(arr)
print(arr)
