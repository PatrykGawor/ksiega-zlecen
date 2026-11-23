ceny = []
najdrozsza = 0
nazwa = ""
data_najdrozszej = ""
try:
    with open("ksiega_zlecen.txt", "r") as plik:
        for linia in plik:
            try:
                usluga, cena, data = linia.strip().split(";")
                cena = float(cena)
                ceny.append(cena)
                if cena > najdrozsza:
                    najdrozsza = cena
                    nazwa = usluga
                    data_najdrozszej = data
            except ValueError:
                print(f"Pomijam błędna linie: {linia.strip()}")
except FileNotFoundError:
    print("Brak pliku")
if len(ceny) > 0:
    print(f"Liczba zlecen:{len(ceny)}")
    print(f"Suma:{round(sum(ceny),2)}")
    print(f"Najdroższe zlecenie: {nazwa} za {najdrozsza} zł  ({data})")      
else:
    print("Brak zleceń do wyświetlenia")              