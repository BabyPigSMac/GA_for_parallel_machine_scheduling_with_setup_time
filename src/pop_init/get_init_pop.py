import random
from src.chromosome_init.chromosome_initialize import chromosome_initialize


# 随机生成初始种群，工件和机器编码都是从1开始
def get_init_pop(pop_size, process_time, num_jobs, num_machines, setup_time, mode='plain'):
    pop = []
    for _ in range(pop_size):
        choose = []
        for _ in range(num_jobs):
            chromosome, _, _ = chromosome_initialize(num_jobs, num_machines, process_time, setup_time, mode=mode)
        pop.append(chromosome)
    return pop
