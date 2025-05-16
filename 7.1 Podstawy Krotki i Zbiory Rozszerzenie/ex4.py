n = int(input("podaj granice ciagu : "))

A = set([i for i in range(0, n, 2)])
B = set([i for i in range(0, n, 2)  if i % 3 == 2])
C = A.union(B) # polaczenie zbiorow
D  = A.intersection(B)  # czesc wspolna zbiorow - intersekcja
E = A.difference(B) # elementy ze zbioru A pozostale po odjeciu elementow zbioru B
F = B.symmetric_difference(A) # polaczenie roznic z obu zbiorow, czyli elementy wystepujace dla A lacza sie z elementami
# wystepujacymi dla B i to jest ich wspolny set

print("zbior A", " liczebnosc : ", len(A), "zawartosc zbioru : ", A)
print("zbior B" , " liczebnosc : ", len(B), "zawartosc zbioru : ", B)
print("zbior C" , " liczebnosc : ", len(C), "zawartosc zbioru : ", C)
print("zbior D" , " liczebnosc : ", len(D), "zawartosc zbioru : ", D)
print("zbior E",  " liczebnosc : ", len(E), "zawartosc zbioru : ", E)
print("zbior F",  " liczebnosc : ", len(F), "zawartosc zbioru : ", F)

print(B.issubset(A))
