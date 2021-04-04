from os import system

from Scene import scene
from Table_scene import table_scene

class cli:
    
    CSV_FORMAT = 0
    JSON_FORMAT = 1

    RIGHT = 0
    CENTER = 1
    
    scene_name_dict = {}
    symbol = None
    current_scene = None

    def __init__(self, symbol: str = ">"):
        """
        It create the cli object

        :param symbol (string): It is the symbol which will be displayed on the beginning of the input line
                                default = >
        """
        self.symbol = symbol

    def set_first_scene_name(self, first_scene: str) -> None:
        """
        It will set the first scene which will be displayed (Call this function after set at least one scene)

        :param first_scene(string): It receives the name of the first scene you want to show
        """

        self.current_scene = self.scene_name_dict[first_scene]


    def is_link_to_scene_name_a_function(self, link_to_scene_name: str or "function") -> bool:
        """
        It returns True if the link_to_scene_name is a function (not a string)

        :param link_to_scene_name(string or function): It receives a string or a function
        """

        if type(link_to_scene_name) is not str:
            return True

    
    def is_user_input_a_integer(self, user_input: str or int) -> bool:
        """
        It returns True if the user_input's type is int

        :param user_input(string or int): It receives the user input which can be a string or a integer
        """

        if type(user_input) is int:
            return True


    def is_user_input_in_range_of_scene_link(self, user_input: int) -> bool:
        """
        It returns True if the user_input is on the range of the scene link's list

        :param user_input (int): It receiver the user_input
        """

        if  user_input >= 0 and user_input <= len(self.current_scene.get_links()):
            return True


    def render_forever(self) -> None:
        """
        Display the first scene and start the eternal loop. If r (the user input) is numeric and
        the number is equal one of the index in current scene's link list it will redirect the user
        to the scene contained in the scene_name_dict
        """

        system('cls')
        
        self.current_scene.render()

        while True:
            user_input = input(f"\n{self.symbol} ")
            user_input = int(user_input) - 1 if user_input.isdigit() else user_input

            system('cls')

            if self.is_user_input_a_integer(user_input) and self.is_user_input_in_range_of_scene_link(user_input):

                links = self.current_scene.get_links()
                link_to_scene_name = links[user_input]

                if self.is_link_to_scene_name_a_function(link_to_scene_name):
                    link_to_scene_name()
                    link_to_scene_name = self.current_scene.get_name()
                    system('cls')

                self.current_scene = self.scene_name_dict[link_to_scene_name]
                
                self.current_scene.render()
            else:

                
                self.current_scene.render()
                print(f'\n#That\'s is not a valid option#')
                

    def add_scene(self, name: str, scene: scene) -> None:
        """
        Add a new scene in the scenes dict

        :param name (string): The name of the scene
        :param scene (scene): A scene of any type which will be add in the scene dict
        """

        self.scene_name_dict[name] = scene

if __name__ == "__main__":
    cli_obj = cli()

    table_dict = {
        "Coluna1": ["Valor 1", "Valor 2", "Valor 3"],
        "Coluna2": ["Valor 1", "Valor 2", "Valor 3"]
    }

    table_info = table_scene("table_info", ["Back to intro"], table_dict, ["intro"])
    intro_scene = scene("intro", ["See table"], "Send 1 to see the table", ["table_info"], align_options=cli.CENTER)

    cli_obj.add_scene("intro", intro_scene)
    cli_obj.add_scene("table_info", table_info)

    cli_obj.set_first_scene_name("intro")

    cli_obj.render_forever()

