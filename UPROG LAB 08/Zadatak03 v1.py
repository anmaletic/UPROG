# Napišite program za unos imena i prezimena (jedna varijabla) te adrese stanovanja za 5 
# studenata. Unos imena i prezimena je obavezan, ako se ne unese, tražiti ponovan upis. Unos 
# adrese nije obavezan. Podatci se unose u main funkciji, te se šalju na ispis funkciji ispis. Funkcija 
# ispis može se pozvati na dva načina – sa jednim ili sa dva argumenta. Ako se podatak o adresi ne 
# pošalje funkciji, vrijednost njenog drugog parametra će biti ‘Adresa će biti naknadno upisana’. 

def ispis(p_ip, p_add = "Adresa će biti naknadno upisana."):
    print()
    print(F"Ime i prezime: {p_ip}")
    print(F"Adresa: {p_add}")
    print()


def main():
    for i in range(5):  
        unosImePrezime = ""      
        while unosImePrezime == "":            
            unosImePrezime = input(F"Unesite ime i prezime {i+1}. studenta: ")

        unosAdresa = input(F"Unesite adresu {i+1}. studenta:")

        if(unosAdresa == ""):
            ispis(unosImePrezime)
        else:
            ispis(unosImePrezime, unosAdresa)

main()