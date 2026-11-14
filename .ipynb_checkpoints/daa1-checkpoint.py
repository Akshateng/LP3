# Non-Recursive Method
def iterative(n):
    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c


# Recursive Method
def recursive(n):
    if n <= 1:
        return n
    return recursive(n-1) + recursive(n-2)


n = int(input("Enter number of terms: "))

print("Non-Recursive:")
iterative(n)

print("\nRecursive:")
for i in range(n):
    print(recursive(i), end=" ")
