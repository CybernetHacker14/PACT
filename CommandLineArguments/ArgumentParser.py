import argparse
from enum import Enum


class ArgumentType(Enum):
    VARIABLE = 1
    LIST = 2
    FLAG = 3


class ArgumentParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            formatter_class=argparse.ArgumentDefaultsHelpFormatter
        )

    def AddArgumentParameter(
        self,
        argument: str,
        argumentType=ArgumentType.VARIABLE,
        argumentValueType=str,
        description: str = None,
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
        elif argumentType == ArgumentType.FLAG:
            self.parser.add_argument(argument, action="store_true", help=description)

    def ProcessArguments(self):
        self.args = self.parser.parse_args()
        self.config = vars(self.args)
        return self.config
