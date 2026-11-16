# BROKEN: Late Binding
def create_workers():
    workers = []
    for i in range(3):
        workers.append(lambda: i)
    return workers


# workers[0]() returns 2! All lambdas point to the same 'i' which ends up as 2.


# FIXED: Default Argument Binding
def create_workers_fixed():
    workers = []
    for i in range(3):
        workers.append(lambda local_val=i: local_val)  # Evaluates 'i' at creation time
    return workers


# since default arguments are created a t compile time
