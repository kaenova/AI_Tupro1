import random

def pemotongan(ortu1, ortu2, panjang_gen, panjang_potong):
    anak1 = []
    anak2 = []

    for j in range(panjang_potong):
        anak1.append(ortu1[j])
    for k in range(panjang_gen - panjang_potong):
        anak1.append(ortu2[k+panjang_potong])
    for j in range(panjang_potong):
        anak2.append(ortu2[j])
    for k in range(panjang_gen - panjang_potong):
        anak2.append(ortu1[k+panjang_potong])

    return anak1, anak2


bruh1 = [0,1,1,1,0]
bruh2 = [1,0,0,1,1]
panjang_potong = random.randint(1,5)
offspring1, offspring2 = pemotongan(bruh1, bruh2, 5, panjang_potong)
print("panjang potong: {}".format(panjang_potong))
print("awal: {}{}".format(bruh1, bruh2))
print("akhir: {}{}".format(offspring1, offspring2))