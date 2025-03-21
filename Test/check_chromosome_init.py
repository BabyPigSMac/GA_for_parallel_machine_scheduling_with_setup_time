from src.chromosome_init.chromosome_initialize import chromosome_initialize
from Test.test_data import test_data


if __name__ == '__main__':
    process_time, num_jobs, num_machines, setup_time = test_data()
    chromosome, assignment_per_machine, completion_time = chromosome_initialize(num_jobs, num_machines, process_time,
                                                                                setup_time, mode='plain')
    print(chromosome)
