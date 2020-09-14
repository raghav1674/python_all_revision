import logging,re
logging.basicConfig(filename="myexception1.log",level=logging.DEBUG)

class InvalidPasswordException(Exception):

    def __init__(self,msg):
        logging.warning("RAISING EXCEPTION")

        self.msg=msg
    def display_exception(self):
        print(self.msg)

def password_validator(pwd):
    try:
        logging.info("VALIDATING PASSWORD")

        if len(pwd)<8:

            raise InvalidPasswordException("PLEASE ENTER THE VALID PASSWORD ")
    except InvalidPasswordException as e:
        e.display_exception()
        logging.error(f"INVALID PASSWORD ENTERED :{pwd}")
        logging.debug("INVALID PASSWORD EXCEPTION HANDLED")
    else:
        print("You have entered the valid password")
        logging.info(f"VALID PASSWORD ENTERED :{pwd}")


password=input("ENTER THE PASSWORD: ")
password_validator(password)



