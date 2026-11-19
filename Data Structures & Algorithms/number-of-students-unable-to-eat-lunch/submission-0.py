class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        res = len(students)
        cnt = Counter(students)

        for i in sandwiches:
            if cnt[i] > 0:
                res -= 1
                cnt[i] -= 1
            else:
                break
        return res