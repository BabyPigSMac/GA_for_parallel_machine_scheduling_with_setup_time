from src.pop_crossover.crossover import crossover
from src.pop_init.get_init_pop import get_init_pop
from Test.test_data import test_data


if __name__ == '__main__':
    POP_SIZE = 20
    process_time, num_jobs, num_machines, setup_time = test_data()
    pop = get_init_pop(POP_SIZE, process_time, num_jobs, num_machines, setup_time)
    parent1 = pop[1]
    parent2 = pop[2]
    child1, child2 = crossover(parent1, parent2)
    print('Parent')
    print(parent1)
    print(parent2)
    print('Child')
    print(child1)
    print(child2)
