import sys


class PythonVersionValidation:
    @classmethod
    def __ValidatePython(cls, versionMajor=3, versionMinor=9):
        if sys.version is not None:
            major = sys.version_info.major
            minor = sys.version_info.minor
            micro = sys.version_info.micro
            print(f"Python version : {major}.{minor}.{micro}")

            if major < versionMajor or (major == versionMajor and minor < versionMinor):
                print(
                    f"Python version too low, expected version {versionMajor}.{versionMinor} or higher"
                )
                return False

            return True
