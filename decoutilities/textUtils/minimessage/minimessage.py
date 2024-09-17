import re

# Same as classic textutils formatting, however, this is more precise as on every style cange fully resets the styles and writes the new ones
# Inspired by the MiniMessage package from Kyori (This one does not include component system)
class MiniMessage():
    def __init__(self, debug=False):
        self.debug = debug
        self.text = []
        self.aliases = {
            "bold": "\033[1m",
            "underline": "\033[4m",
            "italic": "\033[3m",
            "b": "\033[1m",
            "u": "\033[4m",
            "i": "\033[3m",
            "red": "\033[91m",
            "green": "\033[92m",
            "yellow": "\033[93m",
            "blue": "\033[94m",
            "purple": "\033[95m",
            "cyan": "\033[96m",
            "white": "\033[97m",
            "dark_red": "\033[31m",
            "dark_green": "\033[32m",
            "gold": "\033[33m",
            "gray": "\033[37m",
            "dark_gray": "\033[90m",
            "black": "\033[30m",
            "reset": "\033[00m"
        }

    def __parseFromText(self, text):
        # A segment starts when a tag is opened or closeed, meaning a tag can be opened and closed in the same segment or be cloased with the opening/closing of another tag, i.e [["</last_tag>", "message"],  [...]]
        segments = re.split(r"(<[^>]+>)", text)
        # Loop through the segments and determine the opened tags for each one, finally fill data_segments with the data, i.e ["red,bold", "This is a test", "green", "of the", "bold", "MiniMessage", "green", "class", "red"]
        current_tags = []
        message = ""
        for segment in segments:
            # Use RE to clasify if the segment is a tag or not
            if re.match(r"<[^>]+>", segment):
                # If the segment is a tag, check if it is an opening or closing tag
                tag = segment[1:-1]
                if tag[0] == "/":
                    if tag[1:] in current_tags:
                        # If the tag is a closing tag, remove it from the current_tags list
                        current_tags.remove(tag[1:])
                else:
                    if tag in self.aliases:
                        # If it is an opening tag, add it to the current_tags list
                        current_tags.append(tag)
                    else:
                        # Check for HEX color
                        if re.match(r"#[0-9a-fA-F]{6}", tag):
                            current_tags.append(tag)
                        else:
                            # If the tag is not in the aliases, add it to the message
                            message += segment
            else:
                # If the segment is not a tag, add it to the message with the current tags value
                temp = ""
                # Loop through the current tags and add the aliases to the message
                for tag in current_tags:
                    # check if tag is a HEX color
                    if re.match(r"#[0-9a-fA-F]{6}", tag):
                        temp += "\033[38;2;" + tag[1:] + "m"
                    else:
                        temp += self.aliases[tag]
                message += temp + segment
                # Add the reset tag to the end of the message
                message += self.aliases["reset"]
        return message
    
    def __parseFromComponent(self, component):
        message = ""
        for data in component.data:
            temp = ""
            for tag in data["tags"]:
                # check if tag is a HEX color
                if re.match(r"#[0-9a-fA-F]{6}", tag):
                    temp += "\033[38;2;" + tag[1:] + "m"
                else:
                    temp += self.aliases[tag]
            message += temp + data["text"]
            # Add the reset tag to the end of the message
            message += self.aliases["reset"]
        return message
    
    def parse(self, arg):
        if isinstance(arg, str):
            return self.__parseFromText(arg)
        else:
            return self.__parseFromComponent(arg)