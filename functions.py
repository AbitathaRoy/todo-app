def get_todos(filepath="todos.txt"):  # default parameter defined
    """ Read a text file and return the list of to-do items.
    """
    with open(filepath, "r") as file_local :
        local_todos = file_local.readlines();
    return local_todos;


def write_todos(todos_arg, filepath="todos.txt") :
    """ Write the to-do items in the list.
    """
    with open(filepath, "w") as file:
        file.writelines(todos_arg);  # completely overrides the existing file
