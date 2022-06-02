import argparse
from enum import Enum


class ArgumentType(Enum):
    VARIABLE = 1
    LIST = 2
    CONST = 3
    FLAG_TRUE = 4
    FLAG_FALSE = 5


class ArgumentParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            formatter_class=argparse.ArgumentDefaultsHelpFormatter
        )

    def AddArgumentParameter(
        self,
        argument: str,
        argumentType: ArgumentType.VARIABLE,
        argumentValueType: str,
        description: str = None,
        constValue=None,
    ):
        if argumentType == ArgumentType.VARIABLE:
            self.parser.add_argument(
                argument, action="store", type=argumentType, help=description
            )
        elif argumentType == ArgumentType.LIST:
            self.parser.add_argument(
                argument,
                action="extend",
                nargs="+",
                type=argumentValueType,
                help=description,
            )
        elif argumentType == ArgumentType.CONST:
            self.parser.add_argument(
                argument,
                action="store_const",
                type=argumentValueType,
                const=constValue,
                help=description,
            )
        elif argumentType == ArgumentType.FLAG_TRUE:
            self.parser.add_argument(argument, action="store_true", help=description)
        elif argumentType == ArgumentType.FLAG_FALSE:
            self.parser.add_argument(argument, action="store_false", help=description)

    def ProcessArguments(self, testArguments=None):
        if not testArguments is None:
            self.args = self.parser.parse_args(testArguments)
        else:
            self.args = self.parser.parse_args()
        self.config = vars(self.args)
        return self.config
