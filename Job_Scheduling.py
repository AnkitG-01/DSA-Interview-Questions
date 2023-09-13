'''
Job Sequencing Problem

Given a set of N jobs where each jobi has a deadline and profit associated with it.

Each job takes 1 unit of time to complete and only one job can be scheduled at a time. We earn the profit associated with job if and only if the job is completed by its deadline.

Find the number of jobs done and the maximum profit.

Note: Jobs will be given in the form (Jobid, Deadline, Profit) associated with that Job.


Example 1:

Input:
N = 4
Jobs = {(1,4,20),(2,1,10),(3,1,40),(4,1,30)}
Output:
2 60

Explanation:
Job1 and Job3 can be done with
maximum profit of 60 (20+40).

Example 2:

Input:
N = 5
Jobs = {(1,2,100),(2,1,19),(3,2,27),
        (4,1,25),(5,1,15)}
Output:
2 127

Explanation:
2 jobs can be done with
maximum profit of 127 (100+27).

'''
class Job:
     def __init__(self,profit=0,deadline=0):
          self.profit=profit
          self.deadline=deadline
          self.id=0
          
def JobScheduling(jobs,n):
        jobs.sort(key=lambda x:x.profit,reverse=True)
        max_d=0
        for job in jobs:
            if job.deadline>max_d:
                max_d=job.deadline
        schedule=[-1]*max_d
        count=0
        profit=0
        for job in jobs:
            if schedule[job.deadline-1]==-1:
                schedule[job.deadline-1]=job.id
                profit+=job.profit
                count+=1
            else:
                for i in range(job.deadline-1,0,-1):
                    if schedule[i-1]==-1:
                        schedule[i-1]=job.id
                        profit+=job.profit
                        count+=1
                        break
        return [count,profit]