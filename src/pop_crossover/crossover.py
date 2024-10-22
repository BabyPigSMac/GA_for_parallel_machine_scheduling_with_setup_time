import numpy as np

from src.utils.utils import cal_break_point


def crossover_for_part(all_parent1, all_parent2, break_point, length_parent):
    parent1 = all_parent1[0]
    parent2 = all_parent2[0]
    inbetween1 = parent1[break_point[0]:break_point[1]]
    inbetween2 = parent2[break_point[0]:break_point[1]]
    loop1 = np.concatenate((parent1[break_point[1]:], parent1[:break_point[1]]))
    loop2 = np.concatenate((parent2[break_point[1]:], parent2[:break_point[1]]))
    loop1_machine = np.concatenate((all_parent1[1][break_point[1]:], all_parent1[1][:break_point[1]]))
    loop2_machine = np.concatenate((all_parent2[1][break_point[1]:], all_parent2[1][:break_point[1]]))

    offspring1 = np.copy(parent1)
    offspring2 = np.copy(parent2)
    offspring1_machine = np.copy(all_parent1[1])
    offspring2_machine = np.copy(all_parent2[1])
    delay1 = 0
    delay2 = 0
    for i in range(length_parent - len(inbetween1)):
        index = (break_point[1] + i) % (length_parent)
        while loop1[i + delay2] in inbetween2:
            delay2 += 1
        offspring2[index] = loop1[i + delay2]
        offspring2_machine[index] = loop1_machine[i + delay2]

        while loop2[i + delay1] in inbetween1:
            delay1 += 1
        offspring1[index] = loop2[i + delay1]
        offspring1_machine[index] = loop2_machine[i + delay1]
    return np.array((offspring1, offspring1_machine)), np.array((offspring2, offspring2_machine))


# Apply order crossover, OX1 1985.
def crossover(parent1, parent2):
    # Get point.
    length_parent = len(parent1[0])
    break_point = cal_break_point(length_parent)
    offspring1, offspring2 = crossover_for_part(parent1, parent2, break_point, length_parent)
    return offspring1, offspring2
