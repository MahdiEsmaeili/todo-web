FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    with open(filepath, "r") as file_todos:
        todos = file_todos.readlines()
        return todos


def write_todos(todos, filepath=FILEPATH):
    with open(filepath, "w") as file_todos:
        file_todos.writelines(todos)