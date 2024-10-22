from src.chromosome_init.chromosome_initialize import chromosome_initialize
from src.cal_fitness.fitness import fitness
from Test.test_data import test_data


if __name__ == '__main__':
    process_time, num_jobs, num_machines, setup_time = test_data()
    chromosome, assignment_per_machine, completion_time = chromosome_initialize(num_jobs, num_machines,
                                                                                process_time, setup_time)
    fitness_value = fitness(chromosome, process_time, setup_time, num_machines)
    print(fitness_value)
    print(1 / fitness_value)
