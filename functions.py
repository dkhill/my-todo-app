FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """Reeds the todos file and returns a list of todos."""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """Writes the to-do items list to the text file"""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)

if __name__ == "__main__":
    print("Hello")
    print(get_todos())
