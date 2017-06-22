from anasinExpresArit import *
listInt = []
listFloat = []
listChar = []
listIds = []
def initPrograma(i,simbolos):
    if (simbolos[i][1]=="int" and simbolos[i+1][1]=="main " and simbolos[i+2][0]=="("and simbolos[i+3][0]==")"and simbolos[i+4][0]=="{"):

        if i+1 < len(simbolos):
            i=nextsimb(i)
            i=nextsimb(i)
            i=nextsimb(i)
            i=nextsimb(i)
            i=nextsimb(i)
            i = programa(i,simbolos)
        #    print(simbolos[i])
            if  simbolos[i][0]=="}":
                i = nextsimb(i)
                return i
            else:
                erro(str(simbolos[i]))
                return i
    elif simbolos[i][0]=="{":
        i=nextsimb(i)
        i = programa(i,simbolos)
    #    print(simbolos[i])
        if  simbolos[i][0]=="}":
            i = nextsimb(i)
            return i
        else:
            erro(str(simbolos[i]))
            return i
    else:
        erro(str(simbolos[i]))
        return i
def programa2(i,simbolos):
    #print str(simbolos[i])
    if simbolos[i][0]==";" and i+1 < len(simbolos):
        i=nextsimb(i)
        i = programa(i,simbolos)
    elif simbolos[i-1][0]=="}"and i+1 < len(simbolos):
        #i=nextsimb(i)
        i = programa(i,simbolos)
    elif simbolos[i][0]=="}"and i+1 == len(simbolos):
        return i
    else:
        erro(str(simbolos[i]))
    return i
def programa(i,simbolos):
    if(simbolos[i][0]=="IDENTIFICADOR"):
        #print simbolos[i]
        i = atribui(i,simbolos)
        i = programa2(i,simbolos)
#        print str(i) +": finalizou aqui - atribuicao"
        return i
    elif(simbolos[i][1]=="int" or simbolos[i][1]=="float" or simbolos[i][1]=="char"):
        i = declara(i,simbolos)
        i = programa2(i,simbolos)
    #    print str(i) +": finalizou aqui - declaracao"
        return i
    elif simbolos[i][1] == "while":
        #i = repeti(i,simbolos)
        i = nextsimb(i)
        i = E(i,simbolos)
        if(simbolos[i][0]=="{"):
            i = initPrograma(i,simbolos)
    #        print str(simbolos[i])
        else:
            erro("repeticao" + str(simbolos[i]))
        i = programa2(i,simbolos)
    #    print str(i) +": finalizou aqui - while" + str(simbolos[i])
        return i
    elif simbolos[i][1] == "if":
        i = nextsimb(i)
        i = E(i,simbolos)
        if(simbolos[i][0]=="{"):
            i = initPrograma(i,simbolos)
            #print str(simbolos[i])
        else:
            erro("condicao" + str(simbolos[i]))
        i = programa2(i,simbolos)
    #    print str(i) +": finalizou aqui - if" + str(simbolos[i])
        return i
    else:
        if simbolos[i][0] == "}":
            return i
        erro(+str(simbolos[i])+" - "+str(i))
        return i
def nextsimb(i):
	i = i+1
	return i
def declara(i,simbolos):
    tipo = simbolos[i][1]
    i = nextsimb(i)
    if(simbolos[i][0]=="IDENTIFICADOR"):
        addTabelaVarTipo(i,simbolos,tipo)
        if simbolos[i+1][0]=="=":
            i = atribui(i,simbolos)
        else:
            i = nextsimb(i)
        #print i
        i = declara2(i,simbolos,tipo)
        if(simbolos[i][0]==";"):
            return i
        else:
            erro(str(simbolos[i]))
            return i
    else:
        erro(str(simbolos[i]))
        return i
def declara2(i,simbolos,tipo):
    if (simbolos[i][0]=="comma"):
        i= nextsimb(i)
        if(simbolos[i][0]=="IDENTIFICADOR"):
            addTabelaVarTipo(i,simbolos,tipo)
            if simbolos[i+1][0]=="=":
                i = atribui(i,simbolos)
            else:
                i = nextsimb(i)
        else:
            erro(str(simbolos[i]))
        i = declara2(i,simbolos,tipo)
        return i
    else:
        return i
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
def addTabelaVarTipo(i,simbolos,tipo):
    if tipo=="int":
        if simbolos[i][1] not in listIds:
            listInt.append("["+tipo+","+simbolos[i][1]+","+simbolos[i][2]+"]")
            listIds.append(simbolos[i][1])
            print listInt
        else:
            print "O identificador "+simbolos[i][1]+" ja foi declarado. Declaracao dupla em "+simbolos[i][2]
    elif tipo=="float":
        if simbolos[i][1] not in listIds:
            listFloat.append("["+tipo+","+simbolos[i][1]+","+simbolos[i][2]+"]")
            listIds.append(simbolos[i][1])
            print listFloat
        else:
            print "O identificador "+simbolos[i][1]+" ja foi declarado. Declaracao dupla em "+simbolos[i][2]
    elif tipo=="char":
        if simbolos[i][1] not in listIds:
            listChar.append("["+tipo+","+simbolos[i][1]+","+simbolos[i][2]+"]")
            listIds.append(simbolos[i][1])
            print listChar
        else:
            print "O identificador "+simbolos[i][1]+" ja foi declarado. Declaracao dupla em "+simbolos[i][2]
