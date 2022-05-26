from glob import glob
import os
import shutil
import pathlib


class Filesystem:
    @staticmethod
    def GetAbsolutePath(path: str) -> str:
        return os.path.abspath(path)

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
    def CreateFolder(path: str) -> None:
        os.makedirs(Filesystem.GetAbsolutePath(path), exist_ok=True)

    @staticmethod
    def IsFolderEmpty(path: str) -> None:
        return (
            Filesystem.DoesPathExist(path)
            and Filesystem.IsFolder(path)
            and os.scandir(Filesystem.GetAbsolutePath(path))
        )

    @staticmethod
    def GetAllFilepathsRecursively(root: str) -> list:
        return [
            os.path.abspath(f).replace("\\", "/")
            for f in glob(f"{root}/**", recursive=True)
            if os.path.isfile(f)
        ]

    @staticmethod
    def GetFilename(path: str) -> str:
        return pathlib.Path(path).name

    @staticmethod
    def GetFilenames(paths: list) -> list:
        return [Filesystem.GetFilename(path) for path in paths]

    @staticmethod
    def GetExtension(path: str) -> str:
        return pathlib.Path(path).suffix

    @staticmethod
    def GetExtensions(paths: list) -> list:
        return [Filesystem.GetExtension(path) for path in paths]

    @staticmethod
    def SearchForFile(filename: str, location: str):
        paths = Filesystem.GetAllFilepathsRecursively(location)
        for path in paths:
            if Filesystem.GetFilename(path) == filename:
                return path

        return None

    @staticmethod
    def MoveFile(source: str, destination: str):
        if os.path.isfile(source):
            os.makedirs(os.path.abspath(destination), exist_ok=True)
            shutil.move(source, destination)

    @staticmethod
    def CopyFile(source: str, destination: str):
        if os.path.isfile(source):
            os.makedirs(os.path.abspath(destination), exist_ok=True)
            shutil.copy2(source, destination)
