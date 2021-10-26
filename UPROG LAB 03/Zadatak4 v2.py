# Kupit ćete košulju samo ako cijena nije veća od 100kn, broj je 42 i boja je bijela ili zelena. Nakon unesenih 
# vrijednosti ispisuje se poruka ''Kupujem'' ako su svi uvjeti zadovoljeni, u suprotnom se ispisuje poruka ''Ne 
# kupujem''. Napišite složeni uvjet koristeći logičke operatore and i or.
# Obavezno provjerite radi li složeni logički uvjet dobro na sve kombinacije istinitosti relacijskih izraza.

unosCijena = float(input("Unesite cijenu: "))
unosBroj = int(input("Unesite broj: "))
unosBoja = input("Unesite boju: ")

if(unosCijena <= 100 and unosBroj == 42 and (unosBoja == "bijela" or unosBoja == "zelena")):
    print("Kupujem")
else:
    print("Ne kupujem")
