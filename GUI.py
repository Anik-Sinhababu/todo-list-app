from functions import get_todos, write_todos
import PySimpleGUI as sg

label = sg.Text("Type in a To-Do Item", text_color="black", background_color="lavender blush2")
input_box = sg.InputText(tooltip="Enter a todo item", key="todo")
button = sg.Button('Add', button_color="black")
list_box = sg.Listbox(values=get_todos(), key='todos', enable_events=True, size=[70, 5], background_color="lavender")
edit_button = sg.Button("Edit")
window = sg.Window('MY TO_DO APP', layout=[[label], [input_box, button],
                                           [list_box, edit_button]],
                   background_color="gray20",
                   font=('Dina', 13), icon="todo.ico")

while True:
    event, values = window.read()
    match event:
        case 'Add':
            todos = get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            write_todos(todos)
            window['todos'].update(values=todos)

        case 'Edit':
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']
            todos = get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            write_todos(todos)
            window['todos'].update(values=todos)

        case 'todos':
            input_box = window['todo'].update(value=values['todos'][0])

        case sg.WIN_CLOSED:
            break

window.close()
