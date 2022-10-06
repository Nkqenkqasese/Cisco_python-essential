				#SCENARIO

#Imagine a list ‒ not very long, not very complicated, just a simple list containing some integer numbers. Some of these numbers may be repeated, and this is the clue. We don't want any repetitions. We want them to be removed.

#Your task is to write a program which removes all the number repetitions from the list. The goal is to have a list in which all the numbers appear not more than once.

#Note: assume that the source list is hard-coded inside the code ‒ you don't have to enter it from the keyboard. Of course, you can improve the code and add a part that can carry out a conversation with the user and obtain all the data from her/him.

#Hint: we encourage you to create a new list as a temporary work area ‒ you don't need to update the list in situ.

from random import *

n=int(input('Input the size of the list '))
my_list = []

for i in range(n):
    x = round(random()*10,0) #generate a list of random number from 1 to 10
    my_list.append(x)
#
#sorting the list in ascending order in order to put the duplicated values side by side
my_list.sort()
final_list = []

#check the cases of indice[1] to indice[n]
for i in range(len(my_list)-1): 
    if my_list[i+1] == my_list[i]:  #if value[i+1] is a duplication, it is not added to final_list
        continue
    if my_list[i+1] != my_list[i]:
        final_list.append(my_list[i+1]) #if value [i+1] is a new numbern it is added to final_list
        
#case for indice[0]
if my_list[0] not in final_list: 
    final_list.insert(0,my_list[0]) #if value[0] is not in final_list it is added to it

    
print("The list with unique elements only: ")
print(final_list)
