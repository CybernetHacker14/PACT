from ..CommandLineArguments.ArgumentParser import (
    ArgumentParser as Parser,
    ArgumentType as Type,
)


argumentFormat = {
    "--option": (Type.FLAG_TRUE, bool, "Optional Test Argument declaration"),
    "argument": (Type.VARIABLE, str, "Compulsory Test Argument declaration"),
}


class ArgumentProcessor:
    def __init__(self):
        self.parser = Parser()
        for argument, data in argumentFormat.items():
            self.parser.AddArgumentParameter(argument, data[0], data[1], data[2])

    def GetArgVars(self, testArguments=None):
        if testArguments is None:
            return self.parser.ProcessArguments()
        else:
            return self.parser.ProcessArguments(testArguments)
