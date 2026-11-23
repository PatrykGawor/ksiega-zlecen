from datetime import datetime
def pobierz_cene():
    while True:
        try:
            cena = float(input("Podaj cene uslugi: "))
            if cena >= 0:
                return cena
            print("Cena nie może być ujemna")
        except ValueError:
            print("Podaj poprawna wartosc")
def dodaj_zlecenie(usluga,cena):
    data = datetime.now().strftime("%d.%m.%Y")
    with open("ksiega_zlecen.txt", "a") as plik:
        plik.write(f"{usluga};{cena};{data}\n")

licznik = 0
usluga = input("Podaj nazwe uslugi(koniec kończy):")
while usluga != "koniec":
    cena = pobierz_cene()
    dodaj_zlecenie(usluga,cena)
    licznik = licznik + 1
    usluga = input("Podaj nazwe uslugi(koniec kończy):")
print(f"Dodano {licznik} zleceń")  


