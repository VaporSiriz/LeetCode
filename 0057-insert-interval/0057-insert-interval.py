class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        due_union_start = 100001
        due_union_end = -1
        new_start, new_end = newInterval[0], newInterval[1]
        for interval in intervals:
            start, end = interval[0], interval[1]

            if (new_start <= end and end <= new_end) or \
               (new_start <= start and start <= new_end) or \
               (start <= new_start and new_end <= end):
                    if due_union_start>=start:
                        due_union_start = start
                    if due_union_end<=end:
                        due_union_end = end
            else:
                result.append(interval)

        if due_union_start>=new_start:
            due_union_start = new_start
        if due_union_end<=new_end:
            due_union_end = new_end


        result.append([due_union_start, due_union_end])
        if len(result)==0:
            result.append([new_start, new_end])
        result.sort()
        return result