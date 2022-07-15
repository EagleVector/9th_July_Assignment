import logging as lg
lg.basicConfig(filename = 'oops.log', level = lg.DEBUG, format = '%(asctime)s %(levelname)s %(name)s %(message)s')
lg.info("INHERITANCE")

class ineuron:
    lg.info("Parent Class")
    def __init__(self, student_name, user_id, password):
        self.student_name = student_name
        self._user_id = user_id
        self.__password = password

    def courses(self):
        """Courses Availability"""
        try:
            lg.info("Multiple Courses are Available in all tech domains")
            return "GO TO COURSES"

        except Exception as e:
            lg.exception(e)


    def internship(self):
        """Internship options"""
        try:
            lg.info("Students are eligible for free internships")
            return "FREE INTERNSHIP"

        except Exception as e:
            lg.exception(e)


    def one_neuron(self):
        """NETFLIX FOR EDUCATION"""
        try:
            lg.info("OTT platform for a range of demanding quality courses")
            return "OTT FOR EDUCATION"

        except Exception as e:
            lg.exception(e)


class ineuron_intelligence(ineuron):
    lg.info("Inherited class")
    def Research(self):
        """Research centre"""
        try:
            lg.info("Research team for product development")
            return "R&D centre for product development"

        except Exception as e:
            lg.exception(e)

class ineuron_solutions(ineuron_intelligence):
    lg.info("Inherited sub class")
    def Solutions(self):
        """Solution centre"""
        try:
            lg.info("Dev Team for app development")
            return "Business solutions to the company"

        except Exception as e:
            lg.exception(e)

try:
    i = ineuron_solutions("Subham Kumar", 1234, "!@#$")
    lg.info("Name of Student is: %s", i.student_name)
    lg.info("Courses: %s", i.courses())
    lg.info("Internship: %s", i.internship())
    lg.info("OTT: %s", i.one_neuron())
    lg.info("OTT: %s", i.Research())
    lg.info("OTT: %s", i.Solutions())

except Exception as e:
    lg.exception(e)