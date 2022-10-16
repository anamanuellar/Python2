from tkinter import *
from menu import *

PERC_LARGURA = 80
PERC_ALTURA = 80

win = Tk()
# Janela principal
telaLarg=win.winfo_screenwidth()
telaAlt=win.winfo_screenheight()
win.title("Sistema de Registro e Controle")
win.configure(background = "#16878c")
win.resizable(True,True)
win.maxsize(width = 1080, height = 720)
win.minsize(width = 800, height = 600)

win.geometry(f"{str(int(telaLarg*(PERC_LARGURA/100)))}x{str(int(telaAlt*(PERC_ALTURA/100)))}")
app = MainMenu(win)
win.mainloop()