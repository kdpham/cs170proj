import docplex.mp
import sys
import docplex.cp
from docplex.cp.model import *
from docplex.mp.model import *
from multiprocessing import Process
import time
import os

FILE_SIZE = "small"

def idkman(filename):
    #filename = 'medium-65.in'
    file = open("inputs/" + "largeRedos/vm2/" + filename, 'r').read().split()  ## Change this line
    size = int(file[0])

    stress_max = float(file[1])

    stress = {}
    happiness = {}


    for i in range(2, len(file)):
        if i % 4 == 2:
            first = int(file[i])
            second = int(file[i+1])
            happiness[(first, second)] = float(file[i+2])
            stress[(first, second)] = float(file[i+3])

    maxScore = 0
    bestSolution = None
    bestK = 0


    for k in range(1,size+1):
        model = Model(name='cs170')
        # x_roomi, person1, person2 --> binary variables
        x = {(room, person): model.binary_var(name='x_{0}_{1}'.format(room, person)) for room in range(k) for person in range(size)}
        #x = {(room, person1, person2): model.binary_var(name='x_{0}_{1}_{2}'.format(room, person1, person2)) for room in range(size) for (person1, person2) in happiness}
        y = {(room, person1, person2): model.binary_var(name='y_{0}_{1}_{2}'.format(room, person1, person2)) for room in range(k) for (person1, person2) in happiness}
        aux_y = {(room, person1, person2): model.binary_var(name='aux_y_{0}_{1}_{2}'.format(room, person1, person2)) for room in range(k) for (person1, person2) in happiness}

        stress_rooms = {room: model.continuous_var(name = 'stress_{0}'.format(room)) for room in range(k)}
        happiness_rooms = {room: model.continuous_var(name = 'happiness_{0}'.format(room)) for room in range(k)}

        # happiness and stress
        for i in range(k):
            for (j,m) in happiness:
                model.add_constraint(y[(i,j,m)] <= x[(i,j)])
                model.add_constraint(y[(i,j,m)] <= x[(i,m)])
                model.add_constraint(y[(i,j,m)] >= x[(i,j)] - 2*aux_y[(i,j,m)])
                model.add_constraint(y[(i,j,m)] >= x[(i,m)] - 2*(1-aux_y[(i,j,m)]))

        for i in range(k):
            model.add_constraint(happiness_rooms[i] == model.sum(y[(i,j,m)] * happiness[(j, m)] for (j,m) in happiness))
            model.add_constraint(stress_rooms[i] == model.sum(y[(i,j,m)] * stress[(j, m)] for (j,m) in happiness))

        for i in range(k):
            model.add_constraint(k * stress_rooms[i] <= stress_max)

        # person only in one room

        for j in range(size):
            model.add_constraint(model.sum(x[(i, j)] for i in range(k)) == 1)

        model.maximize(model.sum(happiness_rooms[i] for i in range(k)))
        model.set_time_limit(120)
        solution = model.solve()
        try:
            if (solution.get_objective_value() > maxScore):
                maxScore = solution.get_objective_value()
                bestSolution = solution
                bestK = k
            print(filename + ", room size " + str(k) + ", solution found")
        except:
            print(filename + ", room size " + str(k) + ", no solution")

    print(filename + " " + str(maxScore))
    print(" ")

    output_filename = (filename.split("."))[0] + ".out"
    new_file = open(os.getcwd() + '/' + 'outputs' + '/largeRedos/' + output_filename, "a")   # output is student space room

    for student in range(size):
        for room in range(bestK):
            variable_name = 'x_' + str(room) + '_' + str(student)
            if bestSolution.get_value(variable_name) == 1:
                string = str(student) + ' ' + str(room) + '\n'
                new_file.write(string)


    new_file.close()






def main():
     # directory = 'inputs/small' for small inputs, large etc.
    for filename in os.listdir(os.getcwd() + "/inputs/largeRedos/vm3"): ## Change this line as well
        start = time.time()
        if filename == 'large-110.in':
            idkman(filename)
        end = time.time()
        print(start-end)

    
main()
