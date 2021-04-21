
def multiple_recursion(n):
    if n == 0:
        return
    print(n)
    multiple_recursion(n-1)
    print("This executes post first recursive func completion!")
    multiple_recursion(n-1)


multiple_recursion(3)