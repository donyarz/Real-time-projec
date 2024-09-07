from task import Resource, Node, Edge, Task, Job, TaskType, generate_tasks, generate_resources, CriticallyEDF
import random as rand

rand.seed(5)

num_resources = rand.randint(1, 5)
resources = generate_resources(resource_count=num_resources)
num_tasks = rand.randint(5, 10)
tasks = generate_tasks(resources=resources, task_count=num_tasks, ratio=0.5, utilization_ub=1)

cedf = CriticallyEDF(tasks=tasks, resources=resources, speedup_factor=1, verbose=True)
try:
    cedf.schedule()
    cedf.visualize(show=False, save=True, filename="normal-1")
except Exception as e:
    print(e)
    pass