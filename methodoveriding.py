import logging as lg
lg.basicConfig(filename = 'oops.log', level = lg.DEBUG, format = '%(asctime)s %(levelname)s %(name)s %(message)s')
lg.info("METHOD OVERRIDING")
class courses:
    def internship(self, mentor):
        """INTERNSHIP FOR ALL STUDENTS"""
        try:
            lg.info("Job Guarantee Programs by : %s", mentor)
            lg.info("Internship available for all students")
            return "INEURON"

        except Exception as e:
            lg.exception(e)

class fsds(courses):
    def internship(self, mentor):
        """INTERNSHIP FOR ALL STUDENTS"""
        try:
            lg.info("Mentor for this course will be: %s", mentor)
            lg.info("Internship available for Data Science")
            return "FSDS"

        except Exception as e:
            lg.exception(e)

class fsda(courses):
    def internship(self, mentor):
        """INTERNSHIP FOR ALL STUDENTS"""
        try:
            lg.info("Mentor for this course will be: %s", mentor)
            lg.info("Internship available for Data Analytics")
            return "FSDA"

        except Exception as e:
            lg.exception(e)

class fswd(courses):
    def internship(self, mentor):
        """INTERNSHIP FOR ALL STUDENTS"""
        try:
            lg.info("Mentor for this course will be: %s", mentor)
            lg.info("Internship available for Web Development")
            return "FSWD"

        except Exception as e:
            lg.exception(e)

class cpp(courses):
    def internship(self, mentor):
        """INTERNSHIP FOR ALL STUDENTS"""
        try:
            lg.info("Mentor for this course will be: %s", mentor)
            lg.info("Internship available for IOT")
            return "CPP"

        except Exception as e:
            lg.exception(e)

class js(courses):
    def internship(self, mentor):
        """INTERNSHIP FOR ALL STUDENTS"""
        try:
            lg.info("Mentor for this course will be: %s", mentor)
            lg.info("Internship available for Enterprise Java with Springboot.")
            return "JSS"

        except Exception as e:
            lg.exception(e)

class csm(courses):
    def internship(self, mentor):
        """INTERNSHIP FOR ALL STUDENTS"""
        try:
            lg.info("Mentor for this course will be: %s", mentor)
            lg.info("Internship available for Cyber Security")
            return "CSM"

        except Exception as e:
            lg.exception(e)

class blockchain(courses):
    def internship(self, mentor):
        """INTERNSHIP FOR ALL STUDENTS"""
        try:
            lg.info("Mentor for this course will be: %s", mentor)
            lg.info("Internship available for blockchain")
            return "BLOCKCHAIN"

        except Exception as e:
            lg.exception(e)

class DM(courses):
    def internship(self, mentor):
        """INTERNSHIP FOR ALL STUDENTS"""
        try:
            lg.info("Mentor for this course will be: %s", mentor)
            lg.info("Internship available for Digital Marketing")
            return "DIGITAL MARKETING"

        except Exception as e:
            lg.exception(e)

try:
    enroll = courses()

    lg.info("course1: %s", enroll.internship("Ineuron"))

    enroll1 = fsds()

    lg.info("course1: %s", enroll1.internship("Sudhanshu Kumar"))

    enroll2 = fsda()

    lg.info("course1: %s", enroll2.internship("Krish Naik"))

    enroll3 = fswd()

    lg.info("course1: %s", enroll3.internship("Hitesh Choudhary"))

    enroll4 = cpp()

    lg.info("course1: %s", enroll4.internship("Sourav Shukla"))

    enroll5 = js()

    lg.info("course1: %s", enroll5.internship("Navin Reddy"))

    enroll6 = csm()

    lg.info("course1: %s", enroll6.internship("Saksham Choudhary"))

    enroll7 = blockchain()

    lg.info("course1: %s", enroll7.internship("Navin Reddy"))

    enroll8 = DM()

    lg.info("course1: %s", enroll8.internship("Mahatmaji"))


except Exception as e:
    lg.exception(e)