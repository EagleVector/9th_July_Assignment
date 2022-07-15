from class_variables import company
import logging as lg
lg.basicConfig(filename = 'oops.log', level = lg.DEBUG, format = '%(asctime)s %(levelname)s %(name)s %(message)s')
lg.info("We are importing the company module from class_variables package")

class services(company):
    def drone_development(self):
        """Drones are the future. We make drone solutions"""

        try:
            lg.info("We provide drone solutions")
            return "DRONES"

        except Exception as e:
            lg.exception(e)

    def mobileapp_development(self):
        """Android and ios application development"""

        try:
            lg.info("We build cool mobile applications")
            return "MOBILE APPS"

        except Exception as e:
            lg.exception(e)

    def cloud_solution(self):
        """Cloud Management"""

        try:
            lg.info("We provide cloud solutions")
            return "CLOUD SERVICES"

        except Exception as e:
            lg.exception(e)

    def startup_building(self):
        """Let's build it together"""

        try:
            lg.info("We provide startup solutions")
            return "STARTUP SOLUTION"

        except Exception as e:
            lg.exception(e)

    def business_solutions(self):
        """WE INCREASE THE BUSINESS REVENUE"""

        try:
            lg.info("We provide business solutions")
            return "BUSINESS SOLUTIONS"

        except Exception as e:
            lg.exception(e)

    def training(self):
        """SELLING QUALITY COURSES"""

        try:
            lg.info("We provide quality education and mentorship")
            return "TRAINING PROGRAM"

        except Exception as e:
            lg.exception(e)

    def internship(self):
        """REAL TIME PROJECTS FOR INTERNSHIP"""

        try:
            lg.info("We provide free internships to everyone")
            return "GLOBAL INTERNSHIP PROGRAM"

        except Exception as e:
            lg.exception(e)

try:
    service = services('Sudhanshu Kumar', 'Krish Naik', 'Hitesh Choudhary', 'Manoj Kumar', 'Darius', 15, 20, 10, 18, 12)

    lg.info("services are: %s", service.drone_development())

    lg.info("services are: %s", service.mobileapp_development())

    lg.info("services are: %s", service.cloud_solution())

    lg.info("services are: %s", service.startup_building())

    lg.info("services are: %s", service.business_solutions())

    lg.info("services are: %s", service.training())

    lg.info("services are: %s", service.internship())

except Exception as e:
    lg.exception(e)