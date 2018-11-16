#SOLVING 0-1 KNAPSACK PROBLEM USING GENETIC ALGORITHM
#0-1 KNAPSACK PROBLEM:A REAL-TIME PROBLEM IN WHICH WE NEED TO FILL THE KNAPSACK WITH ITEMS OF SOME WEIGHT 
#AND PROFITS SUCH THAT SUM OF WEIGHTS OF ITEM ADDED MUST NOT EXCEED KNAPSACK CAPACITY WHICH IS FIXED AND PROFIT IS MAX.
#STEP 1:RANDOMLY GENERATING 5 ITEM WITH PROFITS AND WEIGHTS USING RANDOM MODULE.
#STEP 2:GENERATION OF FIRST POPULATION( A SET OF SOLUTIONS) CONSISTING OF CHROMOSOMES(POSSIBLE SOLUTIONS) WHICH ARE
#A STRING OF COMBINATIONS OF BINARY BITS(0 OR 1).
#STEP 3:FITNESS OF EACH CHROMOSOME IS CALCULATED.
#STEP 4:NEXT GENERATION (MORE FTTER OR PROFITABLE) IS CREATED BY FOLLOWING STEPS.
     #1.SOME OF FITTEST PARENTS(SOLUTIONS) ARE SELECTED AND MUTATION IS PERFORMED OVER THEM. THESE MUTATED PARENTS 
     #ARE ADDED TO NEXT GENERATION.
     #2.NOW SCINCE POPULATION SIZE OF 10 IS FIXED REMAINING SOLUTIONS ARE CREATED BY A METHOD CALLED CROSSOVER.
     #CROSSOVER IS PERFORMED OVER 2 SOLUTIONS AMONG THE FTTEST SELECTED IN 1.AND THESE CHILDREN PRODUCED ARE ADDED
     #TO NEXT GENERATION.
#IN SAME WAY MAX 10 GENERATIONS ARE PRODUCED AND OPTIMAL(FITTEST OR MOST PROFITABLE COMBINATION OF ITEMS) 
#SOLUTION IS OBTAINED.
    


import random
class Item(object):
    def __init__(self, p, w):
        self.profit = p   # Item's value. 
        self.weight = w  # Item's weight.
ITEMS = [Item(random.randint(0,30),random.randint(0,30)) for x in range (0,10)]
CAPACITY =100
POP_SIZE = 10
GEN_MAX = 10
START_POP_WITH_ZEROES = False

def fitness(target):
    #Higher fitness are better and are equal to the total profit of items in the a chromosome.
    #If total_weight is higher than the capacity, return 0 because the chromosome cannot be used.
 
    total_profit = 0
    total_weight = 0
    i= 0
    for j in target:        
        if i >= len(ITEMS):
            break
        if (j == 1):
            total_profit += ITEMS[i].profit
            total_weight += ITEMS[i].weight
        i += 1
        
    
    if total_weight > CAPACITY:
        # Chromosome cannot be considered.
        return 0
    else:
        return total_profit

def starting_population(amount):
    return [create_chromosome() for x in range (0,amount)]

def create_chromosome():
    if START_POP_WITH_ZEROES:
        return [random.randint(0,0) for x in range (0,len(ITEMS))]
    else:
        return [random.randint(0,1) for x in range (0,len(ITEMS))]

def mutate(target):
   
    #Changes a random bit of the chromosome array from 0 -> 1 or from 1 -> 0.
    
    r = random.randint(0,len(target)-1)
    if target[r] == 1:
        target[r] = 0
    else:
        target[r] = 1

def next_population(pop):
    parent_eligibility = 0.2
    mutation_chance = 0.08
    parent_lottery = 0.05

    parent_length = int(parent_eligibility*len(pop))
    parents = pop[:parent_length]
    nonparents = pop[parent_length:]

    for np in nonparents:
        if parent_lottery > random.random():
            parents.append(np)

    for p in parents:
        if mutation_chance > random.random():
            mutate(p)

    children = []
    desired_length = len(pop) - len(parents)
    while len(children) < desired_length :
        male = pop[random.randint(0,len(parents)-1)]
        female = pop[random.randint(0,len(parents)-1)]        
        half = len(male)/2
        child = male[:int(half)] + female[int(half):] # Crossover from start to half from father, from half to end from mother
        if mutation_chance > random.random():
            mutate(child)
        children.append(child)

    parents.extend(children)
    return parents

def GeneticAlgo():
    generation = 1
    population = starting_population(POP_SIZE)
    for g in range(0,GEN_MAX):
        print("Generation %d with %d" % (generation,len(population)))
        population = sorted(population, key=lambda x: fitness(x), reverse=True)
        for i in population:        
            print("%s, fit: %s" % (str(i), fitness(i)))        
        population = next_population(population)
        generation += 1

GeneticAlgo()

