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
        self.__log_file.write(message + "\n")
        self.__log_file.flush()

    def clear(self):
        self.__log_file.close()
        open(self.__log_name, 'w').close()
        self.__log_file = open(self.__log_name, "a+")


