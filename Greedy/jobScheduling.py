class Job:
    
    # Job class which stores profit and deadline.
    
    def __init__(self,profit=0,deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id =       
class Solution:
    # Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self, Jobs, n):
        Jobs.sort(key=lambda x: x.profit, reverse=True)
        
     
        result = [False] * n
        job = ['-1'] * n
        
        total_profit = 0
        count_jobs = 0
      
        for i in range(len(Jobs)):
            for j in range(min(n, Jobs[i].deadline) - 1, -1, -1):
                if result[j] is False:
                    result[j] = True
                    job[j] = Jobs[i].id
                    total_profit += Jobs[i].profit
                    count_jobs += 1
                    break
        
        return count_jobs, total_profit
