from src.pop_init.get_init_pop import get_init_pop
from src.pop_selection.selection import selection
from Test.test_data import test_data


if __name__ == '__main__':
    POP_SIZE = 20
    process_time, num_jobs, num_machines, setup_time = test_data()
    pop = get_init_pop(POP_SIZE, process_time, num_jobs, num_machines, setup_time)
    selected = selection(pop, POP_SIZE, process_time, setup_time, num_machines)
    print(selected)
