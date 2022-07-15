import logging as lg
lg.basicConfig(filename = 'oops.log', level = lg.DEBUG, format = '%(asctime)s %(levelname)s %(name)s %(message)s')
lg.info("POLYMORPHISM")
lg.info("SUDHANSHU SIR HAS MANY AVATARS")
class CEO:
    def SUDHANSHU_KUMAR(self):
        try:
            lg.info("Sudhanshu Kumar is the CEO of ineuron")
            return "CEO ROLE"

        except Exception as e:
            lg.exception(e)

class Developer:
    def SUDHANSHU_KUMAR(self):
        try:
            lg.info("Sudhanshu Kumar is a chief developer in ineuron")
            return "DEVELOPER ROLE"

        except Exception as e:
            lg.exception(e)

class Mentor:
    def SUDHANSHU_KUMAR(self):
        try:

            lg.info("Sudhanshu Kumar is a mentor for data courses in ineuron")
            return "MENTOR ROLE"

        except Exception as e:
            lg.exception(e)

class Owner:
    def SUDHANSHU_KUMAR(self):
        try:
            lg.info("Sudhanshu Kumar is the owner of ineuron")
            return "OWNER ROLE"

        except Exception as e:
            lg.exception(e)

class Motivator:
    def SUDHANSHU_KUMAR(self):
        try:
            lg.info("Sudhanshu Kumar is motivator in ineuron")
            return "MOTIVATOR ROLE"

        except Exception as e:
            lg.exception(e)

class FRIEND:
    def SUDHANSHU_KUMAR(self):
        try:

            lg.info("Sudhanshu Kumar is everyone's friend")
            return "FRIEND ROLE"

        except Exception as e:
            lg.exception(e)

class Youtuber:
    def SUDHANSHU_KUMAR(self):
        try:

            lg.info("Sudhanshu Kumar is a Famous Youtuber")
            return "YOUTUBER"

        except Exception as e:
            lg.exception(e)

class Entrepreneur:
    def SUDHANSHU_KUMAR(self):
        try:

            lg.info("Sudhanshu Kumar is an Entrepreneur")
            return "ENTREPRENEUR"

        except Exception as e:
            lg.exception(e)

try:
    def call(a):
        a.SUDHANSHU_KUMAR()

    a1 = CEO()
    a2 = Developer()
    a3 = Mentor()
    a4 = Motivator()
    a5 = Owner()
    a6 = FRIEND()
    a7 = Youtuber()
    a8 = Entrepreneur()

    lg.info(call(a1))

    lg.info(call(a2))

    lg.info(call(a3))

    lg.info(call(a4))

    lg.info(call(a5))

    lg.info(call(a6))

    lg.info(call(a7))

    lg.info(call(a8))

except Exception as e:
    lg.exception(e)