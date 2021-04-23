import datetime


class Log:

    __log_file = None
    __log_name = ""

    def __init__(self, log="/etc/hobby-hub/log.txt"):
        try:
            self.__log_name = log
            self.__log_file = open(log, "a+")
        except:
            raise Exception('invalid log file')

    def write(self, message):
        ct = datetime.datetime.now()
        date = ct.strftime("%x").split("/")
        time = date[0] + "-" + date[1] + " " + ct.strftime("%X")
        self.__log_file.write(time + " " + message + "\n")
        self.__log_file.flush()

    def clear(self):
        self.__log_file.close()
        open(self.__log_name, 'w').close()
        self.__log_file = open(self.__log_name, "a+")



