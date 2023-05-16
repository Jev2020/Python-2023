class Auto:

    def __init__(self, registracni_znacka, typ_vozidla, najete_km):
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupne = True

    def get_info(self):
        return f"{self.registracni_znacka}, {self.typ_vozidla}"

    def pujc_auto(self):
        if self.dostupne:
            text = "Potvrzuji zapůjčení vozidla"
        else:
            text = "Vozidlo není k dispozici"
        return text

Peugeot= Auto("4A2 3020", "Peugeot 403 Cabrio", "47534")
Skoda = Auto("1P3 4747", "Škoda Octavia", "41253")

znacka = input("Jakou značku si přejete půjčit? Peugeot nedo Skoda?")

#print(Peugeot.get_info())
#print(Peugeot.pujc_auto())

#nebo

#print(Skoda.get_info())
#print(Skoda.pujc_auto())
