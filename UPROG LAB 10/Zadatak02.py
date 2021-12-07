# Zadatak 2
# # Tekst se može komprimirati tako da se uzastopno pojavljivanje nekog znaka u tekstu zamijeni znakom i 
# brojem koji kaže koliko se puta taj znak uzastopno ponavlja. Napisati program koji će dekomprimirati 
# uneseni komprimirani tekst. Pretpostavlja se da je u unesenom tekstu iza svakog znaka 
# jednoznamenkasti potitivni broj. Tekst se unosi u funkciji main, a funkcija dekompres vraća 
# dekompresirani tekst.
# Npr. ako je uneseni tekst a3b4c2 ispisat će se aaabbbbcc.

def dekompres(tekst):
    temp_tekst = ""
    for i in range(len(tekst)):
        if i % 2 == 0:
            znak = tekst[i]
        else:
            znak = znak * int(tekst[i])
            temp_tekst += znak
    return temp_tekst

def main():
    unosTekst = input("Unesite komprimirani tekst: ")    
    print(dekompres(unosTekst))

main()