COMMAND = "@readfile"

def run(command, blocks, preprocessed):
    if command.parms:
        with open(command.parms[0], "r") as file:
            return file.read()