# By adding a flag swapped = 1

# arr_ints = [10, 4, 43, 5, 57, 91, 45, 9, 7]

arr_ints = [1, 2, 3, 4, 5]

# arr_ints = [4, 5, 7, 9, 10, 43, 45, 57, 91]


def bubble_sort(arr):
    swapped = 1
    for i in range(len(arr)-1, 0, -1):
        if(swapped == 0):
            print(swapped)
            return
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = 1
                print(arr)
        print(f'Iteration {i} completed!')


# print(arr_ints)
bubble_sort(arr_ints)
print(f"Output: {arr_ints}")