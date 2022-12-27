# # todo with context manager
# while True:
#     user_action = input("Enter the action you want to perform\nadd\t\tshow\tedit\tcomplete\n")
#     match user_action:
#         case 'add':
#             todo = input("Enter a todo work:- ") + "\n"
#             with open("../pythonProject3/todos.txt", 'r') as file:
#                 todos = file.readlines()
#             todos.append(todo)
#             with open("../pythonProject3/todos.txt", 'w') as file:
#                 file.writelines(todos)
#
#         case 'show':
#             with open("../pythonProject3/todos.txt", 'r') as file:
#                 todos = file.readlines()
#             for index, items in enumerate(todos):
#                 items.strip('\n')
#                 print(index+1, items)
#
#         case 'edit':
#             num = int(input("Enter the index number at which you want to delete the content\n"))
#             with open("../pythonProject3/todos.txt", 'r') as file:
#                 todos = file.readlines()
#             num = num-1
#             todos[num] = input("Enter the todo you wna tto enter newly\n") + '\n'
#             with open("../pythonProject3/todos.txt", 'w') as file:
#                 file.writelines(todos)
#
#         case 'complete':
#             num = int(input("Enter the number that you want to remove from the todo list"))
#             num = num-1
#             with open("../pythonProject3/todos.txt", 'r') as file:
#                 todos = file.readlines()
#             todos.pop(num)
#             with open("../pythonProject3/todos.txt", 'w') as file:
#                 file.writelines(todos)


# todo with context manager
# while True:
#     user_action = input("Enter the action you want to perform\nadd\t\tshow\tedit\tcomplete\texit\n")
#
#     if 'add' in user_action:
#         todo = user_action[4:] + '\n'
#         with open("../pythonProject3/todos.txt", 'r') as file:
#             todos = file.readlines()
#         todos.append(todo)
#         with open("../pythonProject3/todos.txt", 'w') as file:
#             file.writelines(todos)
#
#     elif 'show' in user_action:
#         with open("../pythonProject3/todos.txt", 'r') as file:
#             todos = file.readlines()
#         for index, items in enumerate(todos):
#             items.strip('\n')
#             print(index+1, items)
#
#     elif 'edit' in user_action:
#         num = int(input("Enter the index number at which you want to delete the content\n"))
#         with open("../pythonProject3/todos.txt", 'r') as file:
#             todos = file.readlines()
#         num = num-1
#         todos[num] = input("Enter the todo you wna tto enter newly\n") + '\n'
#         with open("../pythonProject3/todos.txt", 'w') as file:
#             file.writelines(todos)
#
#     elif 'complete' in user_action:
#         num = int(input("Enter the number that you want to remove from the todo list"))
#         num = num-1
#         with open("../pythonProject3/todos.txt", 'r') as file:
#             todos = file.readlines()
#         todos.pop(num)
#         with open("../pythonProject3/todos.txt", 'w') as file:
#             file.writelines(todos)
#     elif 'exit' in user_action:
#         break
#     elif user_action != ('show', 'complete', 'edit', 'add', 'exit'):
#         print("\033[1;4mEnter a valid keyword\033[0m\n")

# todo with try except and continue codeblocks

from functions import get_todos, write_todos
import time


now = time.strftime('%A\nDate:-%d-%b-%y\nTime:-%H:%M:%S')
print("The date is as below")
print(now)
while True:
    user_action = input("Enter the action you want to perform\nadd\t\tshow\tedit\tcomplete\texit\n")

    if 'add' in user_action:
        try:
            todo = user_action[4:] + '\n'
            todos = get_todos()
            todos.append(todo)
            write_todos(todos)
        except ValueError:
            print("Wrong command, Enter again")
            continue

    elif 'show' in user_action:
        todos = get_todos()
        for index, items in enumerate(todos):
            items.strip('\n')
            print(index + 1, items)

    elif 'edit' in user_action:
        try:
            num = int(user_action[5:])
            todos = get_todos()
            num = num - 1
            todos[num] = input("Enter the todo you wna tto enter newly\n") + '\n'
            write_todos(todos)
        except ValueError:
            print(" wrong input command")

    elif 'complete' in user_action:
        num = int(user_action[9:])
        num = num - 1
        todos = get_todos()
        todos.pop(num)
        write_todos(todos)
    elif 'exit' in user_action:
        break
    elif user_action != ('show', 'complete', 'edit', 'add', 'exit'):
        print("\033[1;4mEnter a valid keyword\033[0m\n")
