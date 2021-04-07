from os import system

from scene import scene
from table_scene import table_scene

class cli:
    
    CSV_FORMAT = 0
    JSON_FORMAT = 1

    scene_name_dict = {}
    symbol = None
    current_scene = None

    def __init__(self, input_demarcation: str = ">", scene_option_error: str = "\n#That's is not a valid option#",
                 scene_name_error: str = "\n#That scene don't exist#"):
        """
        It create the cli object

        :param input_demarcation (string): It is the symbol which will be displayed on the beginning of the 
                                           input line, default = >.
        :param scene_option_error (string): The error massage which will appear when the user type a non 
                                            valid option, default = \n#That's is not a valid option#.
        :param scene_name_error (string): The error massage which will appear when the user tries to enter
                                          in a non existent scene, default = \n#That scene don't exist#.

        """
        self.input_demarcation = input_demarcation
        self.scene_option_error = scene_option_error
        self.scene_name_error = scene_name_error

    def set_first_scene_name(self, first_scene: str) -> None:
        """
        It will set the first scene which will be displayed (Call this function after set at least one scene).

        :param first_scene(string): It receives the name of the first scene you want to show.
        """

        self.current_scene = self.scene_name_dict[first_scene]


    def is_link_to_scene_name_a_function(self, link_to_scene_name: str or "function") -> bool:
        """
        It returns True if the link_to_scene_name is a function (not a string).

        :param link_to_scene_name(string or function): It receives a string or a function.
        """

        if type(link_to_scene_name) is not str:
            return True

    def render_forever(self) -> None:
        """
        Display the first scene and start the eternal loop. If r (the user input) is numeric and
        the number is equal one of the index in current scene's link list it will redirect the user
        to the scene contained in the scene_name_dict.
        """

        system('cls')
        
        self.current_scene.render()

        while True:
            user_input = input(f"\n{self.input_demarcation} ")

            system('cls')

            try:
                option = int(user_input) - 1

                links = self.current_scene.get_links()
                link_to_scene_name = links[option]

                if self.is_link_to_scene_name_a_function(link_to_scene_name):
                    link_to_scene_name()
                    link_to_scene_name = self.current_scene.get_name()
                    system('cls')

                self.current_scene = self.scene_name_dict[link_to_scene_name]
                    
                self.current_scene.render()
            
            except ValueError:
                self.current_scene.render()
                print(self.scene_option_error)

            except IndexError:
                self.current_scene.render()
                print(self.scene_name_error)
                

    def add_scene(self, scene: scene) -> None:
        """
        Add a new scene in the scenes dict.

        :param scene (scene): A scene of any type which will be add in the scene dict.
        """

        self.scene_name_dict[scene.name] = scene

if __name__ == "__main__":

    cli_obj = cli(input_demarcation="Write here:")

    table_dict = {
        "Coluna1": ["Valor 1", "Valor 2", "Valor 3"],
        "Coluna2": ["Valor 1", "Valor 2", "Valor 3"]
    }

    table_info = table_scene("table_info", ["Back to intro"], table_dict, ["intro"])
    intro_scene = scene("intro", ["See table", "No where"], "Send 1 to see the table", ["table_info"], char_per_line=30,
                        centralize_options=True, centralize_body=True)

    cli_obj.add_scene(intro_scene)
    cli_obj.add_scene(table_info)

    cli_obj.set_first_scene_name("intro")

    cli_obj.render_forever()

