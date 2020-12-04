import docplex.mp
import sys
import docplex.cp
from docplex.cp.model import *
from docplex.mp.model import *
from multiprocessing import Pool

def idkman(filename):
    #filename = 'medium-65.in'
    file = open(directory + '/' + filename, 'r').read().split()
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
        model.set_time_limit(20)
        solution = model.solve()
        try:
            if (solution.get_objective_value() > maxScore):
                maxScore = solution.get_objective_value()
                bestSolution = solution
            print("solution found")
        except:
            print("no solution")

    print(filename + " " + str(maxScore))
    print(" ")


directory = 'inputs/medium'
for filename in os.listdir(directory):
    p = Process(target=idkman, args=(filename,))
    p.start()
    p.join()