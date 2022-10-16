"""
    Algoritmo desenvolvido por José Antonio (Stunt106), 2022
    https://github.com/stun106/
"""
from typing import *
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
import datetime as dt 
import pkg_resources
''' import awesometkinter as atk '''
from insert_cliente import inserirCliente
from select_cliente import lista_clientes



class telaClientes:
    def __init__(self, root) -> None:
        self.root = root
        self.FrameClientes()
        self.FrameTabelaClientes()
        self.LabelsandEntrys()
        self.btnSubmit()
        self.ListaClientes()

    
    def atkInstalado(self) -> bool:
        modulo = "awesometkinter".upper()
        instalados = {pkg.key.upper() for pkg in pkg_resources.working_set}
        return (True if modulo in instalados else False)


    def FrameClientes(self):
        self.Frame1 = Frame(self.root, bg = '#ffffff')
        self.Frame1.place(relx = 0.02, rely = 0.05, relwidth = 0.28, relheight = 0.9)
    

    def FrameTabelaClientes(self):
        self.Frame2 = Frame(self.root, bg = '#F2E8DF')
        self.Frame2.place(relx = 0.32, rely = 0.05, relwidth = 0.66, relheight = 0.9 )
    

    def LabelsandEntrys(self):  
        #clientes
        #frame1 header
        self.LabelCli = Label(self.Frame1,text = "Clientes", bg = '#ffffff')
        self.LabelCli.configure(font=('Courier',25))
        self.LabelCli.place(relx = 0.17,rely = 0.1)

        # Labels&Entrys1
        nameVar = StringVar()
        self.NameLb = Label(self.Frame1,text = 'Nome*', bg = '#ffffff')
        self.NameLb.place(relx = 0.05, rely = 0.3)
        self.NameEntry = Entry(self.Frame1, bg='#f7f7f7', textvariable=nameVar)
        self.NameEntry.place(relx = 0.05, rely = 0.34, relwidth = 0.80, relheight = 0.04 )
        
        addressVar = StringVar()
        self.addressLb = Label(self.Frame1,text = 'Endereço*', bg = '#ffffff')
        self.addressLb.place(relx = 0.05, rely = 0.4)
        self.addressEntry = Entry(self.Frame1, bg = '#f7f7f7', textvariable=addressVar)
        self.addressEntry.place(relx = 0.05, rely = 0.44, relwidth = 0.80, relheight = 0.04)

        emailVar = StringVar()
        self.EmailLB = Label (self.Frame1, text = 'Email*', bg = '#ffffff')
        self.EmailLB.place(relx = 0.05, rely = 0.5)
        self.EmailEntry = Entry(self.Frame1, bg = '#f7f7f7', textvariable=emailVar)
        self.EmailEntry.place(relx = 0.05, rely = 0.54, relwidth = 0.80, relheight = 0.04)
        
        telVar = StringVar()
        self.TelLB = Label(self.Frame1,text = 'Telefone', bg = '#ffffff')
        self.TelLB.place(relx = 0.05, rely = 0.6)
        self.TelEntry = Entry(self.Frame1, bg = '#f7f7f7', textvariable=telVar)
        self.TelEntry.place(relx = 0.05, rely = 0.64, relwidth = 0.80, relheight = 0.04)

        self.dateLB = Label(self.Frame1, text = f'{dt.datetime.now():%a, %b %d, %y}', bg = '#ffffff')
        self.dateLB.place(relx = 0.35, rely = 0.9)

        self.matriculaEntry = Label(self.Frame1, bg = '#f7f7f7')
        self.matriculaEntry.place(relx = 0.05, rely = 0.9,relwidth = 0.08, relheight = 0.04)



    '''     #pedidos
        #frame2 header 
        self.LabelPedido = Label(self.Frame2,text = "Pedidos", bg = '#F2E8DF')
        self.LabelPedido.configure(font=('Courier',25))
        self.LabelPedido.place(relx = 0.35,rely = 0.04)
    
        #labels&entrys2
        self.idLbPed = Label(self.Frame2,text = "Id Pedido:", bg = '#F2E8DF')
        self.idLbPed.place(relx = 0.2,rely = 0.26)
        self.cliEntryped = Entry(self.Frame2, bg = '#f7f7f7')
        self.cliEntryped.place(relx = 0.2,rely = 0.3,relwidth = 0.2, relheight = 0.04)

        self.idcliPed = Label(self.Frame2,text = "Id Cliente:", bg = "#F2E8DF" )
        self.idcliPed.place(relx = 0.6,rely = 0.26)
        self.idcliPed = Entry(self.Frame2, bg = '#f7f7f7')
        self.idcliPed.place(relx = 0.6,rely = 0.3,relwidth = 0.2, relheight = 0.04)

        self.statusPed = Label(self.Frame2, text = 'Status:', bg = "#F2E8DF" )
        self.statusPed.place(relx = 0.2,rely = 0.36)
        lst = ['Aprovado', 'Pendente']
        self.Status = ttk.Combobox(self.Frame2, values = lst, background = '#f7f7f7')
        self.Status.place(relx = 0.2,rely = 0.4,relwidth = 0.2, relheight = 0.04)
        
        self.datePed = Label(self.Frame2, text = 'Data:', bg = "#F2E8DF")
        self.datePed.place(relx = 0.6,rely = 0.36)
        self.datePedEntry = Entry(self.Frame2, bg = '#f7f7f7')
        self.datePedEntry.insert(0,f'{dt.datetime.now():%a,%b,%d,%y}')
        self.datePedEntry.place(relx = 0.6,rely = 0.4,relwidth = 0.2, relheight = 0.04)

        self.vaLorPed = Label(self.Frame2,text = 'Valor Total:', bg = "#F2E8DF")
        self.vaLorPed.place(relx = 0.06, rely = 0.94)
        self.valorPedEntry = Entry(self.Frame2, bg = '#f7f7f7')
        self.valorPedEntry.place(relx = 0.22, rely = 0.94,relwidth = 0.18, relheight = 0.045)
    '''
    def btnSubmit(self):
        self.SubmitBtn = Button(self.Frame1,text = 'S a l v a r', command=lambda: self.SalvarClientes([
            self.NameEntry.get(),
            self.addressEntry.get(),
            self.EmailEntry.get(),
            self.TelEntry.get(),
        ]))
        self.SubmitBtn.place(relx = 0.2, rely = 0.74, relwidth = 0.6, relheight = 0.05)
    '''    
        self.SubmitBtn2 = Button(self.Frame2,text = 'S u b m i t')
        self.SubmitBtn2.place(relx = 0.69, rely = 0.93, relwidth = 0.23, relheight = 0.055)  '''

    def SalvarClientes(self, lista:List):
        inserirCliente(lista)


    def ListaClientes(self):
        self.listaCli = ttk.Treeview(self.Frame2, height = 7, columns = ('col1','col2' , 'col3', 'col4', 'col5'), show='headings')
        
        #cabeçalho
        self.listaCli.heading('#0',text ='')
        self.listaCli.heading('#1',text ='Matrícula')
        self.listaCli.heading('#2', text = 'Nome')                               
        self.listaCli.heading('#3', text = 'Endereço')
        self.listaCli.heading('#4', text = 'Email')
        self.listaCli.heading('#5', text = 'Telefone')
       
        self.listaCli.column('#0', width = 1)
        self.listaCli.column('#1',width = 20)
        self.listaCli.column('#2',width = 120)
        self.listaCli.column('#3',width = 150)
        self.listaCli.column('#4',width = 50)
        self.listaCli.column('#5',width = 50)
        self.listaCli.place(relx = 0.06, rely = 0.06, relwidth = 0.88, relheight = 0.89) 

        
        for cliente in lista_clientes():
            self.listaCli.insert('', END, values=cliente)  
        
