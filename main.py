from math import *
import sys as system

system

# Zad 1. Napisz skrypt, w którym tworzysz listę ulubionych sportów,
# odwróć ją a następnie dodaj mniej lubiane sporty na sam koniec.
print('###########ZAD1############')
lista = ['szachy', 'leagueOfLegends', 'tenisStolowy', 'pilkaNozna', 'koszykowka']
print(lista)
lista.reverse()
print(lista)
lista.append('baseball')
lista.append('hokey')
print(lista)

# Zad 2. Stwórz słownik skrótów powszechnie używanych w gazetach lub artykułach internetowych.
# Jako klucz przyjmij skrót danego słowa, wartość to rozwinięcie tego skrótu.
print('###########ZAD2############')
slownik = {'wg': 'wedlug', 'tzn.': 'to znaczy', 'tzw.': 'tak zwany', 'itp.': 'i tym podobne' }
print(slownik)

# Zad 3. Stwórz słownik z ulubionymi grami komputerowymi.
# Pomyśl, co może być kluczem a co wartością w takim słowniku.
# Policz liczbę elementów w słowniku.
print('###########ZAD3############')
slownik = {'margonem': 'mmorpg', 'leagueOfLegends': 'moba', 'battlefield1': 'fps', 'battlefield5': 'fps', 'metin2': 'mmorpg'}
print(slownik)
print(len(slownik.keys()))

# Zad 4. Napisz skrypt, który pobiera od użytkownika zdanie i liczy wystąpienia litery a.
# Użyj funkcji input
print('###########ZAD4############')
zdanie = input('Podaj zdanie: ')
ile = 0
for i in range (0, len(zdanie)):
    if(zdanie[i] == 'a'):
        ile = ile + 1
print(ile)

# Zad 5. Napisz skrypt gdzie pobierzesz trzy liczby całkowite,
# gdzie wykonasz obliczenia: ab + c.
# Użyj instrukcji readline() i write()).
print('###########ZAD5############')
system.stdout.write("Podaj 3 liczby calkowite: ")
a = int(system.stdin.readline())
b = int(system.stdin.readline())
c = int(system.stdin.readline())
print((pow(a, b) + c))

# Zad 6. Wczytaj trzy liczby całkowite a,b,c i sprawdź,
# która z nich jest największa.
# W zależności od wyniku wyświetl odpowiedni komunikat. Użyj zagnieżdżeń.
print('###########ZAD6############')
a = int(input('Podaj liczbe a: '))
b = int(input('Podaj liczbe b: '))
c = int(input('Podaj liczbe c: '))
if a > b:
    if a > c:
        print('a')
    else:
        print('c')
elif b > c:
        print('b')
else:
    print('c')

# Zad 7. Napisz skrypt, gdzie stworzysz listę składającą się z liczb typu int i float.
# Następnie za pomocą użycia pętli for podnieś każdą liczbę do kwadratu.
print('###########ZAD7############')
lista = [2, 3.4, 12, 1.5, 12, 1.6, 7, 9]
for i in range(0, (len(lista))):
    lista[i] = lista[i] * lista[i]
print(lista)

# Zad 8. Napisz skrypt, który za pomocą pętli while pobiera 10 liczb,
# następnie dodaje do listy tylko parzyste liczby.
print('###########ZAD8############')
lista = []
i = 0
while i != 10:
    a = int(input('Podaj liczbe: '))
    i += 1
    if a % 2 == 0:
        lista.append(a)
print(lista)

# Zad 9. Napisz skrypt, który rysuje następującą literę
# EEEEEE
# E
# EEEEEE
# E
# EEEEEE
# Etapy wykonania ćwiczenia:
# Deklarujemy jedną następującą listę [1,2,3,4,5,6].
# Następnie za pomocą pętli i instrukcji warunkowej wykonujemy odpowiednie działania.
# Trzeba wykorzystać zagnieżdżenia.
print('###########ZAD9############')
lista = [1, 2, 3, 4, 5, 6]
for i in range (1, len(lista)):
    if i % 2 == 1:
        print('EEEEE')
    else:
        print('E')

# Zad. 10
# Napisz skrypt, który liczy pierwiastek z liczby podanej przez
# użytkownika jeśli użytkownik poda wartość ujemną to powinien być wyłapany błąd.
liczba = float(input('Podaj liczbe: '))
try:
     wynik = sqrt(liczba)
     print('Pierwiastek kwadratowy z tej liczby to = ' +str(wynik))
except ValueError:
    print('Ujemna liczba - nie ma rozwiazania w zbiorze liczb rzeczywistych')


