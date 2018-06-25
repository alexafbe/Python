#A.Fabre
Numbers = {15,12,2,3,8,7,26,11}

def TriBulle (Numbers) :
    switching = True
    n = len(Numbers)

    while switching == True :
        switching = False

        for i in range(n - 1) :
            if Numbers[i] > Numbers[i + 1] :
                switching = True
                Numbers[i],Numbers[i + 1] = Numbers[i + 1],Numbers[i]
    return Numbers
print(Numbers)
