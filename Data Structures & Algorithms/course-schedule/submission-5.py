class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hashmap = {i:[] for i in range(numCourses)}

        check = []
        if not prerequisites:
            return True
        for course, prereq in prerequisites:
            hashmap[course].append(prereq)
            
        def dfs(course):
            if course in check:
                return False
            if hashmap[course] == []:
                return True
            check.append(course)
            for c in hashmap[course]:
                if not dfs(c):
                    return False
            check.remove(course)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True




        