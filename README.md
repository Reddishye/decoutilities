# decoutilities

A simple python package that allows using decorators for multiple things like easily setting up singleton or config files.

## Installation

You can install `decoutilities` using pip:

```bash
pip install decoutilities
```

## Usage

### @singleton

The `@singleton` decorator transforms any class into a singleton, ensuring only one instance of the class is created.

```python
from decoutilities import singleton

@singleton
class MyClass:
    pass

instance1 = MyClass()
instance2 = MyClass()

print(instance1 is instance2)  # Output: True
```

### @private

The `@private` decorator transforms any class into a private class, making it inaccessible from outside the module.

```python
from decoutilities import private

@private
class MyPrivateClass:
    pass

# Trying to access MyPrivateClass from outside the module will raise an error
```

### @static

The `@static` decorator transforms any class into a static class, raising an exception if an attempt is made to instantiate it. This feature is experimental and might fail, please report any errors.

```python
from decoutilities import static

@static
class MyStaticClass:
    pass

# Trying to instantiate MyStaticClass will raise an exception
instance = MyStaticClass()  # Raises: Exception: This class is static and cannot be instantiated!
```

### @threaded

The `@threaded` decorator transforms any class into a threaded class, returning a thread object when the class is instantiated. This feature is experimental and might fail, please report any errors.

```python
from decoutilities import threaded

@threaded
class MyThreadedClass:
    def __init__(self, value):
        self.value = value

    def run(self):
        print(f"Running with value {self.value}")

# Instantiate MyThreadedClass, which returns a thread object
thread = MyThreadedClass(5)

# Start the thread
thread.start()

# Outputs: Running with value 5
```

### @trycatch

The `@trycatch` decorator wraps a function in a try-catch block, allowing it to handle exceptions without needing to write explicit try-catch blocks in your code.

```python
from decoutilities import trycatch

@trycatch
def risky_function():
    # Some risky operation that might raise an exception
    return 1 / 0

risky_function()  # Prints: An error occurred: division by zero
```

### @loop(condition_func)

The `@loop` decorator is an experimental feature that allows a function to loop until a certain condition is met. The condition is a function that returns a boolean value.

```python
from decoutilities import loop

var1 = 0

@loop(lambda: var1 > 10)
def increment_var1():
    global var1
    var1 += 1
    print(var1)

increment_var1()  # This will keep running until 'var1' is greater than 10
```

### Config System

`decoutilities` provides a complex config system that allows you to easily manage configuration settings using decorators.

#### configContainer

The `configContainer` class is responsible for loading and saving configuration data from/to JSON or YAML files.

```python
from decoutilities.config import configContainer

# Create a configContainer instance
config_container = configContainer(path="config", filename="settings", type="json")

# Register values
config_container.registerValues({
    "api_key": "your_api_key",
    "timeout": 5
})

# Get a value
api_key = config_container.getValue("api_key")

# Set a value
config_container.setValue("timeout", 10)
```

#### config

The `config` class works in conjunction with `configContainer` to provide a decorator-based approach for registering settings.

```python
from decoutilities.config import config, configContainer

# Create a configContainer instance
config_container = configContainer(path="config", filename="settings", type="json")

# Create a config instance
config_instance = config(config_container)

# Register a setting using the @setting decorator
@config_instance.setting()
def api_key():
    return "your_api_key"

# Access the registered setting
api_key = config_container.getValue("api_key")
```

### Inject System

`decoutilities` comes with an easy to use injector class (EXPERIMENTAL) that allows to easily share information.

```python
from decoutilities.inject import injector

# Create an instance of the injector
injector_instance = injector()

# Register a function with the injector
@injector_instance.register('greet')
def greet(name):
    return f"Hello, {name}!"

# Use the injector to get the function
greet_func = injector_instance.inject('greet')

# Call the function
print(greet_func('World'))  # Outputs: Hello, World!
```

## Experimental Features

All features marked as in `BETA` or being `EXPERIMENTAL` are untested, what means they were only tested below specific condititons and not with all case of uses.

Please report any issues or contribute by making a PR (look for [CONTRIBUTING](CONTRIBUTING) section for details).

### REMEMBER:

This whole project is still in beta, and versions below `0.1.5` might not work. Also syntax changes could be made in a future, so consider creating a `requeriments.txt`file for your project specifying the version you wonder to use.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the [GitHub repository](https://github.com/Reddishye/decoutilities).

### Pull Requests

In case you wonder to make a pull request, please include in the title any of these:
- FEATURE: For new features, include a explanation mentioning why it should be inside `decoutilities`.
- BUGFIX: For general bugfixes.
- SECURITY: For fixes related with security issues.
- QoL: For QoL improvements

## Author

- [Hugo Torres](https://github.com/Reddishye)