from src.setup_process_time_init.init_setup_process_time import get_setup_process_time


if __name__ == '__main__':
    num_jobs = 20
    num_machines = 5
    process_time, setup_time = get_setup_process_time(num_jobs, num_machines)
    print(process_time, setup_time)
