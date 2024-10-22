from src.utils.utils import cal_break_point


# swap mutation
def mutation_swap(job):
    break_point = cal_break_point(len(job[0]))
    mutation1 = break_point[0]
    mutation2 = break_point[1]
    tmp1 = job[0][mutation1]
    tmp2 = job[1][mutation1]
    job[0][mutation1] = job[0][mutation2]
    job[1][mutation1] = job[1][mutation2]
    job[0][mutation2] = tmp1
    job[1][mutation2] = tmp2
    return job
