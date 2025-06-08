def example1():
    for i in range( 3 ):
        try:
            x = int(input("Enter a number: "))
            y = int(input("Enter another number: "))
            print(x, '/', y, '=', x / y)
        except ZeroDivisionError:
            print("Division by 0")
        except ValueError:
            print("No number given")





def example2( L ):
    print( "\n\nExample 2" )
    sum = 0
    sumOfPairs = []
    for i in range( len( L ) ):
        try:
            sumOfPairs.append( L[i]+L[i+1] )
        except IndexError:
            print("index out of range")
        except TypeError:
            print("missing convertion from string to int or convertion not possible")

    print( "sumOfPairs = ", sumOfPairs )


def printUpperFile( fileName ):
    try :
        file = open( fileName, "r" )
        for line in file:
            print( line.upper() )
        file.close()
    except FileNotFoundError:
        print("path not found")


def main():
    example1()
    L = [ 10, 3, 5, 6, 9, 3 ]
    example2( L )
    example2( [ 10, 3, 5, 6, "NA", 3 ] )
    try:
        example3( [ 10, 3, 5, 6 ] )
    except NameError:
        print("no function found")

    printUpperFile( "doesNotExistYest.txt" )
    printUpperFile( "./Dessssktop/misspelled.txt" )


if __name__ == "__main__":
    main()
