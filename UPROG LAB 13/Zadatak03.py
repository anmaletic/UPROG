# Zadatak 3
# Stvorite dvije liste – u prvoj listi su metode i funkcije koje smo učili vezano uz stringove, u drugoj listi su 
# metode i funkcije koje smo učili vezano uz liste. Ispišite koja od njih ima više elemenata (ili je broj elemenata 
# jednak). Potom konstruirajte novu listu koja će za elemente imati samo one metode koje su zajedničke 
# objema listama
# ( Lzajednickih = [………… for i in…..if…..]).
# Ispišite elemente sve tri liste.

listaS = ["clear", "append", "count", "index", "insert", "remove", "pop", "sort"]
listaL = ["find", "format", "index", "lower", "replace", "split", "upper"]

listaZ = list(item for item in listaS if item in listaL)

print(listaS)
print(listaL)
print(listaZ)