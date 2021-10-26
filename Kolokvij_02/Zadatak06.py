# Napišite program za unos bodova iz dva kolokvija. Raspon bodova je 0-100. Ako je uneseni 
# broj izvan raspona napisati odgovarajuću poruku i završiti program. 
# Ako iz svakog kolokvija student ima barem 40 bodova i prosječna vrijednost osvojenih 
# bodova je barem 50 napišite ''Prolaz'' inače napišite ''Pad''. Koristite if…elif…else strukture 
# grananja i logičke operatore or/and.

msgVanRaspona = "Uneseni broj nije unutar raspona."

unosKolokvij1 = int(input("Unesite bodove iz prvog kolokvija (0-100): "))
if(unosKolokvij1 < 0 or unosKolokvij1 > 100):
    print(msgVanRaspona)
else:
    unosKolokvij2 = int(input("Unesite bodove iz drugog kolokvija (0-100): "))
    if(unosKolokvij2 < 0 or unosKolokvij2 > 100):
        print(msgVanRaspona)
    elif(unosKolokvij1 >= 40 and unosKolokvij2 >= 40 and (unosKolokvij1 + unosKolokvij2) // 2 >= 50):
        print("Prolaz")
    else:
        print("Pad")
