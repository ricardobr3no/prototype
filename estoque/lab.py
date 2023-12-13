from main import *
import PySimpleGUI as sg

lista = ['a', 'b']

layout = [[sg.Combo(lista)]]

window = sg.Window("oi", layout)
event, values = window.read()

window.close()
