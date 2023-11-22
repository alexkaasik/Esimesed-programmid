from math import pi

print("----Ülesanne 1----\n")
print("Hello World")
print("\n----Ülesanne 2----\n")

print("3 + 8 / (4 - 2) * 4 =",3 + 8 / (4 - 2) * 4)
print("3 + 8 / 4 - (2 * 4) =",3 + 8 / 4 - (2 * 4))
print("3 + 8 / (4 - 2 * 4) =",3 + 8 / 4 - 2 * 4)
print("(3 + 8) / (4 - 2) * 4 =",3 + 8 / (4 - 2) * 4)
print("(3 + 8) / 4 - (2 * 4) =",(3 + 8) / 4 - (2 * 4))
print("(3 + 8) / (4 - 2 * 4) =",(3 + 8) / 4 - 2 * 4)
print("3 + 8 / 4 - 2 * 4 =",3 + 8 / 4 - 2 * 4)

print("\n---Ülesanne 2.1---\n")
Radius=3
print("Ringi raadius on",Radius)
Cube=Radius*2
print("")
print("ruudu pindala =", Cube**2)
print("ruudu ümbermõõt =",Cube*4)
print("ringi pindala =", pi*Radius**2) 
print("ringi ümbermõõt =", 2*pi*Radius)

print("\n---Ülesanne 2.2---\n")

Earth_Radius=6378 # km
Euro2 = 25.75 # mm

km_mm = 1000*1000

Earth_Pere=round((2*pi*Earth_Radius)*km_mm,2)

Answer=int(Earth_Pere/Euro2)

print(Answer,"coins")

print("\n----Ülesanne 3----\n")
# if needed use 1 print but need 2 print line, here var and print
KK1="kill-koll kill-koll killadi-koll kill-koll kill-koll killadi-koll kill-koll kill-koll killkoll\nkill-koll"
print(KK1)

print("\n----Ülesanne 4----\n")

option=str(input("tsush(0)/tuut(1): "))

if (option == "0") or (option == "tsuhh") :
    ttk0="tsuhh tsuhh tsuhh"
    ttk1="rat tat taa"
    ttk2="tat tat taa"
if (option == "1") or (option == "tuut"):
    ttk0="tuut tuut tuut"
    ttk1="kill koll koll"
    ttk2="kill koll kill"

print("Rong see sõitis", ttk0,"\b,")
print("piilupart oli rongijuht.")
print("Rattad tegid", ttk1,"\b,")
print(ttk1, "ja",ttk2 , "\b.")

print("\n----Ülesanne 5----\n")

As = int(input("A ristküliku[int]: "))
Bs = int(input("B ristküliku[int]: "))

print("ümbermõõdu ristküliku:", 2*(As+Bs))
print("pindala ristküliku:", As*Bs)

print("\n----Ülesanne 6----\n")

fuel = int(input("tangitud kütuse liitrid[int]: "))
travel = int(input("läbitud kilomeetrid[int]: "))
print( (fuel / 100) * travel,"Kütusekulu" )

print("\n----Ülesanne 7----\n")

print("M jõuab",int((29.9*3.6)), "meter")

print("\n----Ülesanne 8----\n")

timer=int(input("Give a number[int]: "))
if timer >= 3600: # hour
    print(int(((timer-timer%3600)/3600)%24, end="", flush=True))
    print(":", end="", flush=True)
if timer >= 60: # min
    print(int(((timer-timer%60)/60)%60), end="", flush=True)
    print(":", end="", flush=True)
print(timer%60)
