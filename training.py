def wordNumbers(ph:str):
    ph = input('Ecrivez n\'importe quoi pour savoir quel nombre de mots contient votre message \n')
    ph = ph.replace(" ", "")
    countPh = print(len(ph))
    return countPh

#wordNumbers('')

def monthNumber(n):
    month = ['Janvier', 'Février', 'Mars', 'Avril']
    return month[n -1]

#print (monthNumber(1))

def compteCar(ca:str, ch:str):
    i, tot = 0, 0
    while i < len(ch):
        if ch[i] == ca:
            tot = tot +1
        i = i +1
    return tot

print(compteCar("e", "Cette chaîne est un exemple"))
            
