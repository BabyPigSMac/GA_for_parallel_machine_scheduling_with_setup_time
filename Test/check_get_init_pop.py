from Test.test_data import test_data
from src.pop_init.get_init_pop import get_init_pop


if __name__ == '__main__':
    POP_SIZE = 5
    process_time, num_jobs, num_machines, setup_time = test_data()
    pop = get_init_pop(POP_SIZE, process_time, num_jobs, num_machines, setup_time, mode='plain')
    print(pop)
    for population in pop:
        print(population)
        print(population[0, 2])
        break

