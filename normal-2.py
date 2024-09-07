from task import (
    Resource,
    Node,
    Edge,
    Task,
    Job,
    TaskType,
    generate_tasks,
    generate_resources,
    CriticallyEDF,
)
import random as rand

rand.seed(20)

num_resources = rand.randint(1, 5)
resources = generate_resources(resource_count=num_resources)
num_tasks = rand.randint(5, 10)
tasks = generate_tasks(
    resources=resources, task_count=num_tasks, ratio=0, utilization_ub=2
)

speedup_factor_list = [1, 1.5, 1.6, 1.7, 2]

y = []
missed_deadline_count = []
for speedup_factor in speedup_factor_list:
    cedf = CriticallyEDF(
        tasks=tasks, resources=resources, speedup_factor=speedup_factor, verbose=False
    )
    if cedf.schedule():
        cedf.visualize(
            show=False, save=True, title=f"Critically EDF - Speedup Factor {speedup_factor}", filename=f"normal-speedup{speedup_factor}"
        )
        print(f"Schedulable with speedup factor {speedup_factor} and QoS is {cedf.quality_of_service()}")
        y.append(cedf.quality_of_service())
        missed_deadline_count.append(cedf.missed_deadline_count())
    else:
        print("Speedup factor failed ", speedup_factor)
        cedf.visualize(
            show=False, save=True, filename=f"normal-speedup{speedup_factor}"
        )
        y.append(0)

import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax.plot(speedup_factor_list, y, marker="o")
ax.set_xlabel("Speedup Factor")
ax.set_ylabel("Quality of Service")
fig.savefig("normal-speedup-factor-quality-of-service.png")


fig, ax = plt.subplots()
ax.plot(speedup_factor_list, missed_deadline_count, marker="o")
ax.set_xlabel("Speedup Factor")
ax.set_ylabel("Missed Deadline Count")
fig.savefig("normal-speedup-factor-missed-deadline-count.png")
