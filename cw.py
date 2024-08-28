def foo(a: int, b: list) -> list:
    a = 2
    b[0] = 2
    b = [3, 2, 1]
    return b

a = 5
b = [1, 2, 3]

print(foo(a, b))
print(a)
print(b)
