class help_scene:
    
    def __init__(self, name: str, help_options: list[str], links: list[str]):
        self.name = name
        self.links = links
        self.help_options = help_options

    def get_name(self) -> str:
        return self.name

    def get_links(self) -> list[str]:
        return self.links
        