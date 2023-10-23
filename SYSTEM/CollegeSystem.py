class CollegeOfScience:

    def __init__(self):
        self._college_dean = ""
        self._programs = ""
        self._location = ""

    def college_dean(self):
        return self._college_dean

    def college_dean(self, dean):
        self._college_dean = dean

    def programs(self):
        return self._programs

    def programs(self, programs):
        self._programs = programs

    def location(self):
        return self._location

    def location(self, location):
        self._location = location

    def display_info(self):
        print(f"College Dean: {self.college_dean}")
        print(f"Programs: {self.programs}")
        print(f"Location: {self.location}")


college = CollegeOfScience()
college.college_dean = "sir. Edilberto Ona"
college.programs = "ACS, SITE, ESSA, YBA, MBS, "
college.location = "College of Science Building"
college.display_info()


class CSG:

   def __init__(self, officer_name, officer_id, position):
       self.officer_name = officer_name
        self.officer_id = officer_id
       self.position = position

   def display_officer_details(self):
       print(f"Officer Name: {self.officer_name}")
        print(f"Officer ID: {self.officer_id}")
        print(f"Position: {self.position}")
Create a CSG object
officer = CSG(" Aneza Jamion", "2022-8-0050", "Assistant Secretary")

# Display officer details
officer.display_officer_details()