import numpy as np


def find_earliest_completion_time(completion_time):
    min_time = 1000000
    time_count = 1
    machine_idxes = []
    for index, time in enumerate(completion_time):
        if time < min_time:
            min_time = time
            time_count = 1
            machine_idxes = [index]  # Reset the machine_idxes
        elif time == min_time:
            time_count += 1
            machine_idxes.append(index)
    return machine_idxes, time_count, min_time


def find_min_setup_time(job, setup_time, machine_idxes, assignment_per_machine):
    min_time = 10000
    time_count = 1
    min_time_machine_idxes = []
    for machine_id in machine_idxes:
        last_job = assignment_per_machine[machine_id][-1]
        this_setup_time = setup_time[last_job, job]
        if this_setup_time < min_time:
            min_time = this_setup_time
            time_count = 1
            min_time_machine_idxes = [machine_id]
        elif this_setup_time == min_time:
            time_count += 1
            min_time_machine_idxes.append(machine_id)

    return min_time_machine_idxes, time_count, min_time


def chromosome_initialize(num_jobs, num_machines, process_time, setup_time):
    """
    The function is to init chromosome with greedy assignment procedure. Returns one piece of chromosome.
    :param process_time: <np.array>, 1 * num_jobs
        [11, 15, 12, 13, 14, 17, 12, 13, 11]
    :param setup_time: <np.array>
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
        [G, G, G, G, G, G, G, G, G, G, 0],]
    :param num_jobs: <int>, representing number of jobs.
    :param num_machines: <int>, representing number of machines.
    :return: <np.array>, 2 * len(job), with the first representing jobs, and the second machines.
        An array which contains two arrays, with the first array representing jobs, and the second machines,e.g.
        [[9, 7, 3, 8, 4, 6, 5, 1, 2],
        [3, 1, 1, 2, 2, 3, 1, 2, 3]].
    """
    # Create a permutation of the n jobs
    permutation = np.arange(1, num_jobs + 1)
    np.random.shuffle(permutation)
    completion_time = np.zeros(num_machines)   # Record of completion time.
    assignment = np.zeros(num_jobs)     # Array for assignment of jobs, which is the second row of the return.
    assignment_per_machine = [[] for _ in range(num_machines)]

    for idx, job in enumerate(permutation):
        # Find the machine with the earliest completion time.
        machine_idxes, time_count, min_completion_time = find_earliest_completion_time(completion_time)
        if min_completion_time == 0:
            # If no job in machine, just assign it to the first machine found.
            assignment[idx] = machine_idxes[0] + 1
            completion_time[machine_idxes[0]] += process_time[job - 1]
            assignment_per_machine[machine_idxes[0]].append(job)
            continue

        # Now every machine has at least one job in queue.
        if time_count == 1:
            # Do assignment & update completion time.
            assignment[idx] = machine_idxes[0] + 1
            last_job = assignment_per_machine[machine_idxes[0]][-1]
            completion_time[machine_idxes[0]] += process_time[job - 1] + setup_time[last_job, job]
            assignment_per_machine[machine_idxes[0]].append(job)
        else:
            # Compare setup time.
            min_setup_time_machine_idxes, setup_time_count, min_setup_time = find_min_setup_time(job, setup_time,
                                                                                                 machine_idxes,
                                                                                                 assignment_per_machine)
            setup_time_machine_id = min_setup_time_machine_idxes[0]
            assignment[idx] = setup_time_machine_id + 1
            completion_time[setup_time_machine_id] += process_time[job - 1] + min_setup_time
            assignment_per_machine[setup_time_machine_id].append(job)
    chromosome = np.array([permutation, assignment], dtype=int)
    return chromosome, assignment_per_machine, completion_time
