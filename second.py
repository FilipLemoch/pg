def cislo_text(cislo):
    jednotky = ["nula", "jedna", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět"]
    desitky = ["", "deset", "dvacet", "třicet", "čtyřicet", "padesát", "šedesát", "sedmdesát", "osmdesát", "devadesát"]
    teens = ["jedenáct", "dvanáct", "třináct", "čtrnáct", "patnáct", "šestnáct", "sedmnáct", "osmnáct", "devatenáct"]
    
    cislo = int(cislo)

    if cislo == 100:
        return "sto"
    
    if cislo < 10:
        return jednotky[cislo]
    
    if 10 < cislo < 20:
        return teens[cislo - 11]
    
    if cislo % 10 == 0:
        return desitky[cislo // 10]
    
    return desitky[cislo // 10] + " " + jednotky[cislo % 10]

if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)
