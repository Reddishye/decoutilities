class configContainer:
    def __init__(self, path, filename, type):
        self.path = path
        self.filename = filename
        self.type = type
        self.data = {}
        self.load()
    def load(self):
        if self.type == "json":
            self.loadJSON()
        elif self.type == "yaml":
            self.loadYAML()
        else:
            exception = f"Type '{self.type}' is not supported, use 'json' or 'yaml' instead."
            raise TypeError(exception)
    def loadJSON(self):
        import json
        import os

        # Crear el directorio si no existe
        os.makedirs(self.path, exist_ok=True)

        # Crear el archivo si no existe
        if not os.path.isfile(f"{self.path}/{self.filename}.json"):
            with open(f"{self.path}/{self.filename}.json", "w") as file:
                json.dump({}, file)

        # Cargar el archivo
        with open(f"{self.path}/{self.filename}.json", "r") as file:
            try:
                self.data = json.load(file)
            except json.decoder.JSONDecodeError:
                self.data = {}

    def loadYAML(self):
        import yaml
        import os
        # create folder and files if they don't exist
        if not os.path.exists(self.path):
            os.makedirs(self.path)
        if not os.path.exists(f"{self.path}/{self.filename}.yaml"):
            with open(f"{self.path}/{self.filename}.yaml", "w") as file:
                file.write("{}")
        with open(f"{self.path}/{self.filename}.yaml", "r") as file:
            self.data = yaml.safe_load(file)
        # Store the type of each value
        for key, value in self.data.items():
            self.data[key] = {'type': str(type(value)), 'value': value}

    # Registers the config and generates the keys if they don't exist.
    def registerValues(self, config):
        for key, value in config.items():
            self.__register(key, value)


    def __register(self, key, value):
        if key not in self.data:
            self.data[key] = value
            self.__save()

    # Saves the data into the file.
    def __save(self):
        if self.type == "json":
            self.__saveJSON()
        elif self.type == "yaml":
            self.__saveYAML()
        else:
            exception = f"Type '{self.type}' is not supported, use 'json' or 'yaml' instead."
            raise TypeError(exception)
        
    def __saveJSON(self):
        import json
        with open(f"{self.path}/{self.filename}.json", "w") as file:
            # Only save the value of each item if it is a dictionary
            json.dump({k: v['value'] if isinstance(v, dict) else v for k, v in self.data.items()}, file, indent=4)

    def _convert_data(self, data):
        if isinstance(data, dict):
            return {k: self._convert_data(v) for k, v in data.items()}
        elif isinstance(data, list):
            return [self._convert_data(v) for v in data]
        elif isinstance(data, (str, int, float, bool, type(None))):
            return data
        else:
            return str(data)  # or use any other method to convert `data` to a serializable format
    def __saveYAML(self):
        import yaml
        with open(f"{self.path}/{self.filename}.yaml", "w") as file:
            # Only save the value of each item
            yaml.dump({k: v['value'] for k, v in self.data.items()}, file)
    # Get data from the config file.
    def get(self, key):
        return self.data[key]
    
    # Get the value of the key from the config file.
    def getValue(self, key):
        try:
            value = self.data[key]
            if isinstance(value, dict):
                return value['value']
            else:
                return value
        except KeyError:
            return None
    
    # Set the value of the key from the config file.
    def setValue(self, key, value):
        self.data[key] = value
        self.__save()

    # Change the type of the value of the key from the config file.
    def changeType(self, key, type):
        self.data[key] = type(self.data[key])
        self.__save()

    # Reload all the keys from the config file. (Alias for load())
    def reload(self):
        self.load()