import random
import math

def initialize_population():
    population = []
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
    
def fitnessDecode(population):
    # rumus fitness maksimasi f = h
    fitness = []
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
    
    return fitness

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
    return population, fitness


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
    print("Best of Generation {}".format(generation + 1))
    print("Fitness: {}".format(best_fitness))
    print("Fenotipe X:{} Y:{}".format(decodeX(temp_Xgenotipe), decodeY(temp_Ygenotpe)))
    print("Genotipe: {} \n".format(best_kromosome))

def MatingPool(parent):
    #buat mating pool
    parent_temp = parent
    j = len(parent_temp)
    pasangan_temp = []
    pasangan = []

    for i in range(2):
        random_angka_parent = random.randint(1, j-2)
        pasangan_temp.append(parent_temp[0])
        pasangan_temp.append(parent_temp[random_angka_parent])
        pasangan.append(pasangan_temp)
        pasangan_temp = []
        parent_temp.pop(random_angka_parent)
        parent_temp.pop(0)
        j = j-1

    pasangan.append(parent_temp)

    return pasangan

def crossover(pasangan):
    children = []
    for i in range(3):
        temp_pasangan = pasangan[i]
        parent1 = temp_pasangan[0]
        parent2 = temp_pasangan[1]
        panjang_potong = random.randint(1,4)

        children_temp1 = []
        children_temp2 = []

        for j in range(panjang_potong):
            children_temp1.append(parent1[j])
        for k in range(len(parent1) - panjang_potong):
            children_temp1.append(parent2[k+panjang_potong])
        for j in range(panjang_potong):
            children_temp2.append(parent2[j])
        for k in range(len(parent1) - panjang_potong):
            children_temp2.append(parent1[k+panjang_potong])

        children.append(children_temp1)
        children.append(children_temp2)

    return children

def mutation(children):
    mutated_children = []
    for i in range(6):
        temp_children = children[i]
        for j in range(6):
            random_mutation = random.uniform(0,1)
            if (random_mutation < 0.1 ): #Setup mutasi
                temp_children[j] += (random.uniform(-0.05,0.05))
        mutated_children.append(temp_children)
    
    return mutated_children

def next_gen(elitism, children):
    population = []
    for i in range(4):
        population.append(elitism[i])
    for j in range(6):
        population.append(children[j])
    return population



if __name__ == "__main__":
    generation = int(input("Masukkan ingin berapa generasi?: "))
    pop = []
    fitness = []
    fitness_terbaik = 0
    generasi_terbaik = 0
    pop = initialize_population()
    for i in range(generation):
        fitness = fitnessDecode(pop)
        pop, fitness = PopFitnessSort(pop, fitness)
        printBestKromosom(pop, fitness, i)
        parent = tournamentSelection(pop)

        elitism = getElitism(pop)
        mating_pool = MatingPool(parent)
        children = crossover(mating_pool)
        children = mutation(children)

        pop = next_gen(elitism, children)
        if fitness_terbaik <= fitness[0]:
            fitness_terbaik = fitness[0]
            generasi_terbaik = i + 1

    print("Generasi Terbaik: {}".format(generasi_terbaik))
    print("Dengan Fitness: {}".format(fitness_terbaik))