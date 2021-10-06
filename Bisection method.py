import matplotlib.pyplot as plt
import numpy as np

laskuri = 0
funktio = input("Anna funktio: ")
maara = int(input("Anna tulostettavien nollakohtien määrä: "))
alkuarvo = int(input("Anna alkuarvo: "))
loppuarvo = int(input("Anna loppuarvo: "))
tarkkuus = int(input("Anna vastauksen haluttu tarkkuus: "))


def f(x):
    kasittely = eval(funktio)
    return kasittely

if f(alkuarvo) > 0 and f(loppuarvo) < 0 or f(alkuarvo) < 0 and f(loppuarvo) > 0:
    vali = f"]{alkuarvo}, {loppuarvo}["
    print(f"Funktion nollakohta on välillä {vali}.")

    x = np.linspace(-6, 6, num=1000)
    y = f(x)

    fig, ax = plt.subplots()
    plt.grid()
    ax.plot(x,y, color="blue")
    ax.set_aspect('equal')
    ax.grid(True, which='both')
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')
    ax.set_xlim(-3, 5)
    ax.set_ylim(-3, 5)

    plt.plot(x, y, label="f(x)")
    plt.legend()
    plt.xlabel("x - akseli")
    plt.ylabel("y - akseli")
    plt.title("Kuvaaja")
    plt.show()

    while laskuri <= maara:
        keskikohta = 0.5 * (alkuarvo + loppuarvo)
        arvo_a = f(alkuarvo)
        arvo_c = f(keskikohta)
        tulo_ac = arvo_a * arvo_c
        laskuri += 1
        if tulo_ac >= 0:
            alkuarvo = keskikohta
        elif tulo_ac <= 0:
            loppuarvo = keskikohta
    print("c =", round(keskikohta, tarkkuus))

else:
    vali = f"]{alkuarvo}, {loppuarvo}["
    print(f"Funktiolla ei ole nollakohtaa välillä {vali}.")

