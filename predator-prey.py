#Name: Nana Kwasi Owusu
#Date: 3rd February, 2024.
#Program Description: A program that simulates the population of foxes and rabbits after a number of years

#this makes it possible to import math modules that would be used for some of the calculations 
import math

#this function gets the input from the user and repeatedly asks the question until the user inputs a positive non-zero integer
def getInteger(question):
     while(True):
        answer = input(question)
        if answer.isnumeric() and int(answer)>0:
            return int(answer)
        else:
            print('Invalid Input. Kindly enter a positive non-zero integer')

#this function calculates the number of rabbits that survive until the next year
def nextRabbits(foxes, rabbits):
    A = 0.04
    B = 0.0005
    numOfRabbits = rabbits + math.floor(rabbits * (A - B * foxes))
    return numOfRabbits

#this function calculates the number of foxes that survive until the next year
def nextFoxes(foxes, rabbits):
    G = 0.2
    S = 0.00005
    numOfFoxes = foxes - math.floor(foxes * (G - S * rabbits))
    return numOfFoxes

if __name__ == "__main__":
    #this part of the code collects input from the user (it specifically collects the number of rabbits, the number of foxes anf the number of years to simulate)
    survivedRabbits = getInteger('Enter the number of rabbits: ')
    survivedFoxes = getInteger('Enter the number of foxes: ')
    numOfYears = getInteger('Enter the number of years to simulate: ')
    print()
    print('| Years | Foxes | Rabbits|')
    print('| ----- | ----  | -------|')
    
    #this loop always makes year 0 print. The number of foxes and rabbits for the rest of the years that the user specifies then prints after
    count = 0
    while count <= numOfYears:
        if count == 0:
            print(f'|{count:^6} |{survivedFoxes:^6} | {survivedRabbits:^6} |')
        else:
            initialRabbits = survivedRabbits
            survivedRabbits = nextRabbits(survivedFoxes,survivedRabbits)
            survivedFoxes = nextFoxes(survivedFoxes,initialRabbits)
            print(f'|{count:^6} |{survivedFoxes:^6} | {survivedRabbits:^6} |')
        count +=1
            
    
    
    
    
