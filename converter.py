from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tkinter import filedialog
from time import sleep

Tk().withdraw()  # Isto torna oculto a janela principal
filename = askopenfilename()  # Isto te permite selecionar um arquivo
print(filename)  # printa o arquivo selecionado
arq = list()
linha = 0
execu = 0
'''/*---------------------*/'''

with open(filename) as f:  

    for line in f:
        file = (f'001;0{line[0:5]};{line[6:9]};00000;{line[18:27]};\n')
        arq.append(file)
path = filedialog.asksaveasfilename(filetypes = [('Texto', '.txt')])
path += '.txt'
arquivo = open(path, "a")
print('-------------------------------------------------------------------')
print(f'Arquivo convertido com sucesso, salvo em: {path}')
print('-------------------------------------------------------------------')
sleep(5)
arquivo.writelines(arq)