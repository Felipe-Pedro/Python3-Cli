from Scene_utilities.scene_util import *

class scene:

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
        self.links = links
        self.centralize_options = centralize_options
        self.centralize_body = centralize_body

        self.scene_options = make_options_string(scene_options, centralize_options)
        self.scene_body = make_body_string(scene_body, char_per_line, centralize_body)
        
    def render(self):
        """
        Print all the scene information.
        """

        print(self.scene_options)
        print('\n')
        print(self.scene_body)


    def get_links(self) -> list:
        return self.links
    
    def get_name(self) -> str:
        return self.name