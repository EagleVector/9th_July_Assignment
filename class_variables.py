import logging as lg
lg.basicConfig(filename = 'oops.log', level = lg.DEBUG, format = '%(asctime)s %(levelname)s %(name)s %(message)s')

class company :
    def __init__(self, CEO, CFO, CTO, CBO, CMO, dev_count, analyst_count, support_count, mle_count, devops_count):
        """Examples of class variables"""
        lg.info("Classification of class variables as public, private and protected.")

        self.CEO = CEO
        self.CFO = CFO
        self.CTO = CTO
        self.__CBO = CBO
        self.__CMO = CMO
        self.__dev_count = dev_count
        self._analyst_count = analyst_count
        self._support_count = support_count
        self._mle_count = mle_count
        self._devops_count = devops_count

try:
    lg.info("Creating an object of the class company")
    ineuron = company('Sudhanshu Kumar', 'Krish Naik', 'Hitesh Choudhary', 'Manoj Kumar', 'Darius', 15, 20, 10, 18, 12)

    lg.info("CEO of ineuron is: %s", ineuron.CEO)

    lg.info("CFO of ineuron is: %s", ineuron.CFO)

    lg.info("CTO of ineuron is: %s", ineuron.CTO)

    lg.info("CBO of ineuron is: %s", ineuron._company__CBO)

    lg.info("CMO of ineuron is: %s", ineuron._company__CMO)

    lg.info("Total developers in ineuron is: %s", ineuron._company__dev_count)

    lg.info("Total analyst in ineuron is: %s", ineuron._analyst_count)

    lg.info("Total support team in ineuron is: %s", ineuron._support_count)

    lg.info("Total mle in ineuron is: %s", ineuron._mle_count)

    lg.info("Total devops in ineuron is: %s", ineuron._devops_count)


except Exception as e:
    lg.exception(e)