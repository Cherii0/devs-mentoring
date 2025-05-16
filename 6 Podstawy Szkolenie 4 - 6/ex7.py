while True:

    n = None
    inputed_num = input("provide number... ")
    try:
        n = int(inputed_num)
    except ValueError:
        print("wrong number")

    if n is None:
        continue

    if n < 0:
        n = abs(n)
    elif n >= 0:
        pass
    else:
        print("unrecognized number")

    print(n)
