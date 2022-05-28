import subprocess
import importlib.util as importlib_util

class PackageValidation:
    @staticmethod
    def ValidateList(packageList: dict) -> bool:
        for package in packageList:
            if not PackageValidation.Validate(package):
                return False

        return True

    @staticmethod
    def Validate(moduleName: str) -> bool:
        return not importlib_util.find_spec(moduleName) is None