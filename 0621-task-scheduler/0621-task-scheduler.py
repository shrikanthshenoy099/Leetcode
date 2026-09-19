class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks.sort()
        max_freq = 0
        curr = 1
        count_max = 0
        # Getting the task with most frequency and how many of those are there
        for i in range(1, len(tasks)):
            if tasks[i] == tasks[i-1]:
                curr += 1
            else:
                if curr == max_freq:
                    count_max += 1
                elif curr > max_freq:
                    max_freq = curr
                    count_max = 1
                curr = 1

        if curr == max_freq:
            count_max += 1
        elif curr > max_freq:
            max_freq = curr
            count_max = 1
        
        return max(len(tasks), (max_freq - 1) * (n + 1) + count_max)
        # max_freq is used here as gaps between tasks
        # n + 1 is because there are n + 1 task blocks
        # count_max accounts for anything additional due to multiple max_freq