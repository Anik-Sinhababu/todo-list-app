import functions
import PySimpleGUI as sg

label = sg.Text("Type in a To-Do Item", text_color="white", background_color="indian red")
input_box = sg.InputText(tooltip="Enter a todo item")
button = sg.Button('Add', button_color="black")
window = sg.Window('MY TO_DO APP', layout=[[label], [input_box, button]], background_color="light coral")
window.read()
window.close()