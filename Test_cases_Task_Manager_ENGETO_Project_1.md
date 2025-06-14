### Funkce: hlavni_menu

**TC01: Výběr platné možnosti z menu**
Popis: Ověření, že volba čísla 1 v hlavním menu správně spustí funkci pridat_ukol.
Vstupní podmínky: Program zobrazuje hlavní menu.
Kroky testu:

1. Spusťte program.
2. Ověřte, že se zobrazuje hlavní menu s nabídkou voleb (např. "1 - Přidat úkol", "2 - Zobrazit úkoly" atd.).
3. Zadejte číslo 1 a potvrďte stisknutím klávesy Enter.
Očekávaný výsledek: Program spustí funkci pridat_ukol().
Skutečný výsledek: Funkce pridat_ukol() byla spuštěna a program zobrazil výzvu k zadání nového úkolu.
Stav: Pass
Poznámky: Tento případ je důležitý, protože ověřuje základní navigaci z hlavního menu a funkčnost jedné z klíčových funkcí programu.

---

**TC02: Neplatná volba v hlavním menu**
Popis: Ověření reakce programu na neplatnou volbu v hlavním menu.
Vstupní podmínky: Program zobrazuje hlavní menu.
Kroky testu:

1. Spusťte program.
2. Zadejte číslo 9 a potvrďte Enter.
Očekávaný výsledek: Program zobrazí hlášku o neplatné volbě a nabídne opět hlavní menu.
Skutečný výsledek: Zobrazila se hláška o neplatné volbě a hlavní menu bylo zobrazeno znovu.
Stav: Pass
Poznámky: Ověřuje správné ošetření chybného vstupu uživatele.

---

**TC03: Ukončení programu volbou 4**
Popis: Ověření, že volba čísla 4 v hlavním menu správně ukončí program.
Vstupní podmínky: Program zobrazuje hlavní menu.
Kroky testu:

1. Spusťte program.
2. Zadejte číslo 4 a potvrďte Enter.
Očekávaný výsledek: Program se ukončí a zobrazí hlášku o ukončení.
Skutečný výsledek: Program se ukončil a zobrazil hlášku "Program ukončen. Nashledanou!".
Stav: Pass
Poznámky: Testuje správné ukončení programu.

---

### Funkce: pridat_ukol

**TC04: Přidání platného úkolu**
Popis: Ověření, že program umožní přidat úkol s platným názvem a popisem.
Vstupní podmínky: Seznam úkolů je prázdný.
Kroky testu:

1. Zvolte v hlavním menu možnost "1 - Přidat úkol".
2. Zadejte název úkolu "Testovací úkol".
3. Zadejte popis úkolu "Popis testovacího úkolu".
Očekávaný výsledek: Úkol je přidán do seznamu a zobrazí se potvrzovací hláška.
Skutečný výsledek: Úkol byl přidán a zobrazila se hláška "Úkol 'Testovací úkol' byl přidán."
Stav: Pass
Poznámky: Ověřuje základní funkčnost přidání úkolu.

---

**TC05: Zadání prázdného názvu úkolu**
Popis: Ověření, že program neumožní přidat úkol s prázdným názvem.
Vstupní podmínky: Seznam úkolů je prázdný.
Kroky testu:

1. Zvolte v hlavním menu možnost "1 - Přidat úkol".
2. Zadejte prázdný název (stiskněte pouze Enter).
3. Zadejte platný popis.
Očekávaný výsledek: Program zobrazí hlášku "Název úkolu nesmí být prázdný." a vyzve k opětovnému zadání.
Skutečný výsledek: Zobrazila se hláška a program vyzval k opětovnému zadání názvu.
Stav: Pass
Poznámky: Ověřuje ošetření chybného vstupu.

---

**TC06: Zadání prázdného popisu úkolu**
Popis: Ověření, že program neumožní přidat úkol s prázdným popisem.
Vstupní podmínky: Seznam úkolů je prázdný.
Kroky testu:

