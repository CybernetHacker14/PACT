from jinja2 import Environment, Template, FileSystemLoader, select_autoescape


class JinjaTemplateLoader:
    def __init__(self, templateLocation, templateFilename):
        self.templateLocation = templateLocation
        self.templateFilename = templateFilename
        self.__CreateEnvironmentAndLoadTemplate()

    def __CreateEnvironmentAndLoadTemplate(self):
        self.env = Environment(
            loader=FileSystemLoader(self.templateLocation),
            autoescape=select_autoescape(default_for_string=True, default=True),
        )

        self.template = self.env.get_template(self.templateFilename)
