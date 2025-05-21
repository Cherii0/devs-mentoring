with open("znaki.txt", "r", encoding = "ASCII") as file:
    print(file.readlines())
    # UnicodeDecodeError: 'ascii' codec can't decode byte 0xc4 in position 0: ordinal not in range(128)
    # 0xC4 to system szesnastkowy na dziesietny to ponad 128 zatem nie mozna dopasowac do tablicy ACII
    # parametr encoding pozwala uzyc odpowiednio duzej tablicy jezeli spodziewamy sie np. roznych jezykow


'''

system ASCII powstal na bazie jezyka angielskiego, cyfr 0-9 i znakow specjalnych
stanowi dziesiatkowy zapis 7 bitowego zapisu pozwalajacy na przypasowaniu 128 stanow pamieci do 128 znakow.

następcą systemu ASCII jest UNICODE : pierwsze 128 znaków jest identyczne z tabelą ASCII
zatem mozna UNICODE nazywac rozszerzeniem ASCII. Najpopilarniesza wersja UNICODE jest UTF-8


UTF 8 jest kodowana przez 1 do 6 bajtow. Liczba bajtow w zapisie UTF8 w przeciwienstwie do UTF32 jest zmienna
co pozwala na oszczednosc pamieci. UTF-8 stosuje wzorce bitowe ktore okreslaja czy zaczyna sie litera
1 bajtowa 2 bajtowa itd.


'''
