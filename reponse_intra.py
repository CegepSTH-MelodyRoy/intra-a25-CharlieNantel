##########################################
# Nantel, Charlie, <6266266>
##########################################
import random as rdm
for i in range(10):
    temperature = rdm.uniform(20, 35)

def question1():
    if 24 < temperature <=30:
        message = "ok"
    elif temperature < 24:
        message = "Trop froid"
    elif temperature > 30 :
        message = "Trop chaud"
    print("Jour", i, ":", format(temperature, ".1f"), message)

question1()



import numpy as np
import matplotlib.pyplot as plt

pop_bacterie_initiale = input("Entrez la population de bactérie initiale :")
pop_chaque_heure = pop_bacterie_initiale + str((np.pi)/(1.5))

plt.figure(figsize=(1,1))
plt.xlabel("heures")
plt.ylabel("population")
plt.xlim(0, 10)
plt.title("Croissance bactérienne")
plt.plot(pop_chaque_heure, "*b")
plt.grid()
plt.show()



