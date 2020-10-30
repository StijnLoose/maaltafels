from Tkinter import *
from sys import *
from numpy import *
import random
import string
from datetime import datetime, date
import time

count = -1
run = False
show="a"

def var_name(mark):
   def value():
      if run:
         global count, show
         # Just beore starting
         if count == -1:
            show = "Starting..."
         else:
             mins = count // 60
             sec = count % 60
             hours = mins // 60
             mins = mins % 60
             show=("{0}:{1}:{2}").format(int(hours),int(mins),sec)
         mark['text'] = show
         mark.after(1000, value)
         count += 1
   value()

def Start(mark):
    global run
    run = True
    var_name(mark)

def Stop():
    global run
    run = False


def genereer(matrix):
    global oefeningen, oefen, invoer, go, klok
    Start(klok)
    eind_oef.config(state="active")
    go.config(state="disabled")
    matrix=array([[None,None,None]])
    i=0
    rij=0
    kol=0
    while i<100:
        a=random.randint(0,9)+1
        b=random.randint(0,9)+1
        c=a*b
        matrix=append(matrix,[[a,b,c]],0)
        i+=1
    oefeningen=delete(matrix,[0],0)
    j=0
    while j<50:
        if rij==10:
            rij=0
            kol+=1
        wat=str(oefeningen[j][0])+" x "+str(oefeningen[j][1])+" ="
        hup=Label(oefen, bg="grey", text=wat, width=10, font=("Courier", 15))
        hup.grid(row=rij, column=2*kol)
        antw=Entry(oefen, width=4, font=("Courier", 15))
        antw.insert(0,0)
        antw.grid(row=rij, column=2*kol+1)
        invoer.append(antw)
        j+=1
        rij+=1
    k=50
    tussenregel=Label(oefen, width=25, bg='green', text="       ")
    tussenregel.grid(row=10, column=0, columnspan=5)
    reke=11
    klm=0
    while k<100:
        if reke==21:
            reke=11
            klm+=1
        vraag=str(oefeningen[k][2])+" : "+str(oefeningen[k][0])+" ="
        hup=Label(oefen, bg="grey", text=vraag, width=10, font=("Courier", 15))
        hup.grid(row=reke, column=2*klm)
        antw=Entry(oefen, width=4, font=("Courier", 15))
        antw.insert(0,0)
        antw.grid(row=reke, column=2*klm+1)
        invoer.append(antw)
        k+=1
        reke+=1


def resultaat():
    global result, oefeningen, invoer, naam, score
    Stop()
    result.grid(row=2, column=2)
    eind_oef.config(state="disabled")
    bewaar.config(state="active")
    antwoorden=[]
    for d in invoer:
        z=int(d.get())
        antwoorden.append(z)
    score=0
    a=0
    c=50
    i=len(antwoorden)
    while a<50:
        if antwoorden[a]==oefeningen[a][2]:
            score+=1
        a+=1
    while c<i:
        if antwoorden[c]==oefeningen[c][1]:
            score+=1
        c+=1
    tekst="Je behaalde %d/100" %score
    result.config(text=tekst)
    opslaan()


def nieuw():
    raam=Toplevel()
    raam.title("naam ingeven")
    lab_naam=Label(raam, text="naam: ")
    lab_naam.grid(column=0, row=0)
    lab_klsnr=Label(raam, text="klasnummer: ")
    lab_klsnr.grid(row=1, column=0)
    ent_naam=Entry(raam, width=10, font=("Courier", 15))
    ent_naam.grid(row=0, column=1)
    ent_klsnr=Entry(raam, width=10, font=("Courier", 15))
    ent_klsnr.grid(row=1, column=1)
    def lees():
        global naam, klasnr
        a=ent_naam.get()
        b=ent_klsnr.get()
        naam=a
        klasnr=b
    knop=Button(raam, text="Laat die oefeningen maar komen", command= lambda :[lees(),raam.destroy(),genereer(oefeningen)])
    knop.grid(row=2, column=0, columnspan=2)

def opslaan():
    global naam, klasnr, score, count, run, show, oefeningen, invoer
    file=open("resultaat.txt","a")
    TS=datetime.now()
    dag=TS.strftime("%d/%m/%Y %H:%M")
    tijd=klok['text']
    resultaat=str(klasnr)+" "+str(naam)+" "+str(dag)+" "+str(score)+"/100 "+str(tijd)+"\n"
    file.write(resultaat)
    file.close()
    go['state']="active"
    count = -1
    run = False
    show="a"
    oefeningen=array([[]])
    invoer=[]
    naam="onbekend"
    klasnr=999
    score=0



oefeningen=array([[]])
invoer=[]
naam="onbekend"
klasnr=999
score=0

root = Tk()
root.title('rekenen voor Casper')
hoogte = 2500
breedte = 5000
root.maxsize(breedte, hoogte)
root.config(bg='grey')

boven= Frame(root, bg='#bada55')
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)
boven.grid(columnspan=15, rowspan=3, sticky=NW+SE)

tekstboven=Label(boven, bg='#bada55', font=("Courier", 20),text="Hier zijn er 50 maal-oefeningen en 50 deel-oefeningen. \n Maak ze zo snel mogelijk. Hopelijk gaat het steeds sneller")
Grid.rowconfigure(boven, 0, weight=1)
Grid.columnconfigure(boven, 0, weight=1)
tekstboven.grid(row=0, column=0, columnspan=4, sticky=W)

go=Button(boven, bg='green', text="start oefeningen", width=10,command= nieuw)
Grid.rowconfigure(boven, 0, weight=1)
Grid.columnconfigure(boven, 1, weight=1)
go.grid(row=1, column=0, sticky=NW+SE)

halt=Button(boven, bg='red', text="STOP", width=10, command= root.destroy)
Grid.rowconfigure(boven, 0, weight=1)
Grid.columnconfigure(boven, 1, weight=1)
halt.grid(row=1, column=3, sticky=NW+SE)

ruimte=Label(boven, bg='#bada55', width=25)
Grid.rowconfigure(boven, 0, weight=1)
Grid.columnconfigure(boven, 3, weight=1)
ruimte.grid(row=1, column=1, sticky=NW+SE)


tijd=Frame(root, bg="blue")
Grid.rowconfigure(root,5, weight=1)
Grid.columnconfigure(root, 10, weight=1)
tijd.grid(row=3, column=3, rowspan=10)

""" DE FUNCTIE VAN DEZE KNOP ZIT NU IN KNOP EIND-OEF
bewaar=Button(tijd, bg='green', text="bewaar mijn score", command=opslaan, state="disabled")
Grid.rowconfigure(tijd, 0, weight=1)
Grid.columnconfigure(tijd, 0, weight=1)
bewaar.grid(row=8, column=1)
"""

result=Label(tijd, text="____", width=20)

klok=Label(tijd, width=15, font=("Courier", 15), bg="blue" )
klok.grid(row=1, column=1)

eind_oef=Button(tijd, text="KLAAR!", command=resultaat, width=10, state="disabled")
eind_oef.grid(row=2, column=1)


oefen=Frame(root, bg='green')
Grid.rowconfigure(root,10, weight=1)
Grid.columnconfigure(root, 10, weight=1)
oefen.grid(row=3, column=0)


root.mainloop()
