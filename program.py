from declara import *
from atribui import *
def programa(i,simbolos):
    if(simbolos[i][0]=="IDENTIFICADOR"):
        i = atribui(i,simbolos)
        if simbolos[i][0]==";":
            if i+1 < len(simbolos):
                i=nextsimb(i)
                i = programa(i,simbolos)
        else:
            erro()
        print str(i) +": finalizou aqui - atribuicao"
        return i
    elif(simbolos[i][1]=="int" or simbolos[i][1]=="float" or simbolos[i][1]=="char"):
        i = declara(i,simbolos)
        if simbolos[i][0]==";":
            if i+1 < len(simbolos):
                i=nextsimb(i)
                i = programa(i,simbolos)
        else:
            erro()
        print str(i) +": finalizou aqui - declaracao"
        return i
    else:
        erro()
        return i
def nextsimb(i):
	i = i+1
	return i
