from Text_utilities.text_util import *

class scene:

    options_string = ""
    body_string = ""

    def __init__(self, name: str, scene_options: list, scene_body: str, links: list, 
                 centralize_options: bool = False, centralize_body: bool = False, char_per_line: int = 120):
        """
        Initiates the scene object with de following parameters:
        
        :param name (string): The name of the scene.
        :param scene_options (list): A list containing all the scene options.
        :param scene_body (string): A string containing the body which will be printed on the screen
        :param links (list): A list contaning the links to other scenes and tables. The user will be
                             redirected to the scene when it types the index of the link on the list.
        :param centralize_options (bool): If it is True it will centralize the scene options on the 
                                          screen, default = False.
        :param centralize_body (bool): If it is True it will centralize the scene body on the screen, 
                                       default = False.
        :param char_per_line (int): The number of character printed per line, default = 120.
        """
        self.name = name
        self.scene_options = scene_options
        self.scene_body = scene_body
        self.links = links
        self.centralize_options = centralize_options
        self.centralize_body = centralize_body
        self.char_per_line = char_per_line

        self.make_options_string()
        self.make_body_string()

    def make_options_string(self) -> None:
        """
        It formats the scene options.
        """
        for i in range(0, len(self.scene_options)):
            self.options_string += f"{i + 1} - {self.scene_options[i]}"

        if self.centralize_options:
            self.options_string = self.options_string.center(120)

    def make_body_string(self):
        """
        It formats the scene body.
        """
        body_list = divide_string(self.scene_body, self.char_per_line)

        if self.centralize_body:
            centralize_list(body_list)

        self.body_string = "\n".join(body_list)

    def render(self):
        """
        Call render_title function and show the scene body on the screen 
        """

        print(self.options_string)
        print('\n', end="\n")
        print(self.body_string)


    def get_links(self) -> list:
        return self.links
    
    def get_name(self) -> str:
        return self.name