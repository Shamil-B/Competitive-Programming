class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {course:[] for course in range(numCourses)}
        dep = {course:0 for course in range(numCourses)}

        for course,pre in prerequisites:
            graph[pre].append(course)
            dep[course] += 1
            
        sources = []
        for course in range(numCourses):
            if dep[course]==0:
                sources.append(course)
            
        q = deque(sources)
        coursesCompleted = []
        while q:
            course = q.popleft()
            coursesCompleted.append(course)
            
            for otherCourse in graph[course]:
                dep[otherCourse] -= 1
                
                if dep[otherCourse]==0:
                    q.append(otherCourse)
                    
                    
        if len(coursesCompleted)!=numCourses:
            return []
        
        return coursesCompleted