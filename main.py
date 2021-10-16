import sys

def index(i, p, j): #valoarea din matrice
    c = chr(j + ord('A')) #coloana
    t = p[0:i] + c #stringul cu urmatorul caracter
    for k in range(0, i): #pentru a gasi substringul
        if (t[k:len(t)] == p[0:i - k + 1]):
            return len(t) - k #lungimea substringului
    if (c == p[0]): #daca e prima litera
        return 1
    return 0

def compute_delta(p): #creeaza matricea 
    row = len(p) #numarul de linii
    collumn = ord('Z') - ord('A') + 1 #numarul de coloane
    matrix = [] #matricea
    for i in range(0, row): #fiecare linie
        matrix.append([]) #adaug o linie
        for j in range(0, collumn): #adaug pentru fiecare coloana valoarea
            matrix[i].append(index(i, p.replace('\n', ''), j))
    return matrix

def automat(p, t):
    res = [] #lista cu indecsi
    q = 0 #starea initiala
    f = len(p) - 1 #starea finala
    delta = compute_delta(p) #calculez delta
    for i in range(0, len(t) - 1): #pentru fiecare caracter din text
        q = delta[q][ord(t[i]) - ord('A')] #starea urmatoare
        if q == f: #daca sunt in stare finala
            res.append(i - f + 1) #adaug indexul la rezultat
    return res

def main(inFile, outFile):
    file1 = open(inFile, "r") #fisierul de input
    file2 = open(outFile, "w") #fisierul de output
    p = file1.readline() #citesc pattern-l
    t = file1.readline() #citesc textul
    res = str(automat(p, t)) #rezolv problema
    if (len(res) > 2): #daca exista rezultat il scriu
        res = res.replace(',', '').replace('[', '').replace(']', '') + '  '
        file2.write(res) #scriu rezultatul in fisier
    file1.close() #inchid fisierele
    file2.close()

if (len(sys.argv) < 3): #daca nu exista argumentele
    print("Use python3 main.py inputFile outputFile")
else: main(sys.argv[1], sys.argv[2]) #apelez main
