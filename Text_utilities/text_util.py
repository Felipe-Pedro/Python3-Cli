def get_string_in_range(string, number, string_size) -> str:
    """
    It returns the string in the specified number.

    :param string (str): The string which will be devided.
    :param number (int): The size of each piece of string.
    """
    #If the size of the string if less than the number of characters it will return the full string,
    #and end the function
    if number > string_size:
        yield string
        return
    
    for i in range(0, round(len(string) / number + 0.5)):
        if number > len(string):
            yield string
        yield string[i * number: number * (i + 1)]

def divide_string(string_to_divide: str, char_per_index: int) -> list:
    """
    It returns a list of parts of one string.

    :param string_to_divide (str): The string which will be devided.
    :param char_per_index (int): The amount of chars on each index of the list.
    """

    string_size = len(string_to_divide)

    result =  [part for part in get_string_in_range(string_to_divide, char_per_index, string_size)]
    return result

def centralize_list(list_of_strings: list) -> None:
    """
    It centralizes all the content of a list in place.

    :param list_of_strings (list): The list containing all the strings to centralize
    """
    for i in range(len(list_of_strings)):
        list_of_strings[i] = list_of_strings[i].center(120)

