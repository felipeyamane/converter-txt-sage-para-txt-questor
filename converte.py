from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()  # Isto torna oculto a janela principal
filename = askopenfilename()  # Isto te permite selecionar um arquivo
print(filename)  # printa o arquivo selecionado

'''/*---------------------*/'''

d = {}
with open(filename) as f:
    for line in f:
        (key, val, val2, val3, val4, val5, val6) = line.split("|")
        d[int(key)] = val, val2, val3, val4, val5, val6
        #print(line[3:8])
print(f'{d[1]}')
