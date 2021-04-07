import pandas as pd

from os import system

from Scene_utilities.scene_util import make_options_string

class table_scene:

    

    def __init__(self, name: str, table_options: list, table_info: dict or "DataFrame", links: list,
                changeble_table: bool = True, change_callback: 'function' = None, save_file: tuple = None,
                read_file: tuple = None, centralize_options=False):
        """
        Initiates the table object with de following parameters:

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
                                  .csv and .json files by now, default = None.
        :param read_file (tuple): A optional param which reives a tuple containing the first index as a path
                                  with the file name you want to extract the data from to make a table scene,
                                  and the second index as the format of the file. It accepts only .csv and .json,
                                  files by now, default = None
                                  
        *** USE CLI CONSTANTS (*_FORMAT) TO DEFINE THE FORMAT OF THE SAVE_FILE AND READ_FILE PARAMS ***
        """

        self.name = name
        self.table_options = table_options
        self.links = links
        self.change_callback = change_callback

        self.save_file = save_file
        self.read_file = read_file

        if save_file:
            self.save_file_path = save_file[0]
            self.save_file_format = save_file[1]

        if read_file:
            self.table_info = self.extract_data_frame_from_file(read_file[0], read_file[1])
        else:
            self.table_info = pd.DataFrame(table_info) if type(table_info) is dict else table_info

        if changeble_table:
            self.table_options = ['Change table'] + self.table_options
            self.links = [self.change_data] + self.links

        self.table_options = make_options_string(self.table_options, centralize_options)

    def extract_data_frame_from_file(self, path: str, file_format: int) -> "DataFrame":
        """
        It reads the file with the specified format and return the panda's DataFrame

        :param path (string): The specified  file path which will be readen.
        :param file_format (int): The specified file format which will be readen.
        """

        if file_format == 0:
            return pd.read_csv(path)

        if file_format == 1:
            return pd.read_json(path)

    def render(self) -> None:
        """
        It render all the options and print the data frame (table_info)
        """
        print(self.table_options)
        print("\n")
        print(self.table_info)

    def file_saver(self) -> None:
        """
        It saves the file with de updated data with the specified format.
        """

        if self.save_file_format == 0:
            self.table_info.to_csv(self.save_file_path)

        if self.save_file_format == 1:
            self.table_info.to_json(self.save_file_path)
        
    def change_data(self) -> None:
        """
        Change the table data
        """

        change = ['Wich column would you like to change?', 'Wich line would you like to change', 'Type the new value']
        for i in range(0, 3):
            system('cls')

            self.render()
            
            print(change[i])

            user_input = input('\n> ')
            change[i] = user_input

        column = int(change[0]) - 1
        line = int(change[1]) - 1

        new_value = change[2]
        self.table_info[list(self.table_info)[column]][line] = new_value

        if self.change_callback:
            self.change_callback(self.table_info)
        
        if self.save_file:
            self.file_saver()

    def get_links(self) -> list:
        return self.links


    def get_name(self) -> str:
        return self.name