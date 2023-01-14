class EnvVar():
    items = []

    def __init__(self) -> None:
        self.name        = ""
        self.hint        = ""
        self.descritpion = ""
        self.default     = ""

class Compose():
    def __init__(self) -> None:
        self.app_name            = ""
        self.app_logo            = ""
        self.app_image           = ""
        self.app_port            = ""
        self.app_url             = ""
        self.app_description     = ""
        self.maintainer_name     = ""
        self.maintainer_github   = ""
        self.envvar              = object()
        self.volumlist           = []