from collections import defaultdict


class School:
    def __init__(self):
        self.grades = defaultdict(list)
        self.grade_list = set()
        self.all = []

    def add_student(self, name, grade):
        self.grades[grade].append(name)
        self.grade_list.add(grade)
        self.all.append(name)

    def roster(self):
        arr = []
        for grade in sorted(self.grade_list):
            arr.extend(self.grade(grade))
        return arr

    def grade(self, grade_number):
        return sorted(self.grades[grade_number])
