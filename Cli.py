from os import system

from Scene import scene
from Table_scene import table

class cli:
    
    CSV_FORMAT = 0
    JSON_FORMAT = 1

    LEFT = 0
    RIGHT = 1
    CENTER = 2
    
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
                

    def add_scene(self, name: str, scene_options: list, scene_body: str, links: list, align_options: int = None,
                  align_body: int = None) -> None:
        """
        Create a new scene and add it in the scenes dict with the following params:

        :param name (string): The name of the scene
        :param scene_options (list): A list containing all the scene options
        :param scene_body (string): A string containing the body which will be printed on the screen
        :param links (list): A list contaning the links to other scenes and tables. The user will be
                             redirected to the scene when it types the index of the link on the list
        """

        self.scene_name_dict[name] = scene(name, scene_options, scene_body, links, align_options=align_options,
                                           align_body=align_body)
        
    
    def add_table_scene(self, name: str, table_options: list, table_info: dict or "DataFrame", links: list, 
                  changeble_table: bool = True, change_callback: 'function' = None, save_file: str = None,
                  read_file: tuple = None) -> None:
        """
        Create a new table scene and add it in the scenes dict with the following params:

        :param name (string): A string containing the name of the table scene
        :param table_info (dict or panda's DataFrame): A dict which will be transformed into a pandas data frame, 
                                                       if it isn't already 
        :param links (list): A list contaning the links to other scenes and tables. The user will be
                             redirected to the scene when it types the index of the link on the list
        :param changeble_table (boolean): A optional param which tell if the table can be changed or 
                                          not, if changeble_table param is true, it will add 'Change table' 
                                          in the option list and a reference of the change_data function 
                                          to the link list, default = True
        :param change_callback (function): A optional param which receives a function that will be called passing 
                                           all the updated data from the table. Usefull if you need 
                                           to work with the updated data, default = None.
        :param save_file (tuple): A optional param which receives a tuple containing the first index as a path
                                  with the file name, and the second index as the saving format. It accepts only
                                  .csv and .json files by now.
        :param read_file (tuple): A optional param which reives a tuple containing the first index as a path
                                  with the file name you want to extract the data from to make a table scene,
                                  and the second index as the format of the file. It accepts only .csv and .json,
                                  files by now, default = None

        *** USE CLI CONSTANTS (*_FORMAT) TO DEFINE THE FORMAT OF THE SAVE_FILE AND READ_FILE PARAMS ***
        """

        self.scene_name_dict[name] = table(name, table_options, table_info, links, 
                                        changeble_table=changeble_table, change_callback=change_callback,
                                        save_file=save_file, read_file=read_file)


if __name__ == "__main__":
    cli_obj = cli()

    table_dict = {
        "Coluna1": ["Valor 1", "Valor 2", "Valor 3"],
        "Coluna2": ["Valor 1", "Valor 2", "Valor 3"]
    }

<<<<<<< HEAD
    cli_obj.add_scene("intro", ["See table"], "Use one to see the table", ["table"], align_options=cli.RIGHT)
    cli_obj.add_table("table", ["Back to intro"], table_dict, ["intro"], save_file=("teste.json", cli.JSON_FORMAT),
=======
    cli_obj.add_scene("intro", ["See table"], "Use one to see the table", ["table"])
    cli_obj.add_table_scene("table", ["Back to intro"], table_dict, ["intro"], save_file=("teste.json", cli.JSON_FORMAT),
>>>>>>> f0969b3f1edbc855e22d9630b5becb460613b457
                       read_file=("teste.json", cli.JSON_FORMAT))

    cli_obj.set_first_scene_name("intro")

    cli_obj.render_forever()

