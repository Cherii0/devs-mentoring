def fizz_buzz(n):

    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'

    if n % 3 == 0 :
        return "Fizz"
    elif n % 5 == 0 :
        return "Buzz"

    else:
        return n




print(fizz_buzz(int(input("podaj numer ...  "))))
