#&/xZ

#Bibliotecas
#Pegar dia/hora
import datetime
#Barulho beep
import winsound
#Janela
from tkinter import *
from tkinter import messagebox
#Funções com o tempo
import time

print("Não se preocupe com o horario,\nO programa te avisará 10 minutos antes e exatamente na hora que sua aula começar...\nAh! ele tambem fechará sozinho quando todas as suas aulas do dia terminarem.\nTenha um bom dia!! :)\n                                                    &/xZ")

#Lista de horarios
horarios = ["07:40","08:45","10:40","11:30","14:30","15:40"]
horarios2 = ["07:50","08:55","10:50","11:40","14:40","15:50"]

#Horario que abriu o programas
hora = (datetime.datetime.today().strftime("%H")+":"+(datetime.datetime.today().strftime("%M")))


#Função de remover horarios
def removdia():
    #Dia da semana
    dia = (datetime.datetime.today().weekday())
    
    #Segunda
    if dia == 0:
        #Mudar mensagem final
        texto="amanha"
        #Remover horarios que não sao do dia
        horarios.remove("11:30")
        horarios.remove("15:40")
        horarios2.remove("11:40")
        horarios2.remove("15:50")
        #Ultimo horario
        ultimoh = "14:41"
        #Nome do dia
        nomedia = "Segunda"
        #Retornar valores para fora da função
        return(ultimoh,nomedia,texto)

    #Terça
    if dia == 1:
        texto="amanha"
        horarios.remove("14:30")
        horarios.remove("15:40")
        horarios2.remove("14:40")
        horarios2.remove("15:50")
        ultimoh = "11:41"
        nomedia = "Terça"
        return(ultimoh,nomedia,texto)

    #Quarta
    if dia == 2:
        texto="amanha"
        horarios.remove("11:30")
        horarios.remove("14:30")
        horarios.remove("15:40")
        horarios2.remove("11:40")
        horarios2.remove("14:40")
        horarios2.remove("15:50")
        ultimoh = "10:51"
        nomedia = "Quarta"
        return(ultimoh,nomedia,texto)

    #Quinta
    if dia == 3:
        texto="amanha"
        horarios.remove("10:40")
        horarios.remove("11:30")
        horarios2.remove("10:50")
        horarios2.remove("11:40")
        ultimoh = "15:51"
        nomedia = "Quinta"
        return(ultimoh,nomedia,texto)

    #Sexta
    if dia == 4:
        texto="semana que vem"
        horarios.remove("11:30")
        horarios.remove("14:30")
        horarios.remove("15:40")
        horarios2.remove("11:40")
        horarios2.remove("14:40")
        horarios2.remove("15:50")
        ultimoh = "10:51"
        nomedia = "Sexta"
        return(ultimoh,nomedia,texto)

#Função do barulho beep
def beep():
    #Frequencia do barulho
    frequency = 1250
    #Duração do barulho
    duration = 1000
    #Adicionar as informações
    winsound.Beep(frequency , duration )

#Função da janela 10 min   
def janela10min():
    #Nomear a janela
    window = Tk()
    #Mapear a janela
    window.wm_withdraw()
    #Dar atributos(Sempre no topo)
    window.wm_attributes("-topmost", 1)
    #Tamanho da janela
    window.geometry("1x1+500+500")
    #Informações da janela
    messagebox.showwarning(title = "Aulas de " +nomedia, message = "Sua aula começa em 10 minutos...",parent = window)

#Função da janela na hora 
def janelahora():
    window1 = Tk()
    window1.wm_withdraw()
    window1.wm_attributes("-topmost", 1)
    window1.geometry("1x1+500+500")
    messagebox.showerror(title = "Aulas de " +nomedia, message = "Sua aula vai começar agora...",parent = window1)

#Função da janela do ultimo horario  
def janelaultimo():
    window2 = Tk()
    window2.wm_withdraw()
    window2.wm_attributes("-topmost", 1)
    window2.geometry("1x1+500+500")
    messagebox.showwarning(title = "&/xZ", message = "Suas aulas de hoje acabaram, te vejo {} ;)".format(texto),parent = window2)

#Função para dar loop
def loop():
    #Ficar pegando a hora
    hora = (datetime.datetime.today().strftime("%H") + ":" + (datetime.datetime.today().strftime("%M")))
    while hora not in horarios and hora not in horarios2:
        hora = (datetime.datetime.today().strftime("%H") + ":" + (datetime.datetime.today().strftime("%M")))

    #Chamar função antes dos 10 min
    if hora in horarios:
        beep()
        janela10min()
        time.sleep(60)

    #Chamar a função no horario da aula
    if hora in horarios2:
        beep()
        janelahora()
        time.sleep(60)        

#Retornar as variaveis da função
ultimoh,nomedia,texto = removdia()

#Fechar no ultimo horario
while hora != ultimoh:
    loop()
    hora = (datetime.datetime.today().strftime("%H")+":"+(datetime.datetime.today().strftime("%M")))

#Abrir a janela avisando que terminou
janelaultimo()

