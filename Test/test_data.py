import numpy as np


def test_data():
    G = 1000000
    process_time = np.array([11, 15, 12, 13, 14, 17, 12, 13, 11])
    num_jobs = len(process_time)
    num_machines = 3
    setup_time = np.array(
        [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [G, 0, 2, 3, 2, 3, 2, 1, 2, 3, 0],
         [G, 1, 0, 3, 2, 3, 2, 1, 2, 3, 0],
         [G, 1, 2, 0, 2, 3, 2, 1, 2, 3, 0],
         [G, 1, 2, 3, 0, 3, 2, 1, 2, 3, 0],
         [G, 1, 2, 3, 2, 0, 2, 1, 2, 3, 0],
         [G, 1, 2, 3, 2, 3, 0, 1, 2, 3, 0],
         [G, 1, 2, 3, 2, 3, 2, 0, 2, 3, 0],
         [G, 1, 2, 3, 2, 3, 2, 1, 0, 3, 0],
         [G, 1, 2, 3, 2, 3, 2, 0, 2, 0, 0],
         [G, G, G, G, G, G, G, G, G, G, 0]]
    )
    return process_time, num_jobs, num_machines, setup_time
