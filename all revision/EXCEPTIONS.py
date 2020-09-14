import logging
logging.basicConfig(filename="mylog2.log",level=logging.DEBUG)
def tryexcept():
    try:
        logging.info("division ")
        n = 10 / 0

    except ValueError:
        print("valueeror")
    except ZeroDivisionError:
        print("handled inside function")
        logging.error("dicision by zero")

    else:
        print("no valueeroor")
    finally:
        print("i will execute")
    print("handled")

try:
    tryexcept()
except ZeroDivisionError:
    print("handled after function")
finally:
    print("finally handled ")
print("thnaks trycatch")

