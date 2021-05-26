class Garden:
    def __init__(self, diagram, students=None):
        if not students:
            students = [
                "Alice", "Bob", "Charlie",
                "David", "Eve", "Fred",
                "Ginny", "Harriet", "Ileana",
                "Joseph", "Kincaid", "Larry"
            ]

        self.diagram = diagram.split("\n")
        self.students = sorted(students)
        self.plant_map = {"G": "Grass", "C": "Clover", "R": "Radishes", "V": "Violets"}

    def plants(self, child):
        index = self.students.index(child)
        keys = self.diagram[0][index*2:index*2+2] + self.diagram[1][index*2:index*2+2]
        return [self.plant_map[p] for p in keys]
