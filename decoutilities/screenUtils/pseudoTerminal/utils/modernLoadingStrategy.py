from .autoComplete import autoComplete

class modernLoadingStrategy():
    def __init__(self):
        self.commands = []
        self.commandList = []
        self.autoComplete = autoComplete([])

    def checkCommandComesFromCommandClass(self, command):
        from command import Command
        if not isinstance(command, Command):
            raise Exception("Command must be an instance of the Command class: " + str(command) + " is not an instance of the Command class.")

    def addCommand(self, command):
        self.commands.append(command)
        self.commandList.append(command.name)
        self.autoComplete.updateCommandList(self.commandList)

    def autoCompleteCommand(self, partialCommand):
        return self.autoComplete.completeFromPartial(partialCommand)
    
    def addToComplete(self, command):
        self.checkCommandComesFromCommandClass(command)
        commandNames = [command.name for command in self.commands]
        self.autoComplete.updateCommandList(commandNames)
    
    def runCommand(self, command):
        for c in self.commands:
            if c.name == command:
                return c.onExecute
        return None