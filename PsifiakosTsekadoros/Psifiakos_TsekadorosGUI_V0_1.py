
#
# Grafiko programa eksomiosis Tsekadorou
# copyright (C) Nick isaris 
# Published under the GPL V2
#
# Program Version 0.1 (GUI)
#
# Changelog:
#
#
#
#

from Tkinter import *
import tkMessageBox
import time
import sys
            #Edw yparxei ena polu oreo paradigma me leksika mesa se leksika

#Leksika proionton
proionta = {'pota':{'apla_pota': 0,'special_pota': 0},
            'fiales':{'aples_fiales': 0,'special_fiales': 0},
            'kanates':{'kanates': 0}
            }
#leksika kerasmenon proionton 
kerasmena = {'pota':{'kerasmena_apla_pota': 0,'kerasmena_special_pota': 0},
            'fiales': {'kerasmenes_aples_fiales': 0,'kerasmenes_special_fiales': 0},
            'kanates':{'kerasmenes_kanates': 0}
             }
          
#Metavlites timon potou
timi_pota = 7
timi_special_pota = 8

#Metavlites timon Fialis
timi_fialis = 70
timi_special_fialis = 80

#Metavlites timi Kanatas
timi_kanatas = 15

#################Sinartisis############################

#Sinartisi prosthikis timis
def prosthiki_posotitas_func():

    #Pota
    if entry_apla_pota.get() != "":
        
        try:
            proionta['pota']['apla_pota'] += int(entry_apla_pota.get())
            apla_pota_tipoma = 'Apla pota: ' + str(proionta['pota']['apla_pota'])
            var.set(apla_pota_tipoma)
            
        except:
            tkMessageBox.showwarning('Error',
            "Ta pedia dexonte mono arithmous")
            
    if entry_special_pota.get() != "":
        
        try:
            proionta['pota']['special_pota'] += int(entry_special_pota.get())
            special_pota_tipoma = 'Special Pota: ' + str(proionta['pota']['special_pota'])
            var2.set(special_pota_tipoma)
            
        except:
            tkMessageBox.showwarning('Error',
            "Ta pedia dexonte mono arithmous")

    if entry_aples_fiales.get() != "":
        
        try:
            proionta['fiales']['aples_fiales'] += int(entry_aples_fiales.get())
            aples_fiales_tipoma = 'Aples Fiales: ' + str(proionta['fiales']['aples_fiales'])
            var2.set(aples_fiales_tipoma)
            
        except:
            tkMessageBox.showwarning('Error',
            "Ta pedia dexonte mono arithmous")

    if entry_special_fiales.get() != "":
        
        try:
            proionta['fiales']['special_fiales'] += int(entry_special_fiales.get())
            special_fiales_tipoma = 'Aples Fiales: ' + str(proionta['fiales']['special_fiales'])
            var2.set(special_fiales_tipoma)
            
        except:
            tkMessageBox.showwarning('Error',
            "Ta pedia dexonte mono arithmous")
            
    if entry_kanates.get() != "":
        
        try:
            proionta['kanates']['kanates'] += int(entry_kanates.get())
            special_fiales_tipoma = 'Kanates: ' + str(proionta['kanates']['kanates'])
            var2.set(kanates_tipoma)
            
        except:
            tkMessageBox.showwarning('Error',
            "Ta pedia dexonte mono arithmous")

    #Kalo tin sinartisi gia katagrafi katanalosis
    arxeio_katanalosi()
    
    #Diagrafi pedion kataxoriseon ton box
    entry_apla_pota.delete(0,10)
    entry_special_pota.delete(0,10)
    entry_aples_fiales.delete(0,10)
    entry_special_fiales.delete(0,10)
    entry_kanates.delete(0,10)

#Sinartisi aferesis posotitas
def aferesi_posotitas_func():
    pass

#Sinartisi gia katagrafi katanalosis se arxeio
def arxeio_katanalosi(filepath = 'tamio.txt'):
    
    orig_stdout = sys.stdout
    arxeio = file(filepath, 'w')
    sys.stdout = arxeio
    
    print "############## Katanalosi ################"
    print ""
    print "Pota: "
    for pota_list in proionta['pota']:
        print pota_list + ':', proionta['pota'][pota_list]

    print ""
    print "Fiales: "   
    for fiales_list in proionta['fiales']:
        print fiales_list + ':', proionta['fiales'][fiales_list]

    print ""
    print "Kanates:"
    for kanates_list in proionta['kanates']:
        print kanates_list + ':', proionta['kanates'][kanates_list]

    print ""
    print "############### Kerasmata ###############"
    print ""
    print "Pota:"
    for kerasmena_pota_list in kerasmena['pota']:
        print kerasmena_pota_list + ':', kerasmena['pota'][kerasmena_pota_list]

    print ""
    print "Fiales:"
    
    for kerasmenes_fiales_list in kerasmena['fiales']:
        print kerasmenes_fiales_list + ':', kerasmena['fiales'][kerasmenes_fiales_list]
    print ""
    
    print "Kanates:"
    for kerasmenes_kanates_list in kerasmena['kanates']:
        print kerasmenes_kanates_list + ':', kerasmena['kanates'][kerasmenes_kanates_list]
        
    sys.stdout = orig_stdout
    arxeio.close()

