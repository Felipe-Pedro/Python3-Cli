from os import system

class scene:

    def __init__(self, name: str, scene_options: list, scene_body: str, links: list):
        """
        Initiates the scene object with de following parameters:
        
        :param name: (string) The name of the scene
        :param scene_options: (list) A list containing all the scene options
        :param scene_body: (string) A string containing the body which will be printed on the screen
        :param links: (list) A list contaning the links to other scenes and tables. The user will be
                redirected to the scene when it types the index of the link on the list
        """
        self.name = name
        self.scene_options = scene_options
        self.scene_body = scene_body
        self.links = links


    def render_title(self):
        """
        Show all the options names on the screen

        Ex: 1 - Option 2 - Option 3 - Option
        """

        i = 1

        for title in self.scene_options:
            print(f'{i} - {title}', end="\t")
            i += 1


    def render(self):
        """
        Call render_title function and show the scene body on the screen 
        """

        system('cls')

        self.render_title()

        print('\n', end="\n")
        print(self.scene_body)


    def get_links(self) -> list:
        return self.links
    
    def get_name(self) -> str:
        return self.name