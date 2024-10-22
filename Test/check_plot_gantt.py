from src.chromosome_init.chromosome_initialize import chromosome_initialize
from src.plot_gantt.plot_gantt_chart import plot_gantt_chart
from Test.test_data import test_data

if __name__ == '__main__':
    process_time, num_jobs, num_machines, setup_time = test_data()
    chromosome, _, _ = chromosome_initialize(num_jobs, num_machines, process_time, setup_time)
    print(chromosome)
    plot_gantt_chart(chromosome, num_machines, process_time, setup_time)