#Sinartisi gia klisimo tamiou
def tamio_func():
    
    arxeio_katanalosi('Z.txt')
    tamio = (proionta['pota']['apla_pota'] * timi_pota) + (proionta['pota']['special_pota'] * timi_special_pota) + (proionta['fiales']['aples_fiales'] * timi_fialis) + (proionta['fiales']['special_fiales'] * timi_special_fialis) + (proionta['kanates']['kanates'] * timi_kanatas)

    kerasmeno_tamio = (kerasmena['pota']['kerasmena_apla_pota'] * timi_pota) + (kerasmena['pota']['kerasmena_special_pota'] * timi_special_pota) + (kerasmena['fiales']['kerasmenes_aples_fiales'] * timi_fialis) + (kerasmena['fiales']['kerasmenes_special_fiales'] * timi_special_fialis) + (kerasmena['kanates']['kerasmenes_kanates'] * timi_kanatas)
    #Edw yparxei mia xrisimi loopa oste na mporoume
    #na tiponoume tin print se arxio kai meta na klinoume to arxeio
    #oste na mporesoume na paroume print kai stin othoni
    #xoris na katagraftoun oloi h eksodos tou programatos se arxeio.
    
    orig_stdout = sys.stdout #Auti h metavliti dimiourgithike gia na
                             #apeleftherosoume stin poria tin timi tis sys.stdout apo to
                             #arxeio pou tha kanoume open gia na mporesou me na to klisoume
    arxeio = file('Z.txt', 'a')
    
    sys.stdout = arxeio
    
    print ""
    print "################ Tamio Z #################"
    print ""
    print "Tamio:",tamio, "Euro"
    print ""
    print "Kerasmata:",kerasmeno_tamio, "Euro"
    print ""

    sys.stdout = orig_stdout # Dilonoume na parei to sys.stdout 
                             # San timi tin metavliti orig_stdout
                             # Gia na apeleftherosoume to arxeio katagrafis
                             # kai na mporesoume na to klisoume
                             # PROSOXEI XORIS AYTON TON TROPO DN GINETE.
    arxeio.close()
   
    

root = Tk()
root.geometry('450x450+500+300')
#root.minsize(600,600)
root.title("Psifiakos Tsekadoros")
root.message = "TEST"

#
var = StringVar()
var2 = StringVar()
label = Label(root, textvariable=var)
label2 = Label(root, textvariable=var2)
#


#Dimiourgia etiketon kai box
label_apla_pota = Label( root, text="Apla pota: ")
entry_apla_pota = Entry(root,justify =CENTER, bd =10)

label_special_pota = Label( root, text="Special Pota: ")
entry_special_pota = Entry(root,justify =CENTER, bd =10)

label_aples_fiales = Label( root, text="Aples Fiales: ")
entry_aples_fiales = Entry(root,justify =CENTER, bd =10)

label_special_fiales = Label( root, text="Specia Fiales: ")
entry_special_fiales = Entry(root,justify =CENTER, bd =10)

label_kanates = Label( root, text="Kanates: ")
entry_kanates = Entry(root,justify =CENTER, bd =10)



    

#Dimiourgia koumpion
koumpi_prosthiki_posotitas = Button(root, text ="Prosthiki Posotitas",width = 15, command = prosthiki_posotitas_func)
koumpi_aferesi_posotitas = Button(root, text ="Aferesi Posotitas",width = 15, command = aferesi_posotitas_func)
koumpi_tamio = Button(root, text ="Tamio",width = 15, command = tamio_func)


#
Label(text = '######### Katanalosi #########').pack()

label_apla_pota.pack()
label_special_pota.pack()
label_aples_fiales.pack()
label_special_fiales.pack()
label_kanates.pack()

Label(text = '#########  Kerasmata #########').pack()
#

#Methodi emfanisis etiketon kai box
label_apla_pota.pack()
entry_apla_pota.pack()


label_special_pota.pack()
entry_special_pota.pack()

label_aples_fiales.pack()
entry_aples_fiales.pack()

label_special_fiales.pack()
entry_special_fiales.pack()

label_kanates.pack()
entry_kanates.pack()

#Emfanisis Koumpion
koumpi_tamio.pack(side =BOTTOM)
koumpi_aferesi_posotitas.pack(side =BOTTOM)
koumpi_prosthiki_posotitas.pack(side =BOTTOM)

root.mainloop()
