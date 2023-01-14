class EnvVar():
    items = []

    def __init__(self) -> None:
        self.name        = ""
        self.hint        = ""
        self.descritpion = ""
        self.default     = ""

class Compose():
    def __init__(self,name,logo,image,url,description,maintainer,github) -> None:
        #obligatoires
        self.app_name            = name
        self.app_logo            = logo
        self.app_image           = image
        self.app_url             = url
        self.app_description     = description
        self.maintainer_name     = maintainer
        self.maintainer_github   = github
        #optionnels
        self.app_port            = ""
        self.envvar              = object()
        self.volumlist           = []