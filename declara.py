from program import *
from atribui import *
def declara(i,simbolos):
    i = nextsimb(i)
    if(simbolos[i][0]=="IDENTIFICADOR"):
        if simbolos[i+1][0]=="=":
            i = atribui(i,simbolos)
        else:
            i = nextsimb(i)
        #print i
        i = declara2(i,simbolos)
        if(simbolos[i][0]==";"):
            return i
        else:
            erro1()
            return i
    else:
        erro0()
        return i
def declara2(i,simbolos):
    if (simbolos[i][0]=="comma"):
        i= nextsimb(i)
        if(simbolos[i][0]=="IDENTIFICADOR"):
            if simbolos[i+1][0]=="=":
                i = atribui(i,simbolos)
            else:
                i = nextsimb(i)
        else:
            erro0()
        i = declara2(i,simbolos)
        return i
    else:
        return i