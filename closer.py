def outer(x):
    def inner():
        return x * 10
    return inner()

func = outer(10)
print(func)

