import logging as lg
lg.basicConfig(filename = 'oops.log', level = lg.DEBUG, format = '%(asctime)s %(levelname)s %(name)s %(message)s')
lg.info("ENCAPSULATION")

class employee:
    def __init__(self):
        self.__name = "Subham Kumar"
        self.__role = "Developer"
        self.__yob = 1996
        self.__salary = 50000
        self.__hours_per_week = 40
        self.__benefits = ['HRA' , 'TA']
        self.city = "Bengaluru"
        self.week_off = ['Saturday' , 'Sunday']

    def mod_role(self):
        try:
            self.__role = "Senior Developer"
            lg.info("New role: %s", self.__role)
            return "ROLE UPDATED"

        except Exception as e:
            lg.exception(e)

    def mod_salary(self):
        try:
            self.__salary = 70000
            lg.info("New salary: %s", self.__salary)
            return "SALARY UPDATED"

        except Exception as e:
            lg.exception(e)

    def mod_workhours(self):
        try:
            self.__hours_per_week = 45
            lg.info("Workhours per week: %s", self.__hours_per_week)
            return "NEW WORK HOURS UPDATED"

        except Exception as e:
            lg.exception(e)

    def mod_benefits(self):
        try:
            self.__benefits = ['HRA', 'TA', 'LTA']
            lg.info("New benefits: %s", self.__benefits)
            return "BENEFITS UPDATED"

        except Exception as e:
            lg.exception(e)

try:
    emp1 = employee()
    lg.info("Your Current Working city is: %s", emp1.city)
    emp1.city = 'Chennai'
    lg.info("Your Current Working city is changed to %s", emp1.city)
    lg.info("Your Current Role is %s", emp1._employee__role)
    lg.info(emp1.mod_role())
    lg.info("Your Current Salary is %s", emp1._employee__salary)
    lg.info(emp1.mod_salary())
    lg.info("Your Current working hours per week is %s", emp1._employee__hours_per_week)
    lg.info(emp1.mod_workhours())
    lg.info("Your Current Benefits are %s", emp1._employee__benefits)
    lg.info(emp1.mod_benefits())
    lg.info("Your Current Week Off is: %s", emp1.week_off)
    emp1.week_off = ['Monday' , 'Tuesday']
    lg.info("Your Updated Week Off is: %s", emp1.week_off)
except Exception as e:
    lg.exception(e)