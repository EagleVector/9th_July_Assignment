import logging as lg
lg.basicConfig(filename = 'oops.log', level = lg.DEBUG, format = '%(asctime)s %(levelname)s %(name)s %(message)s')
lg.info("ABSTRACTION")

class compensation:
    __acc_holders_name = "Subham Kumar"
    __acc_no = 12345678
    __aadhar_no = "0987 8765 3456 6784"
    __salary = 40000
    __month = "JULY"
    __date = "15/07/2022"
    __bank_name = "ICICI"
    __branch_ifsc = "icici1234567"
    __city = "Bengaluru"

    def name(self):
        try:
            lg.info("Employee Name: %s", compensation.__acc_holders_name)
            return "NAME ENTERED SUCCESSFULLY"

        except Exception as e:
            lg.exception(e)

    def account(self):
        try:
            lg.info("Account Number: %s", compensation.__acc_no)
            return "ACCOUNT NUMBER ENTERED SUCCESSFULLY"

        except Exception as e:
            lg.exception(e)

    def aadhar(self):
        try:
            lg.info("Aadhar Number: %s", compensation.__aadhar_no)
            return "AADHAR NUMBER ENTERED SUCCESSFULLY"

        except Exception as e:
            lg.exception(e)

    def salary(self):
        try:
            lg.info("Salary: %s", compensation.__acc_no)
            return "SALARY ENTERED SUCCESSFULLY"

        except Exception as e:
            lg.exception(e)

    def month(self):
        try:
            lg.info("Month: %s", compensation.__month)
            return "MONTH ENTERED SUCCESSFULLY"

        except Exception as e:
            lg.exception(e)

    def date(self):
        try:
            lg.info("Date: %s", compensation.__date)
            return "DATE ENTERED SUCCESSFULLY"

        except Exception as e:
            lg.exception(e)

    def bankname(self):
        try:
            lg.info("Bank Name: %s", compensation.__bank_name)
            return "BANK NAME ENTERED SUCCESSFULLY"

        except Exception as e:
            lg.exception(e)

    def ifsc(self):
        try:
            lg.info("Branch IFSC: %s", compensation.__branch_ifsc)
            return "BRANCH IFSC ENTERED SUCCESSFULLY"

        except Exception as e:
            lg.exception(e)

    def city(self):
        try:
            lg.info("City: %s", compensation.__city)
            return "CITY ENTERED SUCCESSFULLY"

        except Exception as e:
            lg.exception(e)

try:
    record = compensation()

    lg.info(record.name())

    lg.info(record.account())

    lg.info(record.aadhar())

    lg.info(record.salary())

    lg.info(record.bankname())

    lg.info(record.month())

    lg.info(record.date())

    lg.info(record.ifsc())

    lg.info(record.city())


except Exception as e:
    lg.exception(e)