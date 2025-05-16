import math

def classification(BMI):

    classification_message = ""

    if BMI < 18.5:
        classification_message = "niedowaga"
    elif BMI >= 18.5 and BMI <= 24:
        classification_message =  "waga normalna"
    elif BMI > 24 and BMI <= 26.5:
        classification_message =  "lekka nadwaga"
    else:
        if BMI < 30:
            classification_message = "nadwaga"
        elif BMI >= 30 and BMI <= 35:
            classification_message = "nadwaga i otyłosc 1 stopnia"
        elif BMI > 30 and BMI <= 40:
            classification_message = "nadwaga i otyłosc 2 stopnia"
        else:
            classification_message = "nadwaga i otyłosc 3 stopnia"

    return classification_message

while True:
    weight = int(input("podaj wage w kg : "))
    height = float(int(input("podaj wzrost w cm: ")) / 100)
    BMI = weight / (math.pow(height, 2))
    print(classification(BMI))
