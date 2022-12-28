from functions import get_todos, write_todos
import PySimpleGUI as sg
import time


clock = sg.Text(key="clock", background_color="lavender", text_color="black", font=("Dina", 11))
label = sg.Text("Type in a To-Do Item", text_color="black", background_color="lavender blush2")
input_box = sg.InputText(tooltip="Enter a todo item", key="todo")
button = sg.Button('Add', button_color="gray15", size=10)
list_box = sg.Listbox(values=get_todos(), key='todos', enable_events=True, size=[45,0], background_color="lavender")
edit_button = sg.Button("Edit", button_color="gray15")
complete_button = sg.Button("Complete", button_color="gray15")
exit_button = sg.Button("Exit", button_color="gray15")
window = sg.Window('MY TO_DO APP', layout=[[label, clock], [input_box, button],
                                           [list_box, edit_button, complete_button], [exit_button]],
                   background_color="gray25",
                   font=('Dina', 12), icon="todo.ico")

while True:
    event, values = window.read(timeout=10)
    window["clock"].update(value=time.strftime("%A\nDate:-%d-%b-%y\nTime:-%H:%M:%S"))
    match event:
        case 'Add':
            todos = get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            write_todos(todos)
            window['todo'].update(value="")
            window['todos'].update(values=todos)

        case 'Edit':
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']
                todos = get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Try selecting an item first, then go for editing!!!! ", title="Caution",
                         font=("helvetica", 11), icon="caution.ico")

        case 'Complete':
            try:
                todo_to_complete = values['todos'][0]
                todos = get_todos()
                todos.remove(todo_to_complete)
                write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                sg.popup("To complete a task first select a task", title="Caution",
                         font=("helvetica", 11), icon="caution.ico")
        case 'todos':
            input_box = window['todo'].update(value=values['todos'][0])
        case 'Exit':
            exit()
        case sg.WIN_CLOSED:
            break

window.close()
