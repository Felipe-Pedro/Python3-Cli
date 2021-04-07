from Text_utilities.text_util import divide_string, centralize_list

def make_options_string(options_list, centralize_options):

    option_string = ""

    for i in range(0, len(options_list)):
        option_string += f"{i + 1} - {options_list[i]} \t"

    if centralize_options:
        option_string = option_string.center(120)

    return option_string

def make_body_string(body_string, char_per_line, centralize_body):
    body_list = divide_string(body_string, char_per_line)

    if centralize_body:
        centralize_list(body_list)

    return "\n".join(body_list)