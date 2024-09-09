from collections import defaultdict

class CourseScheduler:
    def __init__(self):
        self.graph = defaultdict(list)
        self.courses = set()

    def add_course(self, course, prerequisites=None):
        self.courses.add(course)
        if prerequisites:
            for prerequisite in prerequisites:
                self.graph[prerequisite].append(course)
                self.courses.add(prerequisite)  

    def detect_cycle(self):
        visited = set()
        rec_stack = set()    #recursive stack , when performing dfs if we encounter node that is in rec_stack then we may have cyclic dependency

        def dfs(course):
            if course in rec_stack:  #cycle is detected
                return True
            if course in visited:     # no cycle is detected
                return False

            visited.add(course)
            rec_stack.add(course)

            for neighbor in self.graph[course]:
                if dfs(neighbor):
                    return True

            rec_stack.remove(course)
            return False

        for course in self.courses:   # check for dependent  prerequisites courses
            if course not in visited:
                if dfs(course):
                    return True
        return False

    def topological_sort_util(self, course, visited, stack):
        visited.add(course)

        for neighbor in self.graph[course]:
            if neighbor not in visited:
                self.topological_sort_util(neighbor, visited, stack)

        stack.append(course)

    def topological_sort(self):
        visited = set()
        stack = []

        for course in self.courses:
            if course not in visited:
                self.topological_sort_util(course, visited, stack)

        stack.reverse()  # Reverse the stack to get the correct topological order 
        return stack

    def generate_training_plan(self): # to generate training plan
        if self.detect_cycle():
            print("Cycle detected in course prerequisites. Scheduling not possible.")
            return None

        order = self.topological_sort()
        if order:
            print("Training Plan (Course Order):")
            for i, course in enumerate(order, 1):
                print(f"{i}. {course}")
            return order
        else:
            print("Unable to determine a valid course order.")
            return None

scheduler = CourseScheduler()

# Adding courses with prerequisites ("course",["prereq"])

scheduler.add_course("CourseA")
scheduler.add_course("CourseB", ["CourseA"])  
scheduler.add_course("CourseC", ["CourseA","CourseB"])  
scheduler.add_course("CourseD",["CourseC"])

''' Running these creates a cyclic dependency as a -> c , b -> a, c-> b
scheduler.add_course("CourseA",["CourseC"])
scheduler.add_course("CourseB",["CourseA"]) 
scheduler.add_course("CourseC",["CourseB"]) 
''' 
scheduler.generate_training_plan() 