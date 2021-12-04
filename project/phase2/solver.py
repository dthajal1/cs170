from Task import Task
from parse import read_input_file, write_output_file
import os

## PROBLEM DESCRIPTION
# given a list of n igloos to polish with id i, deadline t_i in minutes, duration d_i in minutes, and profit p_i, 
# provide a sequence of igloos to polish in one day (1440 minutes) that would maximize the total profit.

## CONSTRAINTS
# 1. start scheduling polishing tasks at the 0th minute of the day.

# 2. start the next polishing task at the same minute we finish the previous polishing task

# 3. We receive whole profit for tasks that complete any time before or on their deadline. 
# ex. if a task has d=5 and t=10, we get the whole profit p if we schedule it at any time before minute 5
# (including at minute 5) because it would complete by minute 10. 
# If we schedule this task at minute 6, we would
# complete it by minute 11, and gain profit corresponding to completing the task 1 minute late.
# late profit = p_i * e ** (−0.0170 * s_i)
# s_i = number of mins late

# 4. We can schedule tasks such that the last task completes by minute 1440, 
# For example, we can schedule a task with duration 1 at minute 1439 since it would complete by minute 1440




## DP APPROACH
# Hints for DP Heuristics (assumes additional constraints that will make the problem easier to solve)
# 1. assume late tasks have 0 payoffs (for simplicity) ---- ignore for now

# 2. Another example of a DP heuristic you could make is  ------ use this
#               you could assume that tasks are always completed in order of id 
#               (so 1 2 5 6 12 is a valid schedule, but 1 5 2 6 12 is not). 
#               Then, you could design algorithm similar to knapsack around this assumption.


# Parameters: n, i, t_i, d_i, p_i
# Sub Problem:
# f(i, T) = max total profit we can gain amonst tasks[i....n] before minute T

# want: f(1, 1440)

# Recurrence Relation
# i = current igloo, T = # of mins available
# f(i, T) = 
# {
#             (no more igloos left to polish)
#             0,             if i == n + 1   
# 
#             (cannot be finished before 1440 so we can't polish this igloo)
#             f(i + 1, T)    if d_i > T (maybe d_i >= T)? 
# 
#             (otherwise) -- this also handles the case where later tasks have earlier deadline (if the late profit is still positive it will polish it otherwise, it won't polish it)
#             (if we can polish the igloo, we take maximum of polishing the igloo or not polishing the igloo)
#             max{ 
#                   f(i + 1, T)     ----- don't polish the igloo
#                   p_i + f(i + 1, T - d_i)    ------ polish the igloo
#               }           
# }


# knapsack extended to fit the requirement of polishing igloos problem
def knapsack_dp_extended(weights, profits, deadlines, capacity):
    n = len(weights)

    # initialize a mem/lookup table for bottom up approach (fill up table iteratively)
    # row represents items, cols represent capacity
    mem = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)] # first row is a dummy sentinel row to make calculations easier

    for i in range(n + 1):
        for c in range(capacity + 1):
            if (i == 0) or (c == 0): # sentinel
                mem[i][c] = 0
            elif (weights[i - 1] <= c): # if possible to take the current item, take max(with_curr, without_curr)
                with_curr = profits[i - 1] + mem[i - 1][c - weights[i - 1]]
                without_curr = mem[i - 1][c]
                mem[i][c] = max(with_curr, without_curr)
            else: # not possible to take curr item
                mem[i][c] = mem[i - 1][c]

    selected_items = []
    size = capacity
    for i in range(n, 0, -1):
        if (mem[i][size] != mem[i - 1][size]):
            selected_items.append(i)
            size -= weights[i - 1] # accounts for 1-indexed

    # returns items selected
    selected_items.reverse()
    return selected_items

    # returns max profit
    # return mem[n][capacity]

def solve(tasks):
    """
    Args:
        tasks: list[Task], list of igloos to polish
    Returns:
        output: list of igloos in order of polishing  
    """

    weights = [task.get_duration() for task in tasks]
    profits = [task.get_max_benefit() for task in tasks]
    deadlines = [task.get_deadline() for task in tasks]
    capacity = 1440

    return knapsack_dp_extended(weights, profits, deadlines, capacity)




    # Greedy Methods
    # 1. sort the task in decreasing order w.r.t. profit
    # i.e. finish task that has maximum profit first
    # sorted_tasks = sorted(tasks, key=lambda task: task.get_max_benefit(), reverse=True)
    # return [task.get_task_id() for task in sorted_tasks]

    # 2. sort the task in increasing order w.r.t. duration
    # i.e. finish task that the least amount of time first
    # sorted_tasks = sorted(tasks, key=lambda task: task.get_duration(), reverse=False)
    # return [task.get_task_id() for task in sorted_tasks]

    # 3. sort the task in increasing order w.r.t. deadline
    # i.e. finish task that have earliest deadline first
    sorted_tasks = sorted(tasks, key=lambda task: task.get_deadline(), reverse=False)
    # keep_going = True
    # i = 0
    # result = []
    # while keep_going:
    #     # if ((i < len(sorted_tasks)) and sorted_tasks[i].get_deadline())
    #     i += 1

    # return result
    return [task.get_task_id() for task in sorted_tasks]


# Here's an example of how to run your solver.
if __name__ == '__main__':
    # for input_path in os.listdir('inputs/'):
    #     output_path = 'outputs/' + input_path[:-3] + '.out'
    #     tasks = read_input_file(input_path)
    #     output = solve(tasks)
    #     write_output_file(output_path, output)

    # testing
    tasks = [Task(1, 3, 3, 2), Task(2, 8, 1, 2), Task(3, 3, 3, 4), Task(4, 8, 4, 5), Task(5, 3, 2, 3)]
    result = solve(tasks)
    print(result)