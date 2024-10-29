def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):


    if not (1 <= cilova_pozice[0] <= 8 and 1 <= cilova_pozice[1] <= 8):
        return False


    if cilova_pozice in obsazene_pozice:
        return False

    typ = figurka["typ"]
    pozice = figurka["pozice"]


    if typ == "pěšec":
        if pozice[1] == cilova_pozice[1]:
            if pozice[0] == 2 and cilova_pozice[0] == 4 and (3, pozice[1]) not in obsazene_pozice:
                return True
            elif cilova_pozice[0] == pozice[0] + 1:
                return True

    elif typ == "jezdec":
        if abs(pozice[0] - cilova_pozice[0]) == 2 and abs(pozice[1] - cilova_pozice[1]) == 1:
            return True
        elif abs(pozice[0] - cilova_pozice[0]) == 1 and abs(pozice[1] - cilova_pozice[1]) == 2:
            return True


    elif typ == "věž":
        if pozice[0] == cilova_pozice[0]:  # horizontální tah
            step = 1 if pozice[1] < cilova_pozice[1] else -1
            for col in range(pozice[1] + step, cilova_pozice[1], step):
                if (pozice[0], col) in obsazene_pozice:
                    return False
            return True
        elif pozice[1] == cilova_pozice[1]:  # vertikální tah
            step = 1 if pozice[0] < cilova_pozice[0] else -1
            for row in range(pozice[0] + step, cilova_pozice[0], step):
                if (row, pozice[1]) in obsazene_pozice:
                    return False
            return True


    elif typ == "střelec":
        if abs(pozice[0] - cilova_pozice[0]) == abs(pozice[1] - cilova_pozice[1]):
            step_row = 1 if pozice[0] < cilova_pozice[0] else -1
            step_col = 1 if pozice[1] < cilova_pozice[1] else -1
            for i in range(1, abs(pozice[0] - cilova_pozice[0])):
                if (pozice[0] + i * step_row, pozice[1] + i * step_col) in obsazene_pozice:
                    return False
            return True


    elif typ == "dáma":

        if pozice[0] == cilova_pozice[0] or pozice[1] == cilova_pozice[1]:
            return je_tah_mozny({"typ": "věž", "pozice": pozice}, cilova_pozice, obsazene_pozice)
        elif abs(pozice[0] - cilova_pozice[0]) == abs(pozice[1] - cilova_pozice[1]):
            return je_tah_mozny({"typ": "střelec", "pozice": pozice}, cilova_pozice, obsazene_pozice)


    elif typ == "král":
        if abs(pozice[0] - cilova_pozice[0]) <= 1 and abs(pozice[1] - cilova_pozice[1]) <= 1:
            return True

    return False


if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  # False
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  # False

    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))  # False
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # False
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  # True
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  # False

    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))  # False
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))  # False
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))  # True
