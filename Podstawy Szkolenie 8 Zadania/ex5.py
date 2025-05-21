with open("przyklad_zad_5.txt", encoding="utf-8") as plik:
    print(plik.tell())
    plik.seek(43)
    print(plik.read(5))

# wniosek : znaki z poza ASCII patrzac z pozycji seek zajmuja dwie pozycje, dlatego jezeli ustawimy
# plik.seek() na znaku nastepujacym po np. 'ę' to
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0x99 in position 0: invalid start byte.
# w tekscie z zadania pozycja 43 jest zgodna z wynikiem jezeli uznamy ze znaki polskie sa liczone za dwa
