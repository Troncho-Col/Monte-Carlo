# MONTECARLO -Grigori
# Pol Adillon Albero - 14/12/2021
# 
# EXERCICE 1: CENTRAL LIMIT THEOREM
# In this program we consider the problem ot throwing dice multiple times
# and calculate the resulting probability distribution
 
import random
import matplotlib.pyplot as plt
import numpy as np


# TASK 1: 
print("EXERCICE 1:                Pol Adillon Albero")
print("---------------------------------------------")


print("TASK 1: One die")

print("Random output of thowing a die:", random.randint(1,6))

Possible_Outcome = [1,2,3,4,5,6]
Outcome_Counter = [0,0,0,0,0,0]   #We will count how many times we get each number
N_throws = 1000                     #Number of throws
N_dice = 1                          #Number of dice used
sum_die = 0
sum_die2 = 0


print("Here we have how many times we have get each number:")
print(Outcome_Counter)




for j in range(1,N_throws+1):
    i=random.randint(1,6)
    Outcome_Counter[i-1] = Outcome_Counter[i-1]+1
    sum_die = sum_die + i               # This will sum every result of the throws
    sum_die2 = sum_die2 + i**2


print("Afer ",N_throws,"our list is")
print(Outcome_Counter)
print("The total number of throws is:", sum(Outcome_Counter))

#Here we calculate the mean value 
mean_value_data = sum_die/(N_throws)
print("<X>: ",mean_value_data)
mean_value2_data = sum_die2/(N_throws)
print("<X²>: ",mean_value2_data)
variance = np.sqrt(mean_value2_data-mean_value_data**2) 
print("Sigma:", variance)



# PLOT 1:

file = open("data.txt", "w")
for index in range(len(Possible_Outcome)):
    file.write(str(Possible_Outcome[index]) + " " + str(Outcome_Counter[index]) + "\n")
file.close()



#ax.scatter(Possible_Outcome,np.divide(Outcome_Counter,N_throws))
#ax.hlines(1/6,-1,7,colors="r")
#plt.plotS
#ax.set_ylim(0,1)
#ax.set_xlabel("x")
#ax.set_ylabel("Pi")
#ax.set_yticks([0,1/6,2/6,3/6,4/6,5/6,1])
#ax.set_title("Task 1: die")
#plt.show()
#plt.savefig("GRAF1.png")




print("---------------------------------------------")
print("TASK 2: Two dice")

N_throws = 10000   #Number of throws
N_dice = 2          #Number of dice used
sum_die = 0
sum_die2 = 0

DeltaX = 1/N_dice
Many_Dice = [0]*(6*N_dice-1) 

print(Many_Dice)


