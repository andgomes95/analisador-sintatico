from anasinExpresArit import *
from program import *
def repeti(i,simbolos):
    if(simbolos[i][1]=="while"):
        i = nextsimb(i)
        i = E(i,simbolos)
        if(simbolos[i][0]=="{"):
            i = initPrograma(i,simbolos)
            return i
        else:
            erro("repeti")
            return i
    else:
        erro("repeti")
        return i
