import random
import numpy as np


def get_setup_process_time(num_jobs):
    G = 1000000
    setup_time = np.random.uniform(10, 15, (num_jobs + 2, num_jobs + 2))
    setup_time[0, :] = 0
    setup_time[1:, 0] = G
    setup_time[-1, :-1] = G
    setup_time[:, -1] = 0
    np.fill_diagonal(setup_time, 0)
    process_time = np.random.uniform(60, 150, num_jobs)

    return process_time, setup_time
