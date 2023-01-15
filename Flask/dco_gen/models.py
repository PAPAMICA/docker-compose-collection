class EnvVar():
    items = []

    def __init__(self, name, hint, description, default) -> None:
        self.name        = name
        self.hint        = hint
        self.descritpion = description
        self.default     = default

class Volume():
    items = []

    def __init__(self, name, container) -> None:
        self.name      = name
        self.container = container

class Port():
    items = []

    def __init__(self, port_nb) -> None:
        self.port_number = port_nb

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
        self.app_ports           = []
        self.envvar              = []
        self.volumlist           = []