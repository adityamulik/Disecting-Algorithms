
# def run(no):
#     if no == 0:
#         return
#
#     run(no - 1)
#     print(no)


# def run(no):
#     if no == 0:
#         return
#     print("UL", no)
#     run(no-1)
#     print("LL", no)


def star(no):
    if no == 0:
        return
    star(no-1)
    print("*" * no)


# run(3)
star(10)