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
    temp_x = (-1 + (2-(-1)) * temp_sum)
    return temp_x

def decodeY(genotipeY = []):
    temp_sum = 0
    for i in range(3):
        temp_sum = temp_sum + genotipeY[i]
    temp_y = (-1 + (1 -(-1)) * temp_sum)
    return temp_y
    
def fitnessDecode(population, fitness = []):
    # rumus fitness maksimasi f = h
    for i in range(10): #ada 10 kromosom
        kromosom = population[i]
        print(kromosom)
        genotipeX = []
        genotipeY = []
        
        
        for j in range(3): #3 genotipe pertama merepresentasikan x
            genotipeX.append(kromosom[j])

        x = decodeX(genotipeX)

        for k in range(3):
            genotipeY.append(kromosom[k+3])
        
        y = decodeY(genotipeY)

        fitness_temp = (math.cos(x**2) * math.sin(y**2)) + (x + y)
        
        print("Fenotipe Kromosom{} X:{} Y:{} dengan fitness {}".format(i+1,x,y,fitness_temp))

        fitness.append(fitness_temp)


if __name__ == "__main__":
    pop = []
    fitness = []
    initialize_population(pop)
    fitnessDecode(pop, fitness)





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