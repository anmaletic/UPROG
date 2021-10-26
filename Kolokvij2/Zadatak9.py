# Da bi student pristupio ispitu mora imati odrađeno svih 14 vježbi i barem 7 od 15 predavanja. 
# Napisati program koji učitava broj odrađenih vježbi i predavanja te ispisuje odgovarajuću poruku 
# 'Student može pristupiti ispitu' /'Student ne može pristupiti ispitu'. 
# Podrazumijeva se da su uneseni podaci iz zadanog raspona

unosVjezbe = int(input("Unesite broj odradenih vjezbi: "))
unosPredavanja = int(input("Unesite broj odradenih predavanja: "))

if(unosVjezbe == 14 and unosPredavanja >= 7):
    print("Student moze pristupiti ispitu.")
else:
    print("Student ne moze pristupiti ispitu.")
    