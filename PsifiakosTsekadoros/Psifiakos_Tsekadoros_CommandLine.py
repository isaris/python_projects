#
# Programa eksomiosis Tsekadorou
#
#  copyright (C) Nick isaris 
#  Published under the GPL V2
#
# Program Version 0.2 (Command Line Only)
#
# Changelog:
#
# 1.Metatropoi ton metavliton katanalosis alla kai kerasmaton se leksika
# 2.Katagrafi katanalosis kai tamiou se arxeio txt
#
#
from Tkinter import *
import time
import sys
            #Edw yparxei ena polu oreo paradigma me leksika mesa se leksika

#Leksika proionton
proionta = {'pota':{'apla_pota': 0,'special_pota': 0},
            'fiales':{'aples_fiales': 0,'special_fiales': 0},
            'kanates':{'kanates': 0}
            }
#leksika kerasmaton
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

#Sinartisis tipomatos ston xristi
def tipoma_proionton ():
    print ""
    print ""
    print "###############################"
    print "#    Psifiakos Tsekadoros     #"
    print "###############################"
    print ""
    print "Diloste ton kodiko proiontos, gia paradigma (p gia apla pota), patiste enter , diloste ton arithmo posotitas kai patiste pali enter."
    print ""
    print "kodikoi proiontos:"
    print ""
    print "Pota:"
    print "  p) >> (Apla pota) |ENTER| >> (Arithmo posotitas) >> |ENTER|"
    print " sp) >> (Special pota) |ENTER| >> (Arithmo posotitas) >> |ENTER|"
    print " sp) >> (Kerasmena pota) |ENTER| >> (Arithmo posotitas) >> |ENTER|"
    print "ksp)>>(Kerasmena Special Pota) |ENTER| Kai arithmo posotitas |ENTER|"
    print ""
    print "Fiales:"
    print "  f) >> (Special Fiales) |ENTER| >> (Arithmo posotitas) >> |ENTER|"
    print " sf) >> (Special Fiales) |ENTER| >> (Arithmo posotitas) >> |ENTER|"
    print "ksf) >> (Kerasmenes Special Fiales) |ENTER| >> (Arithmo posotitas) >> |ENTER|"
    print ""
    print "Kanates:"
    print " k) >> (kanates) |ENTER| >> (Arithmo posotitas) >> |ENTER|"
    print "kk) >> (Kerasmenes Kanates) |ENTER| >> (Arithmo posotitas) >> |ENTER|"
    print ""
    print "<<tamio>> gia Z"
    
def tipoma_katanalosis():
    
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

def tipoma_tamio():
    print ""
    print "################ Tamio Z #################"
    print ""
    print "Tamio:",tamio, "Euro"
    print ""
    print "Kerasmata:",kerasmeno_tamio, "Euro"
    print ""
    
# Sinartisis katagrafis tipomatos katanalosis - tamiou ston xristi se arxeio
def arxeio_katanalosi():
    
    orig_stdout = sys.stdout
    arxeio = file('tamio.txt', 'w')
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

def arxeio_tamio():
    
    #Edw yparxei mia xrisimi loopa oste na mporoume
    #na tiponoume tin print se arxio kai meta na klinoume to arxeio
    #oste na mporesoume na paroume print kai stin othoni
    #xoris na katagraftoun oloi h eksodos tou programatos se arxeio.
    
    orig_stdout = sys.stdout #Auti h metavliti dimiourgithike gia na
                             #apeleftherosoume stin poria tin timi tis sys.stdout apo to
                             #arxeio pou tha kanoume open gia na mporesou me na to klisoume
    arxeio = file('tamio.txt', 'a')
    
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
    
   

#Ektelesi programatos

while True:
    
    tipoma_proionton()
    tipoma_katanalosis()
    arxeio_katanalosi()
    
    choose = raw_input("Idos CHECK: ")
    
    #An o xristis den dosi timi tamio tote mporei na dilosi tin posotita tou proiontos   
    if choose != "tamio":
        
        #Elengxos tis posotitas an einai arithmos
        try:
            posotita = 0
            posotita = int(raw_input("posotita: "))
            
        except:
            print ""
            print "H timh tis posotitas prepei na einai arithmos"
            print ""
            time.sleep(2)
            
#Pota      
    if choose == "p":
        proionta['pota']['apla_pota'] += int(posotita)

    elif choose == "kp":
        kerasmena['pota']['kerasmena_apla_pota'] += int(posotita)
      
    elif choose == "sp":
        proionta['pota']['special_pota'] += int(posotita)
        
    elif choose == "ksp":
        kerasmena['pota']['kerasmena_special_pota'] += int(posotita)
        
#Fiales        
    elif choose == "f":
        
        proionta['fiales']['aples_fiales'] += int(posotita)

    elif choose == "kf":
        
        kerasmena['fiales']['kerasmenes_aples_fiales'] += int(posotita)
        
    elif choose == "sf":
        
        proionta['fiales']['special_fiales'] += int(posotita)

    elif choose == "ksf":
        
        kerasmena['fiales']['kerasmenes_special_fiales'] += int(posotita)

#Kanates
    elif choose == "k":
        
        proionta['kanates']['kanates'] += int(posotita)
        
    elif choose == "kk":
        
        kerasmena['kanates']['kerasmenes_kanates'] += int(posotita)

#Tamio        
    elif choose == "tamio":

        tamio = (proionta['pota']['apla_pota'] * timi_pota) + (proionta['pota']['special_pota'] * timi_special_pota) + (proionta['fiales']['aples_fiales'] * timi_fialis) + (proionta['fiales']['special_fiales'] * timi_special_fialis) + (proionta['kanates']['kanates'] * timi_kanatas)

        kerasmeno_tamio = (kerasmena['pota']['kerasmena_apla_pota'] * timi_pota) + (kerasmena['pota']['kerasmena_special_pota'] * timi_special_pota) + (kerasmena['fiales']['kerasmenes_aples_fiales'] * timi_fialis) + (kerasmena['fiales']['kerasmenes_special_fiales'] * timi_special_fialis) + (kerasmena['kanates']['kerasmenes_kanates'] * timi_kanatas)

        tipoma_tamio()
        arxeio_tamio()
        break
             
    else:
        print ""
        print ""
        print "H epilogi", choose, "den yparxei... "
        time.sleep(2) #Dinoume xrono ston xristi oste na mporei na diavasi to minima prin emfanistoun oi epiloges
        
