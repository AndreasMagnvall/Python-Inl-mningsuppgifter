#!/usr/bin/python


def create_shopping_list():
    slist = ["1. Kurslitteratur", "2. Anteckningsblock", "3. Penna"]
    return slist


def shopping_add(slist = []):
    print("Vad ska läggas till i listan?")
    inp = input()
    inp = str(len(slist) + 1) + ". " + inp
    slist.append(inp)
    return


def shopping_remove(slist = []):
    print("Vilken sak vill du ta bort ur listan?")
    inp = input()
    slist.remove(inp)
    return

def shopping_edit(slist):
    print("Vilken sak vill du ändra på?")
    inp = input()
    print("Vad ska det stå istället för " + slist.index(inp) + "?")
    return

def shopping_list(slist):
    for x in slist:
        print(x)
    return


slist = create_shopping_list()
shopping_list(slist)