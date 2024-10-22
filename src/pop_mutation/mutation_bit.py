import random


# bit mutation
def mutation_bit(job, num_machines):
    index = random.randint(0, len(job[0]) - 1)
    job[1][index] = random.randint(1, num_machines)
    return job
