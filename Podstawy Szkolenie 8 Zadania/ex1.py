'''

sciezka bezwzgledna okresla lokalizacje pliku bez wzgledu na to gdzie plik .py sie znajduje
rozpoczyna sie od C:\ czyli od 'korzenia
czyli jezeli chce odczytac plik przyklad.txt z uzyciem sciezki bezezglednej uzyje zapisu
file_path = "C:\Users\zygmu\PycharmProjects\devs-mentoring\10 Podstawy Szkolenie 8 Zadania\przyklad.txt"

sciezka wzgledna okresla jak nalezy poruszac sie po katalogach zeby trafic do pliku z miejsca wywolania
jezeli np. chce odczytac plik wzglednie to uzyje zapisue file_path = "../katalog/plik.txt"

..\ oznacza wyjscie z katalogu
\katalog - oznacza wejscie do katalogu 'katalog'

sciezka wzgledna nie rozpoczyna sie od C:\ czyli od 'korzenia

wzgledne sciezki

\outer_dir\innedr_dir\przyklad.txt
\katalog\przyklad.txt

bezwzgledne sciezki

C:\outer_dir\inner_dir\przyklad.txt
C:\przyklad.txt

'''