#OUTPUT
#Generation 1 with 10
#[1, 0, 1, 0, 1, 1, 1, 1, 1, 0], fit: 117
#[1, 0, 0, 1, 0, 1, 1, 1, 1, 0], fit: 114
#[1, 1, 1, 0, 0, 1, 1, 1, 0, 0], fit: 113
#[1, 1, 0, 0, 1, 1, 0, 1, 0, 0], fit: 99
#[0, 1, 0, 1, 0, 1, 0, 1, 0, 1], fit: 98
#[0, 1, 0, 1, 0, 1, 0, 1, 0, 1], fit: 98
#[1, 0, 1, 1, 0, 1, 0, 1, 0, 1], fit: 94
#[0, 0, 1, 0, 0, 1, 1, 1, 1, 0], fit: 83
#[1, 0, 0, 1, 0, 0, 0, 1, 1, 0], fit: 75
#[0, 0, 1, 1, 1, 0, 0, 0, 0, 0], fit: 59
#Generation 2 with 10
#[1, 1, 1, 0, 0, 1, 1, 1, 1, 0], fit: 126
#[1, 1, 1, 0, 0, 1, 1, 1, 1, 0], fit: 126
#[1, 1, 1, 0, 0, 1, 1, 1, 1, 0], fit: 126
#[1, 0, 1, 0, 1, 1, 1, 1, 1, 0], fit: 117
#[1, 0, 1, 0, 1, 1, 1, 1, 1, 0], fit: 117
#[1, 0, 1, 0, 1, 1, 1, 1, 1, 0], fit: 117
#[0, 0, 0, 1, 0, 1, 1, 1, 1, 0], fit: 100
#[1, 1, 0, 0, 1, 1, 0, 1, 0, 0], fit: 99
#[0, 0, 0, 1, 0, 1, 1, 1, 0, 0], fit: 87
#[0, 0, 0, 1, 0, 1, 1, 1, 0, 0], fit: 87
#Generation 3 with 10
#[1, 1, 1, 0, 0, 1, 1, 1, 1, 0], fit: 126
#[1, 1, 1, 0, 0, 1, 1, 1, 1, 0], fit: 126
#[1, 1, 1, 0, 0, 1, 1, 1, 1, 0], fit: 126
#[1, 1, 1, 0, 0, 1, 1, 1, 1, 0], fit: 126
#[1, 1, 1, 0, 0, 1, 1, 1, 1, 0], fit: 126
#[1, 1, 1, 0, 0, 1, 1, 1, 1, 0], fit: 126
#[1, 1, 1, 0, 0, 1, 1, 1, 1, 0], fit: 126
#[1, 1, 1, 0, 0, 1, 1, 1, 1, 0], fit: 126
#[1, 1, 1, 0, 0, 1, 1, 1, 1, 0], fit: 126
#[1, 1, 1, 0, 0, 1, 1, 1, 0, 0], fit: 113
#Generation 4 with 10
#[1, 1, 1, 0, 0, 1, 1, 1, 1, 0], fit: 126
#[1, 1, 1, 0, 0, 1, 1, 1, 1, 0], fit: 126
#[1, 1, 1, 0, 0, 1, 1, 1, 1, 0], fit: 126
#[1, 1, 1, 0, 0, 1, 1, 1, 1, 0], fit: 126
#[1, 1, 1, 0, 0, 1, 1, 1, 0, 0], fit: 113
#[1, 0, 1, 0, 0, 1, 1, 1, 1, 0], fit: 97
#[1, 0, 1, 0, 0, 1, 1, 1, 1, 0], fit: 97
#[1, 0, 1, 0, 0, 1, 1, 1, 1, 0], fit: 97
#[1, 0, 1, 0, 0, 1, 1, 1, 1, 0], fit: 97
#[1, 0, 1, 0, 0, 1, 1, 1, 1, 0], fit: 97
#Generation 5 with 10
#[1, 1, 1, 0, 1, 1, 1, 1, 1, 0], fit: 146
#[1, 1, 1, 0, 0, 1, 1, 1, 1, 1], fit: 131
#[1, 1, 1, 0, 0, 1, 1, 1, 1, 0], fit: 126
#[1, 1, 1, 0, 0, 1, 1, 1, 1, 0], fit: 126
#[1, 1, 1, 0, 0, 1, 1, 1, 1, 0], fit: 126
#[1, 1, 1, 0, 0, 1, 1, 1, 1, 0], fit: 126
#[1, 1, 1, 0, 0, 1, 1, 1, 1, 0], fit: 126
#[1, 1, 1, 0, 0, 1, 1, 1, 1, 0], fit: 126
#[1, 1, 1, 0, 0, 1, 1, 1, 0, 0], fit: 113
#[1, 1, 1, 0, 0, 1, 1, 0, 1, 0], fit: 106
#Generation 6 with 10
#[1, 1, 1, 0, 1, 1, 1, 1, 1, 0], fit: 146
#[1, 1, 1, 0, 1, 1, 1, 1, 1, 0], fit: 146
#[1, 1, 1, 0, 1, 1, 1, 1, 1, 0], fit: 146
#[1, 1, 1, 0, 0, 1, 1, 1, 1, 1], fit: 131
#[1, 1, 1, 0, 0, 1, 1, 1, 1, 1], fit: 131
#[1, 1, 1, 0, 0, 1, 1, 1, 1, 1], fit: 131
#[1, 1, 1, 0, 0, 1, 1, 1, 1, 0], fit: 126
#[1, 1, 1, 0, 0, 1, 1, 1, 1, 0], fit: 126
#[1, 1, 1, 0, 0, 1, 1, 1, 1, 0], fit: 126
#[1, 1, 1, 0, 0, 1, 1, 1, 1, 0], fit: 126
#Generation 7 with 10
#[1, 1, 1, 0, 1, 1, 1, 1, 1, 0], fit: 146
#[1, 1, 1, 0, 1, 1, 1, 1, 1, 0], fit: 146
#[1, 1, 1, 0, 1, 1, 1, 1, 1, 0], fit: 146
#[1, 1, 1, 0, 1, 1, 1, 1, 1, 0], fit: 146
#[1, 1, 1, 0, 1, 1, 1, 1, 1, 0], fit: 146
#[1, 1, 1, 0, 1, 1, 1, 1, 1, 0], fit: 146
#[1, 1, 1, 0, 1, 1, 1, 1, 1, 0], fit: 146
#[1, 1, 1, 0, 1, 1, 1, 1, 1, 0], fit: 146
#[0, 1, 1, 0, 1, 1, 1, 1, 1, 0], fit: 132
#[1, 1, 1, 0, 0, 1, 1, 1, 1, 0], fit: 126
#Generation 8 with 10
#[1, 1, 1, 0, 1, 1, 1, 1, 1, 0], fit: 146
#[1, 1, 1, 0, 1, 1, 1, 1, 1, 0], fit: 146
#[1, 1, 1, 0, 1, 1, 1, 1, 1, 0], fit: 146
#[1, 1, 1, 0, 1, 1, 1, 1, 1, 0], fit: 146
#[1, 1, 1, 0, 1, 1, 1, 1, 1, 0], fit: 146
#[1, 1, 1, 0, 1, 1, 1, 1, 1, 0], fit: 146
#[1, 1, 1, 0, 1, 1, 1, 1, 1, 0], fit: 146
#[1, 1, 1, 0, 1, 1, 1, 1, 1, 0], fit: 146
#[1, 1, 1, 0, 1, 1, 1, 1, 1, 0], fit: 146
#[1, 1, 1, 0, 1, 1, 0, 1, 1, 0], fit: 123
#Generation 9 with 10
#[1, 1, 1, 0, 1, 1, 1, 1, 1, 0], fit: 146
#[1, 1, 1, 0, 1, 1, 1, 1, 1, 0], fit: 146
#[1, 1, 1, 0, 1, 1, 1, 1, 1, 0], fit: 146
#[1, 1, 1, 0, 1, 1, 1, 1, 1, 0], fit: 146
#[1, 1, 1, 0, 1, 1, 1, 1, 1, 0], fit: 146
#[1, 1, 1, 0, 1, 1, 1, 1, 1, 0], fit: 146
#[1, 1, 1, 0, 1, 1, 1, 1, 1, 0], fit: 146
#[1, 1, 1, 0, 1, 1, 1, 1, 1, 0], fit: 146
#[1, 1, 1, 0, 1, 1, 1, 1, 1, 0], fit: 146
#[1, 1, 1, 0, 1, 1, 0, 1, 1, 0], fit: 123
#Generation 10 with 10
#[1, 1, 1, 0, 1, 1, 1, 1, 1, 0], fit: 146
#[1, 1, 1, 0, 1, 1, 1, 1, 1, 0], fit: 146
#[1, 1, 1, 0, 1, 1, 1, 1, 1, 0], fit: 146
#[1, 1, 1, 0, 1, 1, 1, 1, 1, 0], fit: 146
#[1, 1, 1, 0, 1, 1, 1, 1, 1, 0], fit: 146
#[1, 1, 1, 0, 1, 1, 1, 1, 1, 0], fit: 146
#[1, 1, 1, 0, 1, 1, 1, 1, 1, 0], fit: 146
#[1, 1, 1, 0, 1, 1, 1, 1, 1, 0], fit: 146
#[1, 1, 0, 0, 1, 1, 1, 1, 1, 0], fit: 135
#[1, 1, 1, 0, 1, 0, 1, 1, 1, 0], fit: 130


#YOU CAN SEE THE VARIATIONS BY CHANGING THE POP_SIZE OR NO. OF ITEMS OR ITEM'S PROFIT AND WEIGHT RANGES OR GEN_MAX.
