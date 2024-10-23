import matplotlib.pyplot as plt
import random


def plot_gantt_chart(job, machine_nums, process_time, setup_time):
    """
    The function is to plot Gantt chart.
    :param job:
    :param machine_nums:
    :param process_time:
    :param setup_time:
    :return:
    """
    # Prepare color.
    colors = ['blue', 'yellow', 'orange', 'green', 'palegoldenrod', 'purple', 'pink', 'Thistle', 'Magenta', 'SlateBlue',
              'RoyalBlue', 'Cyan', 'Aqua', 'floralwhite', 'ghostwhite', 'goldenrod', 'mediumslateblue', 'navajowhite',
              'moccasin', 'white', 'navy', 'sandybrown', 'moccasin', 'darkred', 'darkgreen', 'darkblue', 'darkorange',
              'darkviolet', 'darkcyan', 'darkgray', 'darkmagenta', 'lightblue', 'lightgreen', 'lightcyan', 'lightgray',
              'lightyellow', 'xkcd:sky blue', 'xkcd:light green', 'xkcd:rose', 'xkcd:teal', 'xkcd:lavender',
              'xkcd:mustard', 'xkcd:grey', 'xkcd:olive', 'xkcd:cyan', 'xkcd:maroon', 'crimson', 'lime', 'indigo',
              'gold', 'orchid', 'aquamarine', 'silver', 'khaki', 'fuchsia', 'sienna', 'aliceblue', 'antiquewhite',
              'aqua', 'aquamarine', 'azure', 'beige', 'bisque', 'black', 'blanchedalmond', 'blue', 'blueviolet',
              'brown', 'burlywood', 'cadetblue', 'chartreuse', 'chocolate', 'coral', 'cornflowerblue', 'cornsilk',
              'crimson', 'cyan', 'darkblue', 'darkcyan', 'darkgoldenrod', 'darkgray', 'darkgreen', 'darkkhaki',
              'darkmagenta', 'darkolivegreen', 'darkorange', 'darkorchid', 'darkred', 'darksalmon', 'darkseagreen',
              'darkslateblue', 'darkslategray', 'darkturquoise', 'darkviolet', 'deeppink', 'deepskyblue', 'dimgray',
              'dodgerblue', 'firebrick', 'floralwhite', 'forestgreen', 'fuchsia', 'gainsboro', 'ghostwhite', 'gold',
              'goldenrod', 'gray', 'green', 'greenyellow', 'honeydew', 'hotpink', 'indianred', 'indigo', 'ivory',
              'khaki', 'lavender', 'lavenderblush', 'lawngreen', 'lemonchiffon', 'lightblue', 'lightcoral', 'lightcyan',
              'lightgoldenrodyellow', 'lightgray', 'lightgreen', 'lightpink', 'lightsalmon', 'lightseagreen',
              'lightskyblue', 'lightslategray', 'lightsteelblue', 'lightyellow', 'lime', 'limegreen', 'linen',
              'magenta', 'maroon', 'mediumaquamarine', 'mediumblue', 'mediumorchid', 'mediumpurple', 'mediumseagreen',
              'mediumslateblue', 'mediumspringgreen', 'mediumturquoise', 'mediumvioletred', 'midnightblue', 'mintcream',
              'mistyrose', 'moccasin', 'navajowhite', 'navy', 'oldlace', 'olive', 'olivedrab', 'orange', 'orangered',
              'orchid', 'palegoldenrod', 'palegreen', 'paleturquoise', 'palevioletred', 'papayawhip', 'peachpuff',
              'peru', 'pink', 'plum', 'powderblue', 'purple', 'red', 'rosybrown', 'royalblue', 'saddlebrown', 'salmon',
              'sandybrown', 'seagreen', 'seashell', 'sienna', 'silver', 'skyblue', 'slateblue', 'slategray', 'snow',
              'springgreen', 'steelblue', 'tan', 'teal', 'thistle', 'tomato', 'turquoise', 'violet', 'wheat', 'white',
              'whitesmoke', 'yellow', 'yellowgreen']
    job_colors = random.sample(colors, len(job[0]))
    # Calculate start time and end time of each job assigned to each machine.
    job_machine_pair = [[] for _ in range(machine_nums)]    # Records the jobs assigned to each machine.
    start_time = [[] for _ in range(machine_nums)]
    end_time = [[] for _ in range(machine_nums)]
    duration = [[] for _ in range(machine_nums)]

    # For each machine(with machine_id), find jobs in machine.
    for job_name, machine in zip(job[0], job[1]):
        job_machine_pair[machine - 1].append(job_name)

    # For each job, get last job name, end time of the last job, setup time and process time. Then (1) add start time of
    # the next job to be end time of the last job plus the setup time, (2) add end time of the next job to be start time
    # of the next job plus process time. (3) add duration of the next job to be end time - start time.  Record last job
    # name, end time.
    # In particular, if the first job, init end time = 0, last job name = 0.
    for idx, job_list in enumerate(job_machine_pair):
        last_job = 0
        last_end_time = 0
        for job_name in job_list:
            job_start_time = last_end_time + setup_time[last_job, job_name]
            last_end_time = job_start_time + process_time[job_name - 1]
            start_time[idx].append(job_start_time)
            end_time[idx].append(last_end_time)
            duration[idx].append(last_end_time - job_start_time)
            last_job = job_name

    # Plot Gantt chart, with first element to be machine_id, second element to be duration, 'left' element to be start
    # time.
    plt.figure(figsize=(12, 6))
    for machine_idx in range(machine_nums):
        machine_name = 'machine ' + str(machine_idx + 1)
        for job_list_idx in range(len(job_machine_pair[machine_idx])):
            plt.barh(machine_name, duration[machine_idx][job_list_idx], height=0.5,
                     left=start_time[machine_idx][job_list_idx],
                     color=job_colors[job_machine_pair[machine_idx][job_list_idx] - 1],
                     edgecolor='black')
            plt.text(x=(start_time[machine_idx][job_list_idx] + end_time[machine_idx][job_list_idx]) / 2,
                     y=machine_idx, s=job_machine_pair[machine_idx][job_list_idx], fontsize=14)

    # 图表样式设置
    plt.xlabel('Time')
    plt.ylabel('Machines')
    plt.title('Gantt Chart')
    plt.grid(axis='x')

    # 自动调整图表布局
    plt.tight_layout()

    # 显示图表
    plt.show()
