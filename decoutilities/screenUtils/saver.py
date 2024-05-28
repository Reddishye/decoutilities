import os

class Saver:
    def __init__(self):
        self.data = None
    
    #copies all terminal printed stuff to data
    def getTerminalOutput(self):
        self.data = os.popen("history").read()
        
    #clears the terminal and prints the data
    def printTerminalOutput(self):
        os.system("clear")
        print(self.data)
    
test = Saver()
test.getTerminalOutput()
test.printTerminalOutput()