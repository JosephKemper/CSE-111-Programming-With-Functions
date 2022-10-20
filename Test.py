import PySimpleGUI as sg
import math

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Calculate Volume of sphere')],
            [sg.InputText(key='-NAME-')],
            [sg.InputText(key='Radius')],
            [sg.Submit(), sg.Cancel()] ]

window = sg.Window ('Josephs First window', layout)

event, values = window.read()

window.close()

def cal_sph_vol (radius):
    volume = (4/3)*math.pi*(radius**3)
    return volume

float_radius = float(values['Radius'])
sphere_volume = cal_sph_vol (float_radius)

sg.popup("The volume is", sphere_volume)

sg.popup(values['-NAME-'], 'entered', values["Radius"])

