import random
import matplotlib.pyplot as plt
import copy

from src.setup_process_time_init.init_setup_process_time import get_setup_process_time
from src.chromosome_init.chromosome_initialize import chromosome_initialize
from src.pop_init.get_init_pop import get_init_pop
from src.cal_fitness.fitness import fitness
from src.pop_selection.selection import selection
from src.pop_crossover.crossover import crossover
from src.pop_mutation.mutation_bit import mutation_bit
from src.pop_mutation.mutation_swap import mutation_swap
from src.plot_gantt.plot_gantt_chart import plot_gantt_chart


# 定义遗传算法参数
POP_SIZE = 300  # 种群大小
MAX_GEN = 500  # 最大迭代次数
CROSSOVER_RATE = 0.75  # 交叉概率
MUTATION_RATE_SWAP = 0.15  # 变异概率
MUTATION_RATE_BIT = 0.2


# 主遗传算法循环
# 以最小化 makespan 为目标函数
# TODO: 没有考虑各机器的负载均衡
def GA(num_jobs, num_machines, mode):
    """
    :param num_jobs: <int>.
    :param num_machines: <int>.
    :param mode: <str>, 'greedy' or 'plain'. If 'greedy', do greedy assignment. Otherwise, assign machines randomly.
    :return:
    """
    process_time, setup_time = get_setup_process_time(num_jobs)

    chromosome, _, _ = chromosome_initialize(num_jobs, num_machines, process_time, setup_time)
    best_job = chromosome[1]  # Init any chromosome to get one init best_fitness.

    # "makespan" 是指完成整个生产作业或生产订单所需的总时间，通常以单位时间（例如小时或分钟）来衡量。
    best_makespan = fitness(chromosome, process_time, setup_time, num_machines)  # Set an init best_fitness.

    # The GA.
    fitness_history = []
    makespan_history = []
    pop = get_init_pop(POP_SIZE, process_time, num_jobs, num_machines, setup_time, mode=mode)
    for loop in range(1, MAX_GEN + 1):
        pop = selection(pop, POP_SIZE, process_time, setup_time, num_machines)  # 选择
        new_population = []

        while len(new_population) < POP_SIZE:
            parent1, parent2 = random.sample(pop, 2)  # 不重复抽样2个
            if random.random() < CROSSOVER_RATE:
                child1, child2 = crossover(parent1, parent2)  # 交叉
                new_population.extend([child1, child2])
            else:
                new_population.extend([parent1, parent2])

        # Mutation
        pop = [mutation_swap(job) if random.random() < MUTATION_RATE_SWAP else job for job in new_population]
        pop = [mutation_bit(job, num_machines) if random.random() < MUTATION_RATE_BIT else job for job in pop]

        best_gen_job = max(pop, key=lambda x: fitness(x, process_time, setup_time, num_machines))
        best_gen_makespan = fitness(best_gen_job, process_time, setup_time, num_machines)  # 每一次迭代获得最佳个体的适应度值

        if best_gen_makespan > best_makespan:  # 更新最大fitness值
            best_makespan = best_gen_makespan
            best_job = copy.deepcopy(best_gen_job)  # TODO: 不用deepcopy的话不会迭代，但是这里应该有更好的方法
        fitness_history.append(best_makespan)  # 把本次迭代结果保存到fitness_history中（用于绘迭代曲线）
        makespan_history.append(1 / best_makespan)
        if (loop % 20) == 0:
            print(f"In {loop}")
            # fitness_all = [1 / fitness(job, process_time, setup_time, num_machines) for job in pop]

    # 绘制迭代曲线图
    plt.plot(range(MAX_GEN), fitness_history)
    plt.xlabel('Iteration')
    plt.ylabel('Fitness')
    plt.title('Genetic Algorithm Convergence')
    plt.show()

    plt.plot(range(MAX_GEN), makespan_history)
    plt.xlabel('Iteration')
    plt.ylabel('Makespan')
    plt.title('Genetic Algorithm Convergence')
    plt.show()

    # Plot Gantt chart.
    plot_gantt_chart(best_job, num_machine, process_time, setup_time)

    return best_job, best_makespan


if __name__ == '__main__':
    num_job = 80
    num_machine = 15

    best_jobs, best_makespans = GA(num_job, num_machine, mode='greedy')

    print("最佳调度分配：\n", best_jobs)
    print("Min makespan：", 1 / best_makespans)
