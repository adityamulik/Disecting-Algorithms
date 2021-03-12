
# arr_ints = [10, 4, 43, 5, 57, 91, 45, 9, 7]
arr_ints = [5, 2, 3, 4, 5]


def bubble_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print(arr)
        print(f'Iteration {i} completed!')


# print(arr_ints)
bubble_sort(arr_ints)
print(f"Output: {arr_ints}")