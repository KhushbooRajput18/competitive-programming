def print_nto1(n):
    if n == 0:
        return
    print(n, end=" ")
    print_nto1(n - 1)
print_nto1(5)  # Output: 5 4 3 2 1
