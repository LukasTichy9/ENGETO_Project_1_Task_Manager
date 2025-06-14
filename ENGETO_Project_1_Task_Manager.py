ukoly = []

def hlavni_menu():
    while True:
        print("\nSprávce úkolů - Hlavní menu")
        print("1 - Přidat nový úkol")
        print("2 - Zobrazit včechny úkoly")
        print("3 - Odstranit úkol")
        print("4 - Konec programu")
        volba = input("Zadejte číslo volby: ")
        if volba == "1":
            pridat_ukol()
        elif volba == "2":
            zobrazit_ukoly()
        elif volba == "3":
            odstranit_ukol()
        elif volba == "4":
            print("Program ukončen.")
            break
        else:
            print("Neplatná volba. Zkuste to prosím znovu.")

def pridat_ukol():
    global ukoly
    while True:
        nazev = input("Zadejte název úkolu: ").strip()
        if not nazev:
            print("Název úkolu nesmí být prázdný.")
            continue
        popis = input("Zadejte popis úkolu: ").strip()
        if not popis:
            print("Popis úkolu nesmí být prázdný.")
            continue
        ukoly.append({"nazev": nazev, "popis": popis})
        print(f"Úkol '{nazev}' byl přidán.")
        break

def zobrazit_ukoly():
    if not ukoly:
        print("Seznam úkolů je prázdný.")
    else:
        print("\nSeznam úkolů: ")
        for idx, ukol in enumerate(ukoly, 1):
            print(f"{idx}. {ukol['nazev']} - {ukol['popis']}")

def odstranit_ukol():
    global ukoly
    if not ukoly:
        print("Seznam úkolů je prázdný.")
        return
    zobrazit_ukoly()
    while True:
        try:
            cislo = int(input("Zadejte číslo úkolu, který chcete odstranit: "))
            if 1 <= cislo <= len(ukoly):
                odebrany = ukoly.pop(cislo - 1)
                print(f"Úkol '{odebrany['nazev']}' byl odstraněn.")
                break
            else:
                print("Neplatné číslo úkolu. Zkuste to znovu.")
        except ValueError:
            print("Zadejte prosím platné číslo.")

if __name__ == "__main__":
    hlavni_menu()