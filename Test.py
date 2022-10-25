import PySimpleGUI as sg
import shutil, errno
src = ""
dest = ""
def copy(src, dest):
    try:
        shutil.copytree(src, dest)
    except OSError as e:
        # If the error was caused because the source wasn't a directory
        if e.errno == errno.ENOTDIR:
            shutil.copy(src, dest)
        else:
            print('Directory not copied. Error: %s' % e)

#Me testing out commands in PSG
layout = [[ sg.Text("Select path from source to destination")],
[sg.Text("Source Folder", size=(15,1)), sg.InputText(src),
sg.FolderBrowse()],
[sg.Text("Destination Folder", size=(15,1)),
sg.InputText(dest), sg.FolderBrowse()],
[sg.Button("Transfer", button_color=("white", "blue"), size=
(6, 1)),sg.Button("Copy", button_color=("white",
"green"), size=(6, 1)),sg.Exit(button_color=("white", "red"),
size=(6, 1))]]

window = sg.Window("Mass File Transfer").Layout(layout)

while True:
    event, values = window.Read()
    print(event, values)
    if event in (None, 'Exit'):
        break

    if event == 'Copy':
        copy(values[0], values[1])