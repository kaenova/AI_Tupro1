import random
import math

def initialize_population(population):
    for i in range(10): #ada 10 kromosom
        kromosom = []
        for j in range(6): #ada 6 genotipe 
            kromosom.append(round((random.uniform(0, 1)), 3)) 
        population.append(kromosom)
    return population

def decodeX(genotipeX = []):
    temp_sum = 0
    for i in range(3):
        temp_sum = temp_sum + genotipeX[i]
    temp_x = (-1 + ((2-(-1)) * (temp_sum/3)))
    return temp_x

def decodeY(genotipeY = []):
    temp_sum = 0
    for i in range(3):
        temp_sum = temp_sum + genotipeY[i]
    temp_y = (-1 + ((1 -(-1)) * (temp_sum/3)))
    return temp_y
    
def fitnessDecode(population, fitness = []):
    # rumus fitness maksimasi f = h
    for i in range(10): #ada 10 kromosom
        kromosom = population[i]
        genotipeX = []
        genotipeY = []
        
        
        for j in range(3): #3 genotipe pertama merepresentasikan x
            genotipeX.append(kromosom[j])

        x = decodeX(genotipeX)

        for k in range(3):
            genotipeY.append(kromosom[k+3])
        
        y = decodeY(genotipeY)

        fitness_temp = (math.cos(x**2) * math.sin(y**2)) + (x + y)

        fitness.append(fitness_temp)

    # making all the fitness not negative, but this gave me a weird understanding of a fitness.
    # minimum_fitness = min(fitness)
    # for i in range(10):
    #     fitness[i] = fitness[i] +  (-minimum_fitness)

def tournamentSelection(population):
    #get best of 6 parent
    parent = []
    for i in range(6):
        parent.append(population[i])

    return parent

def getElitism(population):
    #get best of 4 kromosome
    elitism = []
    for i in range(4):
        elitism.append(population[i])

    return elitism


def PopFitnessSort(population, fitness):
    #Using selection sort
    i = 0
    j = 0
    while i < 10:
        maksimum = i
        j = i + 1
        while j < 9:
            if fitness[j] > fitness[maksimum]:
                maksimum = j
            j = j + 1

        temp_fitness = fitness[maksimum]
        temp_kromosom = population[maksimum]
        fitness[maksimum] = fitness[i]
        population[maksimum] = population[i]
        fitness[i] = temp_fitness
        population[i] = temp_kromosom
        i = i+1


def printBestKromosom(population, fitness, generation):
    best_kromosome = population[0]
    best_fitness = fitness[0]
    temp_Xgenotipe = []
    temp_Ygenotpe = []
    for i in range(6):
        if i < 3:
            temp_Xgenotipe.append(best_kromosome[i])
        else:
            temp_Ygenotpe.append(best_kromosome[i])
    print("Best of Generation {}".format(generation))
    print("Fitness: {}".format(best_fitness))
    print("Fenotipe X:{} Y:{}".format(decodeX(temp_Xgenotipe), decodeY(temp_Ygenotpe)))
    print("Genotipe: {}".format(best_kromosome))

def crossover(parent):
    



if __name__ == "__main__":
    generation = int(input("Masukkan ingin berapa generasi?: "))
    pop = []
    fitness = []
    initialize_population(pop)
    for i in range(generation):
        fitnessDecode(pop, fitness)
        PopFitnessSort(pop, fitness)
        printBestKromosom(pop, fitness, generation)
        parent = tournamentSelection(pop)
        elitism = getElitism(pop)
        print(elitism)
        print(parent)
        





# def dekode():


# def fitness():


# def selection():


# def mutation():


# def crossover():
#     #di dalm sini harusnya ada pemotongan

# def regeneration():



# def pemotongan(ortu1, ortu2, panjang_gen, panjang_potong):
#     anak1 = []
#     anak2 = []

#     for j in range(panjang_potong):
#         anak1.append(ortu1[j])
#     for k in range(panjang_gen - panjang_potong):
#         anak1.append(ortu2[k+panjang_potong])
#     for j in range(panjang_potong):
#         anak2.append(ortu2[j])
#     for k in range(panjang_gen - panjang_potong):
#         anak2.append(ortu1[k+panjang_potong])

#     return anak1, anak2

# a = kromosom()

# bruh1 = [0,1,1,1,0]
# bruh2 = [1,0,0,1,1]
# panjang_potong = random.randint(1,5)
# offspring1, offspring2 = pemotongan(bruh1, bruh2, 5, panjang_potong)
# print("panjang potong: {}".format(panjang_potong))
# print("awal: {}{}".format(bruh1, bruh2))
# print("akhir: {}{}".format(offspring1, offspring2))