from os import get_terminal_size

class scene:

    options_string = ""

    def __init__(self, name: str, scene_options: list, scene_body: str, links: list, align_options: int = None,
                 align_body: int = None):
        """
        Initiates the scene object with de following parameters:
        
        :param name (string): The name of the scene.
        :param scene_options (list): A list containing all the scene options.
        :param scene_body (string): A string containing the body which will be printed on the screen
        :param links (list): A list contaning the links to other scenes and tables. The user will be
                             redirected to the scene when it types the index of the link on the list.
        :param align_options (int): Set the side which the options will be aligned.
        :param align_body (int): Set the side which the body will be aligned.
        """
        self.name = name
        self.scene_options = scene_options
        self.scene_body = scene_body
        self.links = links
        self.align_options = align_options
        self.align_body = align_body

        self.make_options_string()


    def make_options_string(self):
        """
        Make the options string with all the options
        """

        i = 1

        for option in self.scene_options:
            self.options_string += f"{i} {option}\t"
            i += 1

        if self.align_options == 0:
            self.options_string = self.options_string.rjust(120)

        if self.align_options == 1:
            self.options_string = self.options_string.center(120)

    def render(self):
        """
        Call render_title function and show the scene body on the screen 
        """

        print(self.options_string)
        print('\n', end="\n")
        print(self.scene_body)


    def get_links(self) -> list:
        return self.links
    
    def get_name(self) -> str:
        return self.name