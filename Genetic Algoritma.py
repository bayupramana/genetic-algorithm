import random
import math

def generateChromosome():
    cromosom = []
    for i in range(6):
        cromosom.append(random.randint(0, 1))
    return cromosom

def decode(cromosom):
    populasi = len(cromosom) // 2
    c1 = cromosom[:populasi]
    c2 = cromosom[populasi:]
    pembagi = 0
    pengali1 = 0
    pengali2 = 0
    for i in range(populasi):
        pembagi += math.pow(2, -i-1)
        pengali1 += c1[i] * math.pow(2, -i-1)
        pengali2 += c2[i] * math.pow(2, -i-1)
    x1 = -3 + ((6)/pembagi) * pengali1
    x2 = -2 + (4/pembagi) * pengali2
    return (x1, x2)

def f(x1, x2):
    return  (4-2.1*math.pow(x1, 2) + (math.pow(x1, 4)/3))*math.pow(x1, 2) + (x1 * x2) + (-4 + 4 * x2 * x2)*x2*x2

def fitness(c):
    x1, x2 = decode(c)
    h = f(x1, x2)
    return 1/(h+5)

def tournament(populasi, k):
    kandidat = []
    for i in range(k):
        kandidat.append(random.randint(0, len(populasi)-1))
    best = kandidat[0]
    for ind in kandidat:
        fit = fitness(populasi[ind])
        if fit > fitness(populasi[best]):
            best = ind
    return populasi[best]

def crossover(p1, p2, pc):
    if pc > random.random():
        titik = random.randint(1, len(p1)-2)
        for i in range(titik):
            temp = p1[i]
            p1[i] = p2[i]
            p2[i] = temp
    return p1, p2

def mutasi(ind, pm):
    if random.random() < pm:
        titik = random.randint(0, len(ind) - 1)
        ind[titik] = 1 if ind[titik] == 0 else 0
    return ind

def cariTerburuk(populasi):
    buruk = 0
    for i in range(len(populasi)):
        if fitness(populasi[i]) < fitness(populasi[buruk]):
            buruk = i
    return buruk

def cariTerbaik(populasi):
    best = 0
    for i in range(len(populasi)):
        if fitness(populasi[i]) > fitness(populasi[best]):
            best = i
    return best