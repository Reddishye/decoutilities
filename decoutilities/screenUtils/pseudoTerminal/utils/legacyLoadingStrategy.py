from .autoComplete import autoComplete
class legacyLoadingStrategy():
    def __init__(self):
        self.commands = {}
        self.autoComplete = autoComplete([], "Command: ")

    def addCommand(self, commandName, command):
        self.commands[commandName] = command
        self.autoComplete.updateCommandList([key for key in self.commands.keys()])

    def autoCompleteCommand(self, partialCommand):
        return self.autoComplete.completeFromPartial(partialCommand)

    def addToComplete(self, command):
        commandNames = [key for key in self.commands.keys()]
        if command not in commandNames:
            commandNames.append(command)

        self.autoComplete.updateCommandList(commandNames)

    def runCommand(self, command):
        if command in self.commands:
            return self.commands[command]
        else:
            return None