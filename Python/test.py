def add_fn(a, b):
    try:
        c = a + b
        print(c)
    except Exception as error:
        print(error)
    finally:
        print("into finally")


if __name__ == '__main__':
    a = 5
    b = 6
    add_fn(5, 6)
