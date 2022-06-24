import os
import webbrowser

from Templating.JinjaTemplateLoader import JinjaTemplateLoader as Loader
from Filesystem.Filesystem import Filesystem


class JinjaTemplateParser:
    def __init__(
        self,
        templateFolderLocation,
        templateFilename,
        resultFolderLocation,
        resultFilename,
    ):
        self.templateFolderLocation = templateFolderLocation
        self.templateFilename = templateFilename
        self.resultFolderLocation = resultFolderLocation
        self.resultFilename = resultFilename
        self.loader = Loader(self.templateFolderLocation, self.templateFilename)
        self.template = self.loader.template
        self.attributeData = {}

    def SetAttributeData(self, attribute: str, value):
        self.attributeData[attribute] = value

    def DeleteAttribute(self, attribute: str):
        self.attributeData.pop(attribute)

    def ClearAttributes(self):
        self.attributeData.clear()

    def WriteParsedData(self) -> str:
        path = Filesystem.GetAbsolutePath(self.resultFolderLocation)
        Filesystem.CreateFolder(path)
        path += f"/{self.resultFilename}"
        with open(path, "w") as f:
            f.write(self.template.render(self.attributeData))

        return path

    def OpenOutputFile(self, path: str):
        Filesystem.OpenAtPath(path)

    def OpenOutputFileInBrowser(self, path: str):
        webbrowser.open_new_tab(path)
