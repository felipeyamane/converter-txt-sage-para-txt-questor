from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tkinter.filedialog import asksaveasfile
from tkinter import filedialog

Tk().withdraw()  # Isto torna oculto a janela principal
filename = askopenfilename()  # Isto te permite selecionar um arquivo
print(filename)  # printa o arquivo selecionado
arq = list()
'''/*---------------------*/'''

with open(filename) as f:
    for line in f:
        file = (f'001;0{line[0:5]};{line[6:9]};00000;{line[18:27]};\n')
        arq.append(file)
        print(arq)
path = filedialog.asksaveasfilename(filetypes = [('Texto', '.txt')])
print(path)
arquivo = open(path, "a")
print(arquivo)
arquivo.writelines(arq)