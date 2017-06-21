from declara import *
from atribui import *
def initPrograma(i,simbolos):
    if (simbolos[i][1]=="int" and simbolos[i+1][1]=="main " and simbolos[i+2][0]=="("and simbolos[i+3][0]==")"and simbolos[i+4][0]=="{") or simbolos[i][0]=="{":
        if i+1 < len(simbolos):
            i=nextsimb(i)
            i=nextsimb(i)
            i=nextsimb(i)
            i=nextsimb(i)
            i=nextsimb(i)
            print simbolos[i]
            i = programa(i,simbolos)
            if  simbolos[i][0]=="}":
                i = nextsimb(i)
                return i
            else:
                erro("abacat1")
                return i
        else:
            erro("abacat1")
            return i


def programa2(i,simbolos):
    if simbolos[i][0]==";":
        if i+1 < len(simbolos):
            i=nextsimb(i)
            i = programa(i,simbolos)
    else:
        erro("abacate2")
    return i
def programa(i,simbolos):
    if(simbolos[i][0]=="IDENTIFICADOR"):
        print simbolos[i]
        i = atribui(i,simbolos)
        i = programa2(i,simbolos)
        print str(i) +": finalizou aqui - atribuicao"
        return i
    elif(simbolos[i][1]=="int" or simbolos[i][1]=="float" or simbolos[i][1]=="char"):
        i = declara(i,simbolos)
        i = programa2(i,simbolos)
        print str(i) +": finalizou aqui - declaracao"
        return i
    elif simbolos[i][0] == "}":
        return i
    else:
        erro("abacate3 "+str(simbolos[i]))
        return i
def nextsimb(i):
	i = i+1
	return i
