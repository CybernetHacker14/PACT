from glob import glob
import os
import shutil
import pathlib


class Filesystem:
    @staticmethod
    def GetAbsolutePath(path: str) -> str:
        return os.path.abspath(path).replace("\\", "/")

    @staticmethod
    def DoesPathExist(path: str) -> bool:
        return os.path.exists(Filesystem.GetAbsolutePath(path))

    @staticmethod
    def IsFile(path: str) -> bool:
        return os.path.isfile(Filesystem.GetAbsolutePath(path))

    @staticmethod
    def IsFolder(path: str) -> bool:
        return os.path.isdir(Filesystem.GetAbsolutePath(path))

    @staticmethod
    def GetDirectoryFromPath(path: str) -> str:
        return os.path.dirname(Filesystem.GetAbsolutePath(path))

    @staticmethod
    def CreateFolder(path: str) -> None:
        os.makedirs(Filesystem.GetDirectoryFromPath(path), exist_ok=True)

    @staticmethod
    def IsFolderEmpty(path: str) -> None:
        return (
            Filesystem.DoesPathExist(path)
            and Filesystem.IsFolder(path)
            and os.scandir(Filesystem.GetAbsolutePath(path))
        )

    @staticmethod
    def HasSubfolders(path: str) -> bool:
        return len(Filesystem.GetAllSubfolders(path)) != 0

    @staticmethod
    def GetImmediateSubfolders(path: str) -> list:
        return [
            os.path.abspath(f).replace("\\", "/")
            for f in glob(f"{path}/**", recursive=False)
            if Filesystem.IsFolder(f)
        ]

    @staticmethod
    def GetAllSubfolders(path: str) -> list:
        return [
            os.path.abspath(f).replace("\\", "/")
            for f in glob(f"{path}/**", recursive=True)
            if Filesystem.IsFolder(f)
        ]

    @staticmethod
    def GetImmediateSubfilepaths(path: str) -> list:
        return [
            os.path.abspath(f).replace("\\", "/")
            for f in glob(f"{path}/**", recursive=False)
            if Filesystem.IsFile(f)
        ]

    @staticmethod
    def GetAllSubfilepaths(path: str) -> list:
        return [
            os.path.abspath(f).replace("\\", "/")
            for f in glob(f"{path}/**", recursive=True)
            if Filesystem.IsFile(f)
        ]

    @staticmethod
    def HasExtension(path: str) -> bool:
        if pathlib.Path(path).suffix:
            return True
        return False

    @staticmethod
    def GetFilenameWithoutExtension(path: str) -> str:
        return pathlib.Path(path).stem

    @staticmethod
    def GetFilenameWithExtension(path: str) -> str:
        return pathlib.Path(path).name

    @staticmethod
    def GetFilenameExtension(path: str) -> str:
        return pathlib.Path(path).suffix

    @staticmethod
    def GetFilenamesWithoutExtension(paths: list) -> list:
        return [Filesystem.GetFilenameWithoutExtension(path) for path in paths]

    @staticmethod
    def GetFilenamesWithExtension(paths: list) -> list:
        return [Filesystem.GetFilenameWithExtension(path) for path in paths]

    @staticmethod
    def GetFilenameExtensions(paths: list) -> list:
        return [Filesystem.GetFilenameExtension(path) for path in paths]

    @staticmethod
    def SearchForFile(filename: str, location: str):
        paths = Filesystem.GetAllFilepathsRecursively(location)
        for path in paths:
            if Filesystem.GetFilename(path) == filename:
                return path

        return None

    @staticmethod  # Windows specific
    def OpenAtPath(path: str):
        if Filesystem.DoesPathExist(path):
            os.startfile(Filesystem.GetAbsolutePath(path))

    @staticmethod
    def DeleteAtPath(path: str):
        if Filesystem.DoesPathExist(path):
            if Filesystem.IsFile(path):
                os.remove(Filesystem.GetAbsolutePath(path))
            elif Filesystem.IsFolder(path):
                shutil.rmtree(Filesystem.GetAbsolutePath(path))

    @staticmethod
    def MoveAtPath(source: str, destination: str):
        if Filesystem.DoesPathExist(source) and Filesystem.IsFile(source):
            os.makedirs(Filesystem.GetAbsolutePath(destination), exist_ok=True)
            shutil.move(source, destination)

    @staticmethod
    def CopyAtPath(source: str, destination: str):
        if Filesystem.DoesPathExist(source) and Filesystem.IsFile(source):
            os.makedirs(Filesystem.GetAbsolutePath(destination), exist_ok=True)
            shutil.copy2(source, destination)

    @staticmethod
    def WriteToFile(path: str, data: str):
        Filesystem.CreateFolder(path)

        with open(path, "w") as outfile:
            outfile.write(data)

    @staticmethod
    def ReadFromFile(path: str, ignoreNewLine: bool = False) -> str:
        with open(path) as data:
            if ignoreNewLine:
                return data.read().replace("\n", "")
            else:
                return data.read()
