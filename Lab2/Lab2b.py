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
    inp = int(input())
    slist.pop(inp -1)

    for number in range(inp-1, len(slist)):
        slist[number] = list(slist[number])
        slist[number][0] = str(number+1)
        slist[number] = "".join(slist[number])
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
shopping_add(slist)
shopping_list(slist)
shopping_remove(slist)
shopping_list(slist)