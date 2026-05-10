class Job:
    def __init__(self, job_id, deadline, profit):
        self.job_id = job_id
        self.deadline = deadline
        self.profit = profit


def job_scheduling(jobs):

    
    jobs.sort(key=lambda x: x.profit, reverse=True)

    # Step 2: Find maximum deadline
    max_deadline = max(job.deadline for job in jobs)

    
    slots = [-1] * max_deadline

    total_profit = 0
    scheduled_jobs = []

    for job in jobs:

        # Check slots from last to first
        for slot in range(job.deadline - 1, -1, -1):

            # If slot is empty
            if slots[slot] == -1:

                # Assign job
                slots[slot] = job.job_id

                total_profit += job.profit
                scheduled_jobs.append(job.job_id)

                break

    return scheduled_jobs, total_profit


jobs = [
    Job('A', 2, 100),
    Job('B', 1, 19),
    Job('C', 2, 27),
    Job('D', 1, 25),
    Job('E', 3, 15)
]

scheduled_jobs, profit = job_scheduling(jobs)

print("Scheduled Jobs:", scheduled_jobs)
print("Total Profit:", profit)