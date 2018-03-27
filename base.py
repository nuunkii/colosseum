import random
#MC= [0:Name,1:HP,2:Str,3:End,4:Dex,5:Int,6:Lck,7:XP,8:LvlCap,9:Lvl]
MC = ["",100,5,5,5,5,5,0,100,1]
#MCE= [0:Adj1,1:Wpn1,2:Adj2,3:Wpn2]
MCE = ["","","",""]

Str1Wpn = ["Axe","Hammer","Sword"]
Str2Wpn = ["Claymore","War Hammer","Halberd"]
EndWpn  = ["Buckler","Shield","Tower Shield"]
Dex1Wpn = ["Dagger","Rapier","Katana"]
Dex2Wpn = ["Scythe","Twinblade","Bow"]
Int1Wpn = ["Wand","Talisman"]
Int2Wpn = ["Staff","Catlyst"]

AdjStrWpn = ["Heavy","Long","Light","Short"]
AdjEndWpn = ["Spiked","Reinforced"]
AdjDexWpn = ["Sharp","Long","Poisonned","Short"]
AdjMagWpn = ["Fire","Frost","Wind"]
AdjSrcWpn = ["Light","Dark","Void"]

def NewWpn():
    x = random.randrange(6)
    if x == 0:
        wpn = random.choice(Str1Wpn)
    elif x == 1:
        wpn = random.choice(Str2Wpn)
    elif x == 2:
        wpn = random.choice(EndWpn)
    elif x == 3:
        wpn = random.choice(Dex1Wpn)
    elif x == 4:
        wpn = random.choice(Dex2Wpn)
    elif x == 5:
        wpn = random.choice(Int1Wpn)
    elif x == 6:
        wpn = random.choice(Int2Wpn)
    return wpn

MC[0]=input("Enter your name : ")
new_weapon = NewWpn
tak_weapon = input("Do you 
