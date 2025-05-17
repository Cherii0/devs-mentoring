


def main():
    A = [i for i in range(1, 10)]
    B = [i for i in range(11, 20)]

    while True:

        for elem in A:
            if elem in B:
                print("sa wspolne elementy")
                return

        print("nie ma wspolnych elementow")
        return




if __name__ == '__main__':
    main()