1. Zvolte v hlavním menu možnost "1 - Přidat úkol".
2. Zadejte platný název úkolu.
3. Zadejte prázdný popis (stiskněte pouze Enter).
Očekávaný výsledek: Program zobrazí hlášku "Popis úkolu nesmí být prázdný." a vyzve k opětovnému zadání.
Skutečný výsledek: Zobrazila se hláška a program vyzval k opětovnému zadání popisu.
Stav: Pass
Poznámky: Ověřuje ošetření chybného vstupu.

---

### Funkce: zobrazit_ukoly

**TC07: Zobrazení prázdného seznamu úkolů**
Popis: Ověření, že program správně informuje o prázdném seznamu úkolů.
Vstupní podmínky: Seznam úkolů je prázdný.
Kroky testu:

1. Zvolte v hlavním menu možnost "2 - Zobrazit úkoly".
Očekávaný výsledek: Program zobrazí hlášku "Seznam úkolů je prázdný."
Skutečný výsledek: Zobrazila se hláška "Seznam úkolů je prázdný."
Stav: Pass
Poznámky: Hraniční případ pro prázdný seznam.

---

**TC08: Zobrazení více úkolů**
Popis: Ověření, že program správně vypíše všechny úkoly v seznamu.
Vstupní podmínky: Seznam obsahuje dva úkoly.
Kroky testu:

1. Zvolte v hlavním menu možnost "2 - Zobrazit úkoly".
Očekávaný výsledek: Program vypíše všechny úkoly s jejich názvy a popisy.
Skutečný výsledek: Byly vypsány oba úkoly s názvy a popisy.
Stav: Pass
Poznámky: Testuje výpis více položek.

---

### Funkce: odstranit_ukol

**TC09: Odstranění existujícího úkolu**
Popis: Ověření, že program umožní odstranit existující úkol podle čísla.
Vstupní podmínky: Seznam obsahuje jeden úkol.
Kroky testu:

1. Zvolte v hlavním menu možnost "3 - Odstranit úkol".
2. Zadejte číslo 1 a potvrďte Enter.
Očekávaný výsledek: Úkol je odstraněn a zobrazí se potvrzovací hláška.
Skutečný výsledek: Úkol byl odstraněn a zobrazila se hláška o odstranění.
Stav: Pass
Poznámky: Ověřuje funkčnost mazání.

---

**TC10: Zadání neplatného čísla úkolu**
Popis: Ověření, že program správně reaguje na zadání neexistujícího čísla úkolu.
Vstupní podmínky: Seznam obsahuje jeden úkol.
Kroky testu:

1. Zvolte v hlavním menu možnost "3 - Odstranit úkol".
2. Zadejte číslo 5 a potvrďte Enter.
Očekávaný výsledek: Program zobrazí hlášku o neplatném čísle úkolu a vyzve k opětovnému zadání.
Skutečný výsledek: Zobrazila se hláška o neplatném čísle úkolu a program vyzval k opětovnému zadání.
Stav: Pass
Poznámky: Ověřuje ošetření chybného vstupu.

---

**TC11: Odstranění z prázdného seznamu**
Popis: Ověření, že program správně reaguje na pokus o odstranění úkolu z prázdného seznamu.
Vstupní podmínky: Seznam úkolů je prázdný.
Kroky testu:

1. Zvolte v hlavním menu možnost "3 - Odstranit úkol".
Očekávaný výsledek: Program zobrazí hlášku "Seznam úkolů je prázdný. Není co odstraňovat."
Skutečný výsledek: Zobrazila se hláška o prázdném seznamu.
Stav: Pass
Poznámky: Hraniční případ.

---

**TC12: Zadání nečíselné hodnoty při mazání úkolu**
Popis: Ověření, že program správně reaguje na zadání nečíselného vstupu při výběru úkolu k odstranění.
Vstupní podmínky: Seznam obsahuje dva úkoly.
Kroky testu:

1. Zvolte v hlavním menu možnost "3 - Odstranit úkol".
2. Zadejte text "abc" místo čísla a potvrďte Enter.
Očekávaný výsledek: Program zobrazí hlášku "Zadejte prosím platné číslo." a vyzve k opětovnému zadání.
Skutečný výsledek: Zobrazila se hláška o neplatném vstupu a program vyzval k opětovnému zadání.
Stav: Pass
Poznámky: Ověřuje ošetření chybného vstupu.

---
