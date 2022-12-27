
def get_todos():
    with open("../pythonProject3/todos.txt", 'r') as local_file:
        local_todos = local_file.readlines()
    return local_todos


def write_todos(todos_args):
    with open("../pythonProject3/todos.txt", 'w') as local_file:
        local_file.writelines(todos_args)
