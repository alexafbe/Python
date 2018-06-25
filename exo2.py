#A.Fabre
import string

text = "aaabbhhdddcccjjhhggffqqllkki iooouuurrrrppppqqqooo okkkllllooooppprrrr tttt"
D = {}
DFq = {}

n = len (text)
Letters = string.ascii_lowercase
for L in Letters :
    if text.count(L) != 0 :
        D[L] = text.count(L)
        DFq[L] = (text.count(L) * 100) / n
print("Nombre d'occurences par lettre : ", D)
print("Fréquence des occurences (%) : ", DFq)
