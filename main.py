import random
import os
import colors

# innentől lehet terminálszíneket használni.
if __name__ == "__main__":
    os.system("color")


rendeles_tipusok = []
rendeles_meretek = []
rendeles_feltetek = []
rendeles_arak = []

pizza_tipusok = ["sajtos", "gombás", "sonkás"]
pizza_tipus_arak = [1000, 1100, 1200]

pizza_meretek = ["kicsi", "normál", "nagy"]
pizza_meret_arak = [0.9, 1.0, 1.1]

feltet_ar = 50

def keretez(szoveg, szelesseg):
    sorok = szoveg.split("\n")
    # {colors.bcolors.GREEN}*\n *{colors.bcolors.ENDC}
    ki_sorok = [colors.bcolors.GREEN + ('*' * (szelesseg - 1)) + colors.bcolors.ENDC]
    i = 0
    while i < len(sorok):
        ki_sorok.append(f" {sorok[i]:<{szelesseg - 4}} ")
        i += 1
    ki_sorok .append(ki_sorok[0])
    return f"{colors.bcolors.GREEN}*\n*{colors.bcolors.ENDC}".join(ki_sorok)


def rendeles_felvetel_random(db):

    i = 0
    while i < db:
        rendeles_tipusok.append(int(random.random() * 3))
        rendeles_meretek.append(int(random.random() * 3))
        rendeles_feltetek.append(int(random.random() * 2))
        i += 1

def rendeles_felvetel():
    vege = False
    while not vege:
        print(keretez("Válassz egy pizza típust!\n1. Sajtos\n2. Gombás\n3. Sonkás", 30))
        tipus = input("Típus vagy @: ")
        if tipus in ["1", "2", "3"]:
            meret = ""
            while meret not in ["1", "2", "3"]:
                print(keretez("Válassz egy pizza méretet!\n1. Kicsi\n2. Normál\n3. Nagy", 30))
                meret = input("Méret: ")
            feltet = ""
            while feltet not in ["I", "N"]:
                print("Döntsd el, hogy kérsz-e extra feltétet a pizzára.")
                feltet = input("Extra feltét: [I/N]: ").upper()

            rendeles_tipusok.append(int(tipus) - 1)
            rendeles_meretek.append(int(meret) - 1)
            rendeles_feltetek.append(feltet == "I")
        elif tipus == "@":
            vege = True
        else:
            print("Érvénytelen választás!")


def arszamitas():

    i = 0
    while i < len(rendeles_tipusok):

        ar = pizza_tipus_arak[rendeles_tipusok[i]] * pizza_meret_arak[rendeles_meretek[i]]

        if rendeles_feltetek[i]:
            ar += feltet_ar

        rendeles_arak.append(ar)
        i += 1


# 1. Melyik típusú (név alapján) pizzából hány darab fogyott?
def statisztika1():

    fogyasztas = [0] * len(pizza_tipusok)
    i = 0
    while i < len(rendeles_tipusok):
        fogyasztas[rendeles_tipusok[i]] += 1
        i += 1

    return fogyasztas


# 2. Melyik pizzából fogyott a legtöbb?
def statisztika2():
    legtobb_idx = 0
    i = 1
    while i < len(fogyasztas_tipus):
        if fogyasztas_tipus[i] > fogyasztas_tipus[legtobb_idx]:
            legtobb_idx = i
        i += 1
    return legtobb_idx


# 3. Mekkora volt a bevétel?
def statisztika3():
    i = 0
    osszbevetel = 0
    while i < len(rendeles_arak):
        osszbevetel += rendeles_arak[i]
        i += 1
    return osszbevetel


# 4. Hányszor kértek extra feltétet?
def statisztika4():
    i = 0
    feltetek = 0
    while i < len(rendeles_arak):
        if rendeles_feltetek[i]:
            feltetek += 1
        i += 1
    return feltetek


# 5. A kicsi, nagy, vagy a közepes pizzából rendeltek-e többet?
def statisztika5():

    fogyasztas = [0] * len(pizza_meretek)
    i = 0
    while i < len(rendeles_meretek):
        fogyasztas[rendeles_meretek[i]] += 1
        i += 1

    return fogyasztas

# 5/b. Melyik pizza méretből fogyott a legtöbb?
def statisztika5b():
    legtobb_idx = 0
    i = 1
    while i < len(fogyasztas_meret):
        if fogyasztas_meret[i] > fogyasztas_meret[legtobb_idx]:
            legtobb_idx = i
        i += 1

    return legtobb_idx


rendeles_felvetel()
# rendeles_felvetel_random(10)
arszamitas()

print(f"\n{colors.bcolors.YELLOW}# 1. Melyik típusú (név alapján) pizzából hány darab fogyott?{colors.bcolors.ENDC}")
i = 0
fogyasztas_tipus = statisztika1()
while i < len(pizza_tipusok):
    if fogyasztas_tipus[i] > 0:
        print(f"A {pizza_tipusok[i]} pizzából {fogyasztas_tipus[i]} fogyott.")
    else:
        print(f"A {pizza_tipusok[i]} pizzából nem fogyott egy darab se.")
    i += 1

print(f"\n{colors.bcolors.YELLOW}# 2. Melyik pizzából fogyott a legtöbb?{colors.bcolors.ENDC}")
legtobb_fogyott = statisztika2()

print(f"A {pizza_tipusok[legtobb_fogyott]} pizzából fogyott a legtöbb.")

print(f"\n{colors.bcolors.YELLOW}# 3. Mekkora volt a bevétel?{colors.bcolors.ENDC}")
osszbevetel = statisztika3()
print(f"Az összbevétel {osszbevetel:.0f} Ft volt.")

print(f"\n{colors.bcolors.YELLOW}# 4. Hányszor kértek extra feltétet?{colors.bcolors.ENDC}")
feltetek = osszbevetel = statisztika4()
print(f"{feltetek} alkalommal kértek feltétet a pizzára.")

print(f"\n{colors.bcolors.YELLOW}# 5. A kicsi, nagy, vagy a közepes pizzából rendeltek-e többet?{colors.bcolors.ENDC}")
i = 0
fogyasztas_meret = statisztika5()
while i < len(pizza_meretek):
    if fogyasztas_meret[i] > 0:
        print(f"A {pizza_meretek[i]} pizzából {fogyasztas_meret[i]} fogyott.")
    else:
        print(f"A {pizza_meretek[i]} pizzából nem fogyott egy darab se.")
    i += 1

legtobb_fogyott_meret = statisztika5b()

print(f"A {pizza_meretek[legtobb_fogyott_meret]} pizzából fogyott a legtöbb.")

print(f"\n{colors.bcolors.YELLOW}*** Rendelések listája ***{colors.bcolors.ENDC}")
i = 0
while i < len(rendeles_tipusok):
    tipus = pizza_tipusok[rendeles_tipusok[i]]
    meret = pizza_meretek[rendeles_meretek[i]]

    # feltet = "Feltéttel" if rendeles_feltetek[i] else "Feltét nélkül"
    if rendeles_feltetek[i]:
        feltet = "Feltéttel"
    else:
        feltet = "Feltét nélkül"

    print(f"{tipus.capitalize():<7} {meret.capitalize():<7} {feltet:<14} {rendeles_arak[i]:>6.0f} Ft")
    i += 1
