#   Napišite program za izračun i ispis trajanja filma u satima i minutama. Vrijeme početka i završetka
#   filma unosi se u satima i minutama (podrazumijeva se da je film započeo i završio u istom danu).

print("Unesite vrijeme pocetka filma: ")
unosPocetakSat = int(input("Sat: "))
unosPocetakMinute = int(input("Minute: "))

print("")

print("Unesite vrijeme kraja filma: ")
unosKrajSat = int(input("Sat: "))
unosKrajMinute = int(input("Minute: "))

print("")

pocetakMinute = unosPocetakSat * 60 + unosPocetakMinute
krajMinute = unosKrajSat * 60 + unosKrajMinute

trajanjeFilmaMinuteTotal = krajMinute - pocetakMinute
trajanjeFilmaSati = trajanjeFilmaMinuteTotal // 60
trajanjeFilmaMinute = trajanjeFilmaMinuteTotal % 60

print(F"Trajanje filma: {trajanjeFilmaSati}h {trajanjeFilmaMinute}min")