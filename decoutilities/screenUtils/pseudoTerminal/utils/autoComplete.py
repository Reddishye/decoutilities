import os

class autoComplete():
    def __init__(self, options, prompt=""):
        self.options = options
        self.prompt = prompt
        self.index = 0
        self.length = len(self.options)
        self.current = self.options[self.index] if self.options else None

    def updateCommandList(self, list):
        self.options = list
        self.length = len(self.options)
        self.index = 0
        self.current = self.options[self.index] if self.options else None

    def next(self):
        if not self.options:
            return
        self.index = (self.index + 1) % self.length
        self.current = self.options[self.index]

    def prev(self):
        if not self.options:
            return
        self.index = (self.index - 1) % self.length
        self.current = self.options[self.index]

    def complete(self):
        return self.current

    def complete_path(self, path):
        if not path:
            return path
        dir_path, partial_path = os.path.split(path)
        try:
            matches = [name for name in os.listdir(dir_path) if name.startswith(partial_path)]
            return os.path.join(dir_path, matches[0]) if matches else path
        except FileNotFoundError:
            return path

    def completeFromPartial(self, partial):
        if not partial:
            return partial
        matches = [option for option in self.options if option.startswith(partial)]
        return matches[0] if matches else partial