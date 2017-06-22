from anasinExpresArit import *
from program import *
def atribui(i,simbolos):
    if(simbolos[i][0]=="IDENTIFICADOR"):
        i = nextsimb(i)
        if(simbolos[i][0]=="="):
            i = nextsimb(i)
            i = E(i,simbolos)
            return i
        else:
            erro(str(simbolos[i]))
            return i
    else:
        print i
        erro(str(simbolos[i]))
        return i
