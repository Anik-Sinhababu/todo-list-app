from functions import get_todos, write_todos
import PySimpleGUI as sg

label = sg.Text("Type in a To-Do Item", text_color="black", background_color="lavender blush2")
input_box = sg.InputText(tooltip="Enter a todo item", key="todo")
button = sg.Button('Add', button_color="black")
window = sg.Window('MY TO_DO APP', layout=[[label], [input_box, button]],
                   background_color="gray20",
                   font=('Dina', 13))
sg.TITLEBAR_MAXIMIZE_KEY
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'Add':
            todos = get_todos()
            print(todos)
            new_todo = values['todo'] + '\n'
            print(new_todo)
            todos.append(new_todo)
            write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()
