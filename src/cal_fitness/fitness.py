# 计算染色体的适应度（makespan） 以最小化 makespan(min maxC_j) 目标函数
# Fitness = 1 / (max C_j)
def fitness(job, process_time, setup_time, machine_num):
    """
    Cal the fitness of one job. The fitness is 1 / (max C_j).
    :param job: An array which contains two arrays, with the first array representing jobs, and the second machines,e.g.
        [[9, 7, 3, 8, 4, 6, 5, 1, 2],
        [3, 1, 1, 2, 2, 3, 1, 2, 3]]
        <np.array> 2 * len(job)
    :param process_time: <array> 1 * len(job)
        [11, 15, 12, 13, 14, 17, 12, 13, 11]
    :param setup_time: <np.array> ((len(job)) * (len(job)+2))
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
    :param machine_num: <int> num of machines.
    :return: <float>
        fitness of the assignment, 1 / makespan.
    """
    # For machine_{idx}, say, machine_3, get sequence [9, 6, 2], cal completion time,
    # process_time[9] + setup_time[0, 9] + process_time[6] + setup_time[9, 6] + process_time[2] + setup_time[6, 2]
    completion_times = []
    for machine_id in range(1, machine_num+1):
        # Get where idx == machine_id
        tmp_job = [job for job, machine in zip(job[0], job[1]) if machine == machine_id]
        this_completion_time = 0
        for idx, this_job in enumerate(tmp_job):
            if idx == 0:
                this_completion_time += process_time[this_job - 1] + setup_time[0, this_job]
            else:
                this_completion_time += process_time[this_job - 1] + setup_time[tmp_job[idx-1], this_job]
        # Record completion time.
        completion_times.append(this_completion_time)

    # Then get max completion time.
    return 1 / max(completion_times)
