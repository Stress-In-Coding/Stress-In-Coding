class Department:

    def __init__(self, name, departmentID):
        self.name = name
        self.departmentID = departmentID

    def display_info(self):
        print(f"Department Name: {self.name}")
        print(f"Department ID: {self.departmentID}")

department = Department("COLLEGE OF SCIENCES DEPARTMENT", 1)
department.display_info()