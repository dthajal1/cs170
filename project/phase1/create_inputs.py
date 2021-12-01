from Task import Task
from parse import write_input_file
import random

def write_n_tasks(path, n):
    file_to_write_to = 'inputs/' + path + '.in'
    tasks = []
    for task_id in range(1, n + 1):
        deadline = random.randint(1, 1440)
        duration = random.randint(1, 60)
        random_int = random.randint(0, 3)
        if random_int == 0:
            perfect_benefit = random.randint(1, 99)
        elif random_int == 1:
            perfect_benefit = round(random.uniform(1, 98), 1)
        elif random_int == 2:
            perfect_benefit = round(random.uniform(1, 98), 2)
        else:
            perfect_benefit = round(random.uniform(1, 98), 3)
        new_task = Task(task_id, deadline, duration, perfect_benefit)
        tasks.append(new_task)

    write_input_file(file_to_write_to, tasks)

def create_input():
    write_n_tasks('100', 100)
    write_n_tasks('150', 150)
    write_n_tasks('200', 200)    
    
create_input()