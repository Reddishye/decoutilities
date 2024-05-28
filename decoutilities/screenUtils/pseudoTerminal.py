import msvcrt
import threading
from decoutilities.textUtils import format as color

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
        def run():
            while True:
                command = self.__get_input()
                self.history.append(command)
                self.historyIndex = -1
                if command in self.commands:
                    self.commands[command]()
                elif command == "exit":
                    break
                else:
                    print(color('{red}Invalid command'))
        threading.Thread(target=run).start()

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

    def __get_input(self):
        command = ''
        print(color('{blue}' + self.prefix), end='', flush=True)
        while True:
            key = msvcrt.getch().decode('utf-8', errors='ignore')
            if key == '\r':  # Enter key pressed
                print()
                break
            elif key == '\b':  # Backspace key pressed
                command = command[:-1]
                print('\r' + color('{blue}' + self.prefix) + ' ' * (len(self.prefix) + len(command)) + '\r' + color('{blue}' + self.prefix + command), end='', flush=True)
                continue
            elif key == '\t':  # Tab key pressed
                matches = [cmd for cmd in self.commands if cmd.startswith(command)]
                if matches:
                    command = matches[0]
                    print('\r' + color('{blue}' + self.prefix) + ' ' * (len(self.prefix) + len(command)) + '\r' + color('{blue}' + self.prefix + command), end='', flush=True)
                continue
            command += key
            print(key, end='', flush=True)
            matches = [cmd for cmd in self.commands if cmd.startswith(command)]
            if matches:
                first_word = command.split(' ')[0]
                if first_word in self.commands:
                    print('\r' + color('{blue}' + self.prefix) + color('{green}' + first_word) + color('{white}' + command[len(first_word):]) + color('{dark_gray}' + matches[0][len(command):]), end='', flush=True)
                else:
                    print('\r' + color('{blue}' + self.prefix) + color('{red}' + first_word) + color('{white}' + command[len(first_word):]) + color('{dark_gray}' + matches[0][len(command):]), end='', flush=True)
                if (command not in self.commands):
                    print("\033[%dD" % len(matches[0][len(command):]), end='', flush=True)  # move cursor back
        return command

terminal = pseudoTerminal()
terminal.addCommand("test", lambda: print("Test command"))
terminal.display()