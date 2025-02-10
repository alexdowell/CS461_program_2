# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 22:27:40 2022

@author: alexa
"""
import random
import math
import numpy as np
import statistics
from tabulate import tabulate
import datetime
 
class Course:
    def __init__(self, name, time, room, room_capacity, instructor, expected_enrollment, preferred_instructors, other_instructors, remaining_instructors):
        self.name = name
        self.time = time
        self.room = room
        self.room_capacity = room_capacity
        self.instructor = instructor
        self.expected_enrollment = expected_enrollment
        self.preferred_instructors = preferred_instructors
        self.other_instructors = other_instructors
        self.remaining_instructors = remaining_instructors
    
# creating a fitness function
def fitness_function(chromosome, courses, rooms, times, instructors, room_capacities):
    # intializing the fitness score
    fitness_score = 0
    
    #checking for the same time and room
    for gene in chromosome:
        for gene1 in chromosome:
            if gene1.time == gene.time: 
                if gene1.room == gene.room: 
                    if gene.name != gene1.name:
                        fitness_score = fitness_score - 0.5/2
                
    # room capacity vs. expected enrollment      
    for gene in chromosome:       
        # checking if the class is in a room too small for its expected enrollment
        room_counter = 0
        if gene.room_capacity < gene.expected_enrollment:
            fitness_score = fitness_score - 0.5
            room_counter += 1
        # checking if the class is in a room with capacity > 3 times expected enrollment
        if gene.room_capacity > 3 * gene.expected_enrollment:
            fitness_score = fitness_score - 0.2
            room_counter += 1
        # checking if the class is in a room with capacity > 6 times expected enrollment
        if gene.room_capacity > 6 * gene.expected_enrollment:
            fitness_score = fitness_score - 0.4
            room_counter += 1
        # otherwise
        if room_counter == 0:
            fitness_score = fitness_score + 0.3
            
    # checking to see if the class is taught by a preferred faculty member
    for gene in chromosome:
        for prefered_instructor in gene.preferred_instructors:
            if prefered_instructor == gene.instructor:
                fitness_score += 0.5
                
    # checking to see if the class is taught by another faculty member listed for that course
    for gene in chromosome:    
        for other_instructor in gene.other_instructors:
            if other_instructor == gene.instructor:
                fitness_score += 0.2
                
    # checking to see if the class is taught by some other faculty
    for gene in chromosome:    
        if gene.instructor not in gene.preferred_instructors and gene.instructor not in gene.other_instructors:
            fitness_score -= 0.1
            
# checking for the instructor load
    Gharibi_list = []
    Gladbach_list = []
    Hare_list = []
    Nait_Abdesselam_list = []
    Shah_list = []
    Song_list = []
    Uddin_list = []
    Xu_list = []
    Zaman_list = []
    Zein_el_Din_list = []
    for gene in chromosome:
        if gene.instructor == 'Gharibi':
            Gharibi_list.append(gene.time)
        if gene.instructor == 'Gladbach':
            Gladbach_list.append(gene.time)
        if gene.instructor == 'Hare':
            Hare_list.append(gene.time)
        if gene.instructor == 'Nait-Abdesselam':
            Nait_Abdesselam_list.append(gene.time)
        if gene.instructor == 'Shah':
            Shah_list.append(gene.time)
        if gene.instructor == 'Song':
            Song_list.append(gene.time)
        if gene.instructor == 'Uddin':
            Uddin_list.append(gene.time)
        if gene.instructor == 'Xu':
            Xu_list.append(gene.time)
        if gene.instructor == 'Zaman':
            Zaman_list.append(gene.time)
        if gene.instructor == 'Zein el Din':
            Zein_el_Din_list.append(gene.time)
    
# checking to see if instructor is double booked
    for time in Gharibi_list:
        if Gharibi_list.count(time) > 1:
            fitness_score -= 0.2
            break
    for time in Gladbach_list:
        if Gladbach_list.count(time) > 1:
            fitness_score -= 0.2
            break
    for time in Hare_list:
        if Hare_list.count(time) > 1:
            fitness_score -= 0.2
            break
    for time in Nait_Abdesselam_list:
        if Nait_Abdesselam_list.count(time) > 1:
            fitness_score -= 0.2
            break
    for time in Shah_list:
        if Shah_list.count(time) > 1:
            fitness_score -= 0.2
            break
    for time in Song_list:
        if Song_list.count(time) > 1:
            fitness_score -= 0.2
            break
    for time in Uddin_list:
        if Uddin_list.count(time) > 1:
            fitness_score -= 0.2
            break
    for time in Xu_list:
        if Xu_list.count(time) > 1:
            fitness_score -= 0.2
            break
    for time in Zaman_list:
        if Zaman_list.count(time) > 1:
            fitness_score -= 0.2
            break
    for time in Zein_el_Din_list:
        if Zein_el_Din_list.count(time) > 1:
            fitness_score -= 0.2
            break

# need to check to see if an instructor for a course is only teaching one course for that time slot
    for gene in chromosome:
        if gene.instructor == 'Gharibi':
            if Gharibi_list.count(gene.time) == 1:
                fitness_score += 0.2
        if gene.instructor == 'Gladbach':
            if Gladbach_list.count(gene.time) == 1:
                fitness_score += 0.2
        if gene.instructor == 'Hare':
            if Hare_list.count(gene.time) == 1:
                fitness_score += 0.2
        if gene.instructor == 'Nait-Abdesselam':
            if Nait_Abdesselam_list.count(gene.time) == 1:
                fitness_score += 0.2
        if gene.instructor == 'Shah':
            if Shah_list.count(gene.time) == 1:
                fitness_score += 0.2
        if gene.instructor == 'Song':
            if Song_list.count(gene.time) == 1:
                fitness_score += 0.2
        if gene.instructor == 'Uddin':
            if Uddin_list.count(gene.time) == 1:
                fitness_score += 0.2
        if gene.instructor == 'Xu':
            if Xu_list.count(gene.time) == 1:
                fitness_score += 0.2
        if gene.instructor == 'Zaman':
            if Zaman_list.count(gene.time) == 1:
                fitness_score += 0.2
        if gene.instructor == 'Zein el Din':
            if Zein_el_Din_list.count(gene.time) == 1:
                fitness_score += 0.2   

    # checking if the course instructor is scheduleed for more than 4 classes total
    if len(Gharibi_list) > 4:
        fitness_score -= 0.5
    if len(Gladbach_list) > 4:
        fitness_score -= 0.5
    if len(Hare_list) > 4:
        fitness_score -= 0.5
    if len(Nait_Abdesselam_list) > 4:
        fitness_score -= 0.5
    if len(Shah_list) > 4:
        fitness_score -= 0.5
    if len(Song_list) > 4:
        fitness_score -= 0.5
    if len(Uddin_list) > 4:
        fitness_score -= 0.5
    if len(Xu_list) > 4:
        fitness_score -= 0.5
    if len(Zaman_list) > 4:
        fitness_score -= 0.5
    if len(Zein_el_Din_list) > 4:
        fitness_score -= 0.5

# checking if the course instructor is scheduleed for 1 or 2 classes total
    if len(Gharibi_list) < 3 and len(Gharibi_list) > 0:
        fitness_score -= 0.4
    if len(Gladbach_list) < 3 and len(Gladbach_list) > 0:
        fitness_score -= 0.4
    if len(Hare_list) < 3 and len(Hare_list) > 0:
        fitness_score -= 0.4
    if len(Nait_Abdesselam_list) < 3 and len(Nait_Abdesselam_list) > 0:
        fitness_score -= 0.4
    if len(Shah_list) < 3 and len(Shah_list) > 0:
        fitness_score -= 0.4
    if len(Song_list) < 3 and len(Song_list) > 0:
        fitness_score -= 0.4
    if len(Uddin_list) < 3 and len(Uddin_list) > 0:
        fitness_score -= 0.4
    if len(Zaman_list) < 3 and len(Zaman_list) > 0:
        fitness_score -= 0.4
    if len(Zein_el_Din_list) < 3 and len(Zein_el_Din_list) > 0:
        fitness_score -= 0.4
        
# checking to see if the two sections of CS 101 are more than 4 hours apart
    for gene in chromosome:            
        for gene1 in chromosome:
            if gene.name == "CS101A" and gene1.name == "CS101B":
                if abs(gene.time - gene1.time) > 4:
                    fitness_score += 0.5
                    
# checking to see if both sections of CS 101 are in the same time slot:
    for gene in chromosome:            
        for gene1 in chromosome:
            if gene.name == "CS101A" and gene1.name == "CS101B":
                if gene.time == gene1.time:
                    fitness_score -= 0.5 
                    
# checking to see if the two sections of CS 191 are more than 4 hours apart
    for gene in chromosome:            
        for gene1 in chromosome:
            if gene.name == "CS191A" and gene1.name == "CS191B":
                if abs(gene.time - gene1.time) > 4:
                    fitness_score += 0.5
                    
# checking to see if both sections of CS 191 are in the same time slot:
    for gene in chromosome:    
        for gene1 in chromosome:
            if gene.name == "CS191A" and gene1.name == "CS191B":
                if gene.time == gene1.time:
                    fitness_score -= 0.5
                    
# checking to see A section of CS 191 and a section of CS 101 are taught in consecutive time slots
    for gene in chromosome:    
        for gene1 in chromosome:
            if gene.name == "CS101A" or gene.name == "CS101B": 
                if gene1.name == "CS191A" or gene1.name == "CS191B":
                    if abs(gene.time - gene1.time) == 1:
                        fitness_score += 0.5
                        # one of the classes is in Bloch or Katz, and the other isn’t
                        if gene.room == "Bloch 119": 
                            if gene1.room == "FH 216" or gene1.room == "Royall 206" or gene1.room == "Royall 201" or gene1.room == "FH 310" or gene1.room == "Haag 201" or gene1.room == "Haag 301" or gene1.room == "MNLC 325":
                                fitness_score -= 0.4
                        if gene.room == "Katz 003":
                            if gene1.room == "FH 216" or gene1.room == "Royall 206" or gene1.room == "Royall 201" or gene1.room == "FH 310" or gene1.room == "Haag 201" or gene1.room == "Haag 301" or gene1.room == "MNLC 325":                            
                                fitness_score -= 0.4
# checking to see A section of CS 191 and a section of CS 101 are taught separated by 1 hour
    for gene in chromosome:    
        for gene1 in chromosome:
            if gene.name == "CS101A" or gene.name == "CS101B": 
                if gene1.name == "CS191A" or gene1.name == "CS191B":
                    if abs(gene.time - gene1.time) == 2:
                        fitness_score -= 0.25

# checking to see A section of CS 191 and a section of CS 101 are taught in the same time slot
    for gene in chromosome:    
        for gene1 in chromosome:
            if gene.name == "CS101A" or gene.name == "CS101B": 
                if gene1.name == "CS191A" or gene1.name == "CS191B":
                    if gene.time - gene1.time == 0:
                        fitness_score -= 0.25

# assigning the fitness score to the chromosome  
    new_chromosome = []
    for gene in chromosome:
        
        transformed_gene = [gene.name, gene.time, gene.room, gene.room_capacity, gene.instructor, gene.expected_enrollment, gene.preferred_instructors, gene.other_instructors, gene.remaining_instructors]
        new_chromosome.append(transformed_gene)
    new_chromosome.append(round(fitness_score, 2))
    
    return new_chromosome

def tournament_selection(chromosomes):
    # randomly select a subset of chromosomes from the population
    probabilities = []
    list_of_chromosome_index = []
    this_many_chromosomes = 0
    for chromosome in chromosomes:
        probabilities.append(chromosome[-1])
        list_of_chromosome_index.append(this_many_chromosomes)
        this_many_chromosomes += 1
    
    parent1 = np.random.choice(list_of_chromosome_index, 1, p = probabilities) # weights=(probabilities)) #, k=2)
    parent2 = np.random.choice(list_of_chromosome_index, 1, p = probabilities) # weights=(probabilities)) #, k=2)
    for parent in parent1:
        parent1 = chromosomes[parent]
    for parent in parent2:        
        parent2 = chromosomes[parent]
    # remove the fitness and probabilities from the chromosomes
    parent1 = [parent1[0],parent1[1],parent1[2],parent1[3],parent1[4],parent1[5],parent1[6],parent1[7],parent1[8],parent1[9]]
    parent2 = [parent2[0],parent2[1],parent2[2],parent2[3],parent2[4],parent2[5],parent2[6],parent2[7],parent2[8],parent2[9]]


    #parent1 = parents[0]
    #parent2 = parents[1]
    return parent1, parent2

def crossover(parent1, parent2):
    # randomly select a crossover point
    crossover_point = random.randint(0, len(parent1) - 1)
    # create the children
    child1 = parent1[:crossover_point] + parent2[crossover_point:] 
    child2 = parent2[:crossover_point] + parent1[crossover_point:] 
    # return the children
    return child1, child2

def mutation(child, pm, times, rooms, room_capacities, instructors, expected_enrollments, preferred_instructors, other_instructors, remaining_instructors):
    # mutate the child
    #look at each child each gene has a chance to mutate and mutation will mutate a random part of the gene
    for gene in child:
        if random.random() < pm:
            rand_gene = random.randint(1,4)
            if rand_gene == 1:
                gene[rand_gene] = random.choice(times)
            if rand_gene == 2:
                room_characteristic = random.randint(0, 8)
                gene[rand_gene] = rooms[room_characteristic]
                gene[rand_gene+1] = room_capacities[room_characteristic]
            if rand_gene == 4:
                gene[rand_gene] = random.choice(instructors)
    return child

# This is the main function that runs the genetic algorithm
if __name__=='__main__':
    
    # The following parameters are used in the genetic algorithm
    # The population size
    pop_size = 500
    # The number of generations
    num_gens = 100
    # The probability of crossover
    pc = 0.8
    # The probability of mutation
    pm = 0.007
    # The number of chromosomes in the tournament selection
    tournament_size = 2


    # The following parameters are used in the chromosome
    # The number of genes in the chromosome
    num_genes = 10
    # The number of classes
    num_classes = 10
    # The number of rooms
    num_rooms = 7
    # The number of times
    num_times = 6
    # The number of instructors
    num_instructors = 10

    # The list of courses
    courses = ['CS101A', 'CS101B', 'CS191A', 'CS191B', 'CS201', 'CS291', 'CS303', 'CS304', 'CS394', 'CS449', 'CS451']
    # The list of rooms
    rooms = ['Katz 003', 'FH 216', 'Royall 206', 'Royall 201', 'FH 310', 'Haag 201', 'Haag 301', 'MNLC 325', 'Bloch 119']
    # The list of class times (military time)
    times = [10, 11, 12, 13, 14, 15]
    # The list of instructors
    instructors = ['Gharibi', 'Gladbach', 'Hare', 'Nait-Abdesselam', 'Shah', 'Song', 'Uddin', 'Xu', 'Zaman', 'Zein el Din']
    # The room capacities
    room_capacities = [45, 30, 75, 50, 108, 60, 75, 450, 60]
    # The list of expected capacities
    expected_enrollment = [50, 50, 50, 50, 50, 50, 60, 25, 20, 60, 100]
    # The list of preferred instructors
    preferred_instructors_list = [['Gladbach', 'Gharibi', 'Hare', 'Zein el Din'], ['Gladbach', 'Gharibi', 'Hare', 'Zein el Din'], ['Gladbach', 'Gharibi', 'Hare', 'Zein el Din'], ['Gladbach', 'Gharibi', 'Hare', 'Zein el Din'], ['Gladbach', 'Hare', 'Zein el Din', 'Shah'], ['Gharibi', 'Hare', 'Zein el Din', 'Song'], ['Gladbach', 'Zein el Din', 'Hare'], ['Gladbach', 'Hare', 'Xu'], ['Xu', 'Song'], ['Xu', 'Song', 'Shah'], ['Xu', 'Song', 'Shah']]
    # The list of other instructors
    other_instructors_list = [['Zaman', 'Nait-Abdesselam'], ['Zaman', 'Nait-Abdesselam'], ['Zaman', 'Nait-Abdesselam'], ['Zaman', 'Nait-Abdesselam'], ['Zaman', 'Nait-Abdesselam', 'Song'], ['Zaman', 'Nait-Abdesselam', 'Shah', 'Xu'], ['Zaman', 'Song', 'Shah'], ['Zaman', 'Song', 'Shah', 'Nait-Abdesselam', 'Uddin', 'Zein el Din'], ['Nait-Abdesselam', 'Zein el Din'], ['Zein el Din', 'Uddin'], ['Zein el Din', 'Uddin', 'Nait-Abdesselam', 'Hare']]
     # adding the preferred and other instructors together
    acceptable_instructors_list = []
    for i in range(len(preferred_instructors_list)):
        acceptable_instructors_list.append(preferred_instructors_list[i] + other_instructors_list[i])
    # The remaining list of instructors that are not preferred instructors or other instructors
    remaining_instructors_list = []
    for instructor_list_count in range(num_classes):
        remaining_instructors = []
        for instructor in instructors:
            if instructor not in acceptable_instructors_list[instructor_list_count]:
                remaining_instructors.append(instructor)
        remaining_instructors_list.append(remaining_instructors)
       

    # The list of chromosomes
    chromosomes = []
    # The list of fitness values
    fitness_values = []
    # The list of probabilities
    probabilities = []
    # randomly generate the 500 chromosomes and determine their fitness values
    for i in range(pop_size):
        chromosome = []
        for j in range(num_genes):
            room_characteristic = random.randint(0, 8)
            genes = Course(courses[j], times[random.randint(0, 5)], rooms[room_characteristic], room_capacities[room_characteristic], instructors[random.randint(0, 9)], expected_enrollment[j], preferred_instructors_list[j], other_instructors_list[j], remaining_instructors_list[j])
            chromosome.append(genes)
        chromosome = fitness_function(chromosome, courses, rooms, times, instructors, room_capacities)
        chromosomes.append(chromosome)
    for chromosome in chromosomes:
        fitness_values.append(chromosome[-1])
    
# calculate each probability for each chromosome using softmax function
    sum = 0
    for fitness_value in fitness_values:
        sum = sum + math.exp(fitness_value)
    for fitness_value in fitness_values:
        probabilities.append(math.exp(fitness_value)/sum)
# adding the probabilities to each chromosome
    chrom_count = 0
    for chromosome in chromosomes:
        chromosome.append(probabilities[chrom_count])
        chrom_count = chrom_count + 1
       
# starting genetic algorithm
    average_old = 0
    gen_count = 0
    av_count = 0
    for generation in range(num_gens):
        # creating the new population
        gen_count += 1
        new_population = []
        # selecting parents based on a probability distribution
        for i in range(int(pop_size/2)):
            # select two parents using tournament selection
            parent1, parent2 = tournament_selection(chromosomes)

            
            # perform crossover
            child1, child2 = crossover(parent1, parent2)


            # perform mutation
            child1 = mutation(child1, pm, times, rooms, room_capacities, instructors, expected_enrollment, preferred_instructors_list, other_instructors_list, remaining_instructors)
            child2 = mutation(child2, pm, times, rooms, room_capacities, instructors, expected_enrollment, preferred_instructors_list, other_instructors_list, remaining_instructors)
            # add the children to the new population
            new_population.append(child1)
            new_population.append(child2)

        
        # transform the chromosomes from a list of lists to a list of objects so it can feed into the fitness function
        # The list of chromosomes
        chromosomes = []
        # The list of fitness values
        fitness_values = []
        # The list of probabilities
        probabilities = []
        for sexy_chomosome in new_population:
            chromosome = []
            for sexy_gene in sexy_chomosome:
                genes = Course(sexy_gene[0], sexy_gene[1], sexy_gene[2], sexy_gene[3], sexy_gene[4], sexy_gene[5], sexy_gene[6], sexy_gene[7], sexy_gene[8])
                chromosome.append(genes)
            chromosome = fitness_function(chromosome, courses, rooms, times, instructors, room_capacities)

            chromosomes.append(chromosome)
        
        for chromosome in chromosomes:
            fitness_values.append(chromosome[-1])
        
    # calculate each probability for each chromosome using softmax function
        sum = 0
        for fitness_value in fitness_values:
            sum = sum + math.exp(fitness_value)
        for fitness_value in fitness_values:
            probabilities.append(math.exp(fitness_value)/sum)
    # adding the probabilities to each chromosome
        chrom_count = 0
        for chromosome in chromosomes:
            chromosome.append(probabilities[chrom_count])
            chrom_count = chrom_count + 1   
    # tracking the evolution of the performance of the population  
        best_score = max(fitness_values)
        average = round(statistics.mean(fitness_values), 4)
        average_difference = average - average_old
        percent_difference_in_averages = round((average_difference/ average)*100,1)
        if 0 < percent_difference_in_averages < 1 and av_count == 0:
            av_count += 1
            print('\n', 'There is less than 1% difference in the averages between generation', gen_count - 1, ' and generation', gen_count, '\n'  )
        print('gen: ', gen_count,'  best: ', best_score, '  average: ', average, '  percent gain in averages: ', percent_difference_in_averages, '%' )
        average_old = average
########    
    # creating an out of the  best performing chromosome
    best_score = max(fitness_values)
    best_chromosome = chromosomes[fitness_values.index(best_score)]
    # removing the probability from the best chromosome
    best_chromosome = best_chromosome[:-1]
    # removing the fitness score from the best chromosome
    best_chromosome = best_chromosome[:-1]
    #listing only the important parts of the chromosome
    smaller_best_chromosome =[]
    for gene in best_chromosome:
        # 24 hour time to 12 hour time conversion
        str_time = str(gene[1])
        newds = datetime.datetime.strptime(str_time,'%H').strftime('%I %p')
        smaller_gene = [gene[0],newds,gene[2],gene[4]]
        smaller_best_chromosome.append(smaller_gene)



    print('\n','schedule fitness score: ', best_score)
    head = ["course", "time", "building/room", "instructor"]
    print(tabulate(smaller_best_chromosome, headers=head, tablefmt="grid"))
    