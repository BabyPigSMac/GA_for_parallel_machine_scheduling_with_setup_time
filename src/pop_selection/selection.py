import numpy as np

from src.cal_fitness.fitness import fitness


# 选择父代，这里选择POP_SIZE/2个作为父代
def selection(pop, POP_SIZE, process_time, setup_time, machine_num):
    fitness_values = [1 / fitness(job, process_time, setup_time, machine_num) for job in pop]  # 以最小化交货期总延时为目标函数，这里把最小化问题转变为最大化问题
    total_fitness = sum(fitness_values)
    prob = [fitness_value / total_fitness for fitness_value in fitness_values]  # 轮盘赌，这里是每个适应度值被选中的概率
    # 按概率分布prob从区间[0,len(pop))中随机抽取size个元素，不允许重复抽取，即轮盘赌选择
    selected_indices = np.random.choice(len(pop), size=POP_SIZE // 2, p=prob, replace=False)
    return [pop[i] for i in selected_indices]
