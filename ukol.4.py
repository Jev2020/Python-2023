predvolba = '+420'
text_jedne_zpravy = 180
cena_jedne_zpravy = '3 Kc'


cislo_uzivatele = int(input('Zadej cislo uzivatele:'))
def vyhodnot_cislo(cislo_uzivatele):
    if cislo_uzivatele == 9 or (cislo_uzivatele == 13 and cislo_uzivatele[:4] == predvolba):
        return True
    else:
        return False



text_zpravy = input('Zadej text zpravy:')
def cena_zpravy(zprava):
    if len(zprava) % 180 == 0:
        cena = (len(zprava) // 180) * 3
    else:
        cena = ((len(zprava) // 180) + 1) * 3
    return cena
print(cena_zpravy (text_zpravy))



cislo_uzivatele = int(input('Zadej cislo uzivatele:'))
if vyhodnot_cislo(cislo_uzivatele):
		text_zpravy = input('Zadej text zpravy:')
		print(cena_zpravy(text_zpravy))
else:
		print("spatne cislo")
