from declara import *
from atribui import *
def programa2(i,simbolos):
    if simbolos[i][0]==";":
        if i+1 < len(simbolos):
            if simbolos[i+1][0] == "}":
                i=nextsimb(i)#para funcionar por enquanto, sem while ou if
            i=nextsimb(i)
            i = programa(i,simbolos)
    else:
        erro()
    return i
def programa(i,simbolos):
    if(simbolos[i][0]=="IDENTIFICADOR"):
        i = atribui(i,simbolos)
        i = programa2(i,simbolos)
        print str(i) +": finalizou aqui - atribuicao"
        return i
    elif(simbolos[i][1]=="int" or simbolos[i][1]=="float" or simbolos[i][1]=="char"):
        i = declara(i,simbolos)
        i = programa2(i,simbolos)
        print str(i) +": finalizou aqui - declaracao"
        return i
    else:
        erro()
        return i
def nextsimb(i):
	i = i+1
	return i
