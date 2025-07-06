ukoly = []

def hlavni_menu():
    while True:
        print("\nSprávce úkolů - Hlavní menu")
        print("1 - Přidat nový úkol")
        print("2 - Zobrazit všechny úkoly")
        print("3 - Odstranit úkol")
        print("4 - Konec programu")
        volba = input("Zadejte číslo volby: ")
        if volba == "1":
            while True:
                nazev = input("Zadejte název úkolu: ").strip()
                popis = input("Zadejte popis úkolu: ").strip()
                try:
                    pridat_ukol(ukoly, nazev, popis)
                    break
                except ValueError as e:
                    print(e)
        elif volba == "2":
            zobrazit_ukoly(ukoly)
        elif volba == "3":
            zobrazit_ukoly(ukoly)
            if not ukoly:
                continue
            while True:
                cislo = input("Zadejte číslo úkolu, který chcete odstranit: ")
                try:
                    cislo_int = int(cislo)
                    odstranit_ukol(ukoly, cislo_int)
                    break
                except ValueError:
                    print("Zadejte prosím platné číslo.")
                except IndexError as e:
                    print(e)
        elif volba == "4":
            print("Program ukončen.")
            break
        else:
            print("Neplatná volba. Zkuste to prosím znovu.")

def pridat_ukol(ukoly, nazev, popis):
    if not nazev:
        raise ValueError("Název úkolu nesmí být prázdný.")
    if not popis:
        raise ValueError("Popis úkolu nesmí být prázdný.")
    ukoly.append({"nazev": nazev, "popis": popis})
    print(f"Úkol '{nazev}' byl přidán.")

def zobrazit_ukoly(ukoly):
    if not ukoly:
        print("Seznam úkolů je prázdný.")
    else:
        print("\nSeznam úkolů: ")
        for idx, ukol in enumerate(ukoly, 1):
            print(f"{idx}. {ukol['nazev']} - {ukol['popis']}")

def odstranit_ukol(ukoly, cislo):
    if not ukoly:
        print("Seznam úkolů je prázdný.")
        return
    if not (1 <= cislo <= len(ukoly)):
        raise IndexError("Neplatné číslo úkolu.")
    odebrany = ukoly.pop(cislo - 1)
    print(f"Úkol '{odebrany['nazev']}' byl odstraněn.")

if __name__ == "__main__":
    hlavni_menu()
