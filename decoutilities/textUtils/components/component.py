class Component():
    def  __init__(self, text = None):
        if text is None:
            self.data=[{"text": "", "color": "white",  "decorations": ["bold"]}]
    # When printing component, print data
    def __str__(self):
        return self.data
    
    # Create a new component with the given text
    # Text example: "<red>He<bold>llo <green>Wor</bold>ld</green></red>"
    def fromText(self, text):
        import re

        # Allowed tags
        self.allowed_tags = [
            "bold",
            "underline",
            "italic",
            "b",
            "u",
            "i",
            "red",
            "green",
            "yellow",
            "blue",
            "purple",
            "cyan",
            "white",
            "dark_red",
            "dark_green",
            "gold",
            "gray",
            "dark_gray",
            "black",
            "reset"
        ]

        # Split the text into segments
        segments = re.split(r"(<[^>]+>)", text)
        # Initialize an empty list to store the data
        data = []
        # Loop through the segments and determine the opened tags for each one
        current_tags = []
        for segment in segments:
            # Use RE to classify if the segment is a tag or not
            if re.match(r"<[^>]+>", segment):
                # If the segment is a tag, check if it is an opening or closing tag
                tag = segment[1:-1]
                if tag[0] == "/":
                    if tag[1:] in current_tags:
                        # If the tag is a closing tag, remove it from the current_tags list
                        current_tags.remove(tag[1:])
                else:
                    if tag in self.allowed_tags:
                        # If it is an opening tag, add it to the current_tags list
                        current_tags.append(tag)
                    else:
                        # Check for HEX color
                        if re.match(r"#[0-9a-fA-F]{6}", tag):
                            current_tags.append(tag)
            else:
                # If the segment is not a tag, add it to the data with the current tags value
                data_segment = {"text": segment, "tags": []}
                # Loop through the current tags and add the aliases to the data_segment
                for tag in current_tags:
                    # check if tag is a HEX color
                    if re.match(r"#[0-9a-fA-F]{6}", tag):
                        # Although if and else are the same, they are kept for future changes

                        data_segment["tags"].append(tag)
                    else:
                        data_segment["tags"].append(tag)
                data.append(data_segment)
        self.data = data
        return self