# first.py

def sudy_nebo_lichy(cislo):
    if cislo % 2 == 0:
        print(f"Číslo {cislo} je sudé")
    else:
        print(f"Číslo {cislo} je liché")

# Volání funkce pro dvě pevná čísla
sudy_nebo_lichy(5)
sudy_nebo_lichy(1000000)

# Získání čísel od uživatele
while True:
    vstup = input("Zadejte číslo (nebo 'konec' pro ukončení): ")
    if vstup.lower() == 'konec':
        break
    try:
        cislo = int(vstup)
        sudy_nebo_lichy(cislo)
    except ValueError:
        print("Zadejte platné číslo!")