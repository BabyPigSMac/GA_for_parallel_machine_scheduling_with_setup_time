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


# 定义遗传算法参数
POP_SIZE = 300  # 种群大小
MAX_GEN = 500  # 最大迭代次数
CROSSOVER_RATE = 0.75  # 交叉概率
MUTATION_RATE_SWAP = 0.15  # 变异概率
MUTATION_RATE_BIT = 0.2


# 主遗传算法循环
# 以最小化 makespan 为目标函数
# TODO: 没有考虑各机器的负载均衡
def GA(num_jobs, num_machines):  # 工件加工顺序是否为无序
    process_time, setup_time = get_setup_process_time(num_jobs)

    chromosome, _, _ = chromosome_initialize(num_jobs, num_machines, process_time, setup_time)
    best_job = chromosome[1]  # 获得最佳个体

    # "makespan" 是指完成整个生产作业或生产订单所需的总时间，通常以单位时间（例如小时或分钟）来衡量。
    best_makespan = fitness(chromosome, process_time, setup_time, num_machines)  # 获得最佳个体的适应度值
    # 创建一个空列表来存储每代的适应度值
    # fitness_history = [best_makespan]
    fitness_history = []
    makespan_history = []

    pop = get_init_pop(POP_SIZE, process_time, num_jobs, num_machines, setup_time)
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

    print(fitness_history[:10])
    # 绘制迭代曲线图
    plt.plot(range(MAX_GEN), fitness_history)
    plt.xlabel('Generation')
    plt.ylabel('Fitness Value')
    plt.title('Genetic Algorithm Convergence')
    plt.show()

    return best_job, best_makespan, process_time, setup_time


def plot_gantt(job, machine_nums):
    # 准备一系列颜色
    colors = ['blue', 'yellow', 'orange', 'green', 'palegoldenrod', 'purple', 'pink', 'Thistle', 'Magenta', 'SlateBlue',
              'RoyalBlue', 'Cyan', 'Aqua', 'floralwhite', 'ghostwhite', 'goldenrod', 'mediumslateblue', 'navajowhite',
              'moccasin', 'white', 'navy', 'sandybrown', 'moccasin']
    job_colors = random.sample(colors, len(job))
    # 计算每个工件的开始时间和结束时间
    start_time = [[] for _ in range(machine_nums)]
    end_time = [[] for _ in range(machine_nums)]
    id = [[] for _ in range(machine_nums)]
    job_color = [[] for _ in range(machine_nums)]

    job_id = job[0]

    for i in range(len(job)):
        if start_time[job[i]]:
            start_time[job[i]].append(max(end_time[job[i]][-1], arr_times[job_id[i]]))
            end_time[job[i]].append(start_time[job[i]][-1] + pro_times[job_id[i]])
        else:
            start_time[job[i]].append(arr_times[job_id[i]])
            end_time[job[i]].append(start_time[job[i]][-1] + pro_times[job_id[i]])
        id[job[i]].append(job_id[i])
        job_color[job[i]].append(job_colors[job_id[i]])

    # 创建图表和子图
    plt.figure(figsize=(12, 6))

    # 绘制工序的甘特图
    for i in range(len(start_time)):
        for j in range(len(start_time[i])):
            plt.barh(i, end_time[i][j] - start_time[i][j], height=0.5, left=start_time[i][j], color=job_color[i][j],
                     edgecolor='black')
            plt.text(x=(start_time[i][j] + end_time[i][j]) / 2, y=i, s=id[i][j], fontsize=14)

    # 设置纵坐标轴刻度为机器编号
    machines = [f'Machine {i}' for i in range(len(start_time))]
    plt.yticks(range(len(machines)), machines)

    # 设置横坐标轴刻度为时间
    # start = min([min(row) for row in start_time])
    start = 0
    end = max([max(row) for row in end_time])
    plt.xticks(range(start, end + 1))
    plt.xlabel('Time')

    # 图表样式设置
    plt.ylabel('Machines')
    plt.title('Gantt Chart')
    # plt.grid(axis='x')

    # 自动调整图表布局
    plt.tight_layout()

    # 显示图表
    plt.show()


if __name__ == '__main__':
    num_job = 40
    num_machine = 10

    best_jobs, best_makespans, process_time, setup_time = GA(num_job, num_machine)

    print("最佳调度分配：\n", best_jobs)
    print("最小 makespan：", 1 / best_makespans)
    # plot_gantt(best_jobs, process_time, setup_time)
