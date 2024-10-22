import matplotlib.pyplot as plt
import random


def plot_gantt_chart(job, machine_nums, process_time, setup_time):
    # 准备一系列颜色
    colors = ['blue', 'yellow', 'orange', 'green', 'palegoldenrod', 'purple', 'pink', 'Thistle', 'Magenta', 'SlateBlue',
              'RoyalBlue', 'Cyan', 'Aqua', 'floralwhite', 'ghostwhite', 'goldenrod', 'mediumslateblue', 'navajowhite',
              'moccasin', 'white', 'navy', 'sandybrown', 'moccasin']
    job_colors = random.sample(colors, len(job))
    # 计算每个工件的开始时间和结束时间
    start_time = [[] for _ in range(machine_nums)]
    end_time = [[] for _ in range(machine_nums)]

    job_loop = job[0]
    machine_loop = job[1]
    loop_length = len(job_loop)
    # for i in range(len(loop_length)):
        # start_time[machine_loop[i]] =


    id = [[] for _ in range(machine_nums)]
    job_color = [[] for _ in range(machine_nums)]

    job_id = job[0]

    # Calculate start time and end time.
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
