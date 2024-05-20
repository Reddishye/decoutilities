from ..textUtils import textUtils

class Logger:
    def __init__(self, prefix = None, debug=False, log = None, format = "{event} {white}| {message}"):
        self.prefix = prefix
        self.log = log
        self.format = textUtils.format
        self.debug = debug

    def  __toLogFile(self, message):
        if self.log is not None:
            with open(self.log, "a") as file:
                file.write(message + "\n")

    def __log(self, event, message):
        if self.prefix is not None:
            event = self.prefix + " " + event
        message = self.format(message)
        message = self.format(self.format, event = event, message = message)
        print(message)
        self.__toLogFile(message)
    
    def info(self, message):
        self.__log("INFO", message)

    def warning(self, message):
        self.__log("WARNING", message)

    def error(self, message):
        self.__log("ERROR", message)

    def success(self, message):
        self.__log("SUCCESS", message)

    def debug(self, message):
        if self.debug:
            self.__log("DEBUG", message)

    def announce(self, message):
        self.__log("ANNOUNCE", message)