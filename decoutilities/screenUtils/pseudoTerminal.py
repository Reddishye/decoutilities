class pseudoTerminal():
    def __init__(self, prefix='>>> '):
        self.prefix = prefix
        self.commands = {}
        self.history = []
        self.historyIndex = -1
        self.__loadDefaultCommands()

    def addCommand(self, command, func):
        self.commands[command] = func

    def display(self):
        while True:
            command = input(self.prefix)
            self.history.append(command)
            self.historyIndex = -1
            if command in self.commands:
                self.commands[command]()
            elif command == "exit":
                break
    
    def __loadDefaultCommands(self):
        self.addCommand("exit", exit)
        self.addCommand("help", self.__help)
        self.addCommand("history", self.__history)
    
    def __help(self):
        print("Commands:")
        for command in self.commands:
            print(command)
        
    def __history(self):
        for command in self.history:
            print(command)

terminal = pseudoTerminal()
terminal.addCommand("test", lambda: print("Test command"))
terminal.display()