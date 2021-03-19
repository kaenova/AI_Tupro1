import random
import math
from time import sleep
from tqdm import tqdm

class kromosome():
    panjang = 8
    
    def decodeX(self):
        temp_genotipe = 0
        temp_integer = 0
        for i in range(int(self.panjang / 2)):
            temp_genotipe += self.kromosom[i] * (10**(-(i+1)))
            temp_integer += 9*(10**(-(i+1)))
        self.x = (-1) + (((2 - (-1))/temp_integer) * temp_genotipe)
        
    def decodeY(self):
        temp_genotipe = 0
        temp_integer = 0
        for i in range(int(self.panjang / 2)):
            temp_genotipe += self.kromosom[i+int(self.panjang / 2)] * (10**(-(i+1)))
            temp_integer += 9*(10**(-(i+1)))
        self.y = (-1) + (((1 - (-1))/temp_integer) * temp_genotipe)

    def CalculateFitness(self):
        self.fitness = (math.cos(self.x**2)*math.sin(self.y**2) + (self.x + self.y))

    def PrintKromosome(self):
        print("Fitness: {}".format(self.fitness))
        print("Fenotip X: {} Y: {}".format(self.x, self.y))
        print("Genotipe: {} \n".format(self.kromosom))

    def __init__(self):
        self.kromosom = []
        self.fitness = 0
        self.x = 0
        self.y = 0
        for j in range(self.panjang):
            self.kromosom.append(random.randint(0, 9))
        self.decodeX()
        self.decodeY()

def initialize_population(population_made):
    population = []
    for i in range(population_made): #variable
        kromosome_temp = kromosome()
        # Coded by Kaenova Mahendra Auditama (kaenova@gmail.com)
        # *not responsible if someone plagirized or copied my code
        population.append(kromosome_temp)
    return population

def calculateKromosomeFitness(population):
    for i in range(len(population)):
        population[i].CalculateFitness()

def PopulationFitnessSort(population: [kromosome()]):
    population = sorted(population, key=lambda x: x.fitness, reverse= 1)

    return population

def tournamentSelection(population):
    get_selection = (math.floor(len(population)/ 5))
    if get_selection % 2 != 0:
       get_selection += 1
    jum_parent = (len(population) - get_selection)
    start_parent = int((get_selection / 2) - 1)
    parent = []
    for i in range(jum_parent) :
        parent.append(population[start_parent])

    return parent

def getElitism(population):
    get_selection = (math.floor(len(population)/ 5))
    if get_selection % 2 != 0:
        get_selection += 1
    elitism = []
    for i in range(get_selection):
        elitism.append(population[i])

    return elitism

# Coded by Kaenova Mahendra Auditama (kaenova@gmail.com)
# *not responsible if someone plagirized or copied my code

def MatingPool(parent = [kromosome()]):
    #buat mating pool
    parent_temp = parent
    pasangan = []
    j = 0

    for i in range(int(len(parent)/2)):
        pasangan_temp = []
        random_angka_parent = random.randint(1, (len(parent_temp)-1))
        pasangan_temp.append(parent_temp[0])
        pasangan_temp.append(parent_temp[random_angka_parent])
        pasangan.append(pasangan_temp)
        parent_temp.pop(random_angka_parent)
        parent_temp.pop(0)
        j = j + 1

    return pasangan


def crossover(pasangan = [[kromosome],[kromosome]]):
    populasi_anak = []
    for i in range(len(pasangan)):
        temp_pasangan = pasangan[i]
        parent1 = temp_pasangan[0]
        parent2 = temp_pasangan[1]
        panjang_potong = random.randint(1,4)

        children_temp1 = []
        children_temp2 = []

        for j in range(panjang_potong):
            children_temp1.append(parent1.kromosom[j])
        for k in range(len(parent1.kromosom) - panjang_potong):
            children_temp1.append(parent2.kromosom[k+panjang_potong])
        for j in range(panjang_potong):
            children_temp2.append(parent2.kromosom[j])
        for k in range(len(parent1.kromosom) - panjang_potong):
            children_temp2.append(parent1.kromosom[k+panjang_potong])

        kromosome_temp_1 = kromosome()
        kromosome_temp_2 = kromosome()
        kromosome_temp_1.kromosom = children_temp1
        kromosome_temp_2.kromosom = children_temp2
        kromosome_temp_1.CalculateFitness()
        kromosome_temp_2.CalculateFitness()
        populasi_anak.append(kromosome_temp_1)
        populasi_anak.append(kromosome_temp_2)

    return populasi_anak

def mutation(children):
    for i in range(len(children)):
        for j in range(children[i].panjang):
            random_mutation = random.uniform(0,1)
            if (random_mutation < 0.1 ): #Setup mutasi
                if children[i].kromosom[j] > 0:
                    children[i].kromosom[j] -= 1
                else:
                    children[i].kromosom[j] += 1
    
    return children

def printAllKromosome(population = [kromosome()]):
    for i in range(len(population)):
        population[i].PrintKromosome()

def printBestKromosom(best: kromosome, generasi):
    print(" Best Fitness from Generation {}".format(generasi+1))
    # Coded by Kaenova Mahendra Auditama (kaenova@gmail.com)
    # *not responsible if someone plagirized or copied my code
    print("Fitness: {}".format(best.fitness))
    print("Fenotip X: {} Y: {}".format(best.x, best.y))
    print("Genotipe: {} \n".format(best.kromosom))


if __name__ == "__main__":
    population_number = int(input("How many population do you want to have? \n [Input Even Number over 10] : "))
    while (population_number % 2 != 0) or (population_number < 10):
        population_number = int(input("How many population do you want to have? \n [Input Even Number over 10] : "))

    generation = int(input("How many generation do you want to have?: "))
    while generation <= 0:
        generation = int(input("How many generation do you want to have?: "))
    

    population = initialize_population(population_number)

    best_kromosom = kromosome()

    for i in tqdm(range(generation)):
        calculateKromosomeFitness(population)
        PopulationFitnessSort(population)
        
        if best_kromosom.fitness < population[0].fitness:
            best_kromosom = population[0]
            printBestKromosom(population[0], i)
        
        elitism = getElitism(population)
        parent = tournamentSelection(population) 
        couple = MatingPool(parent)
        children = crossover(couple)
        children = mutation(children)
        population = children + elitism