# PROBLEM DESCRIPTION
# Subproblem
# f(i, C) = max value we can pack amonst A[i...n] with knapsack capacity C

# Want f(1, W)

# Recurrence Relations
# f(i, C) = {
#           (no more items left)
#           0,          if i = n + 1
#           
#           (current item larger than available capacity)
#           f(i + 1, C),          if w[i] > C
# 
#           (otherwise, we take max of taking the curr item or not taking the curr item)
#           max{
#                f(i + 1, C),
#                v[i] + f(i + 1, C - w[i])
#               },          otherwise
# }

def knapsack(weights, profits, capacity):

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
            item_index = i - 1
            selected_items.append(item_index)
            size -= weights[item_index]

    # returns items selected
    selected_items.reverse()
    return selected_items

    # returns max profit
    # return mem[n][capacity]

if __name__ == '__main__':
    # capacity = 10
    # profits = [1, 4, 8, 5]
    # weights = [3, 3, 5, 6]
    # print(knapsack(weights, profits, capacity)); # 12


    capacity = 7
    profits = [2, 2, 4, 5, 3]
    weights = [3, 1, 3, 4, 2]
    print(knapsack(weights, profits, capacity)); # 10