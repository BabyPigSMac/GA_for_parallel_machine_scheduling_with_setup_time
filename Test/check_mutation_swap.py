from Test.test_data import test_data
from src.chromosome_init.chromosome_initialize import chromosome_initialize
from src.pop_mutation.mutation_swap import mutation_swap


if __name__ == '__main__':
    POP_SIZE = 5
    process_time, num_jobs, num_machines, setup_time = test_data()
    chromosome, _, _ = chromosome_initialize(num_jobs, num_machines, process_time, setup_time)
    print(chromosome)
    print(mutation_swap(chromosome))
